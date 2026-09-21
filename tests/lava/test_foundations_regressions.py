# SPDX-License-Identifier: BSD-3-Clause
"""Bounded regression cases for the first LavaLM maintenance batch."""

import pickle
from contextlib import nullcontext
from unittest.mock import patch

import numpy as np
import pytest
from scipy.sparse import csr_matrix, isspmatrix_csr

from lava.magma.compiler.compiler_graphs import flatten_list_recursive
from lava.magma.core.process.process import AbstractProcess, Collection
from lava.magma.core.process.variable import Var
from lava.magma.runtime.runtime import Runtime
from lava.networks import gradedvecnetwork
from lava.utils import serialization, sparse


def test_collection_traversals_are_independent():
    collection = Collection(AbstractProcess(), "variables")
    first, second = Var((1,)), Var((1,))
    collection.add_members({"first": first, "second": second})
    partial = iter(collection)
    assert next(partial) is first
    assert list(collection) == [first, second]
    assert list(partial) == [second]
    assert [(a, b) for a in collection for b in collection] == [
        (first, first), (first, second), (second, first), (second, second)]


def test_collection_iterator_snapshots_membership():
    collection = Collection(AbstractProcess(), "variables")
    first, second = Var((1,)), Var((1,))
    collection.add_members({"first": first})
    snapshot = iter(collection)
    collection.add_members({"second": second})
    assert list(snapshot) == [first]
    assert list(collection) == [first, second]
    # Retain the historical direct next(collection) interface.
    assert next(collection) is first


def test_flatten_wide_and_deep_lists_preserves_leaves():
    wide = list(range(3000))
    assert flatten_list_recursive(wide) == wide
    nested = ["leaf"]
    for _ in range(3000):
        nested = [nested]
    assert flatten_list_recursive(nested) == ["leaf"]
    assert flatten_list_recursive([[], [1, [2]], (3, 4)]) == [1, 2, (3, 4)]
    assert flatten_list_recursive([]) == []


@pytest.mark.parametrize("fails", [False, True])
def test_process_context_binds_self_and_stops(fails):
    process = AbstractProcess()
    with patch.object(process, "stop") as stop:
        with pytest.raises(ValueError) if fails else nullcontext():
            with process as active:
                assert active is process
                if fails:
                    raise ValueError("body failure")
        stop.assert_called_once_with()


@pytest.mark.parametrize("fails", [False, True])
def test_runtime_context_binds_self_and_stops(fails):
    runtime = Runtime(exe=None, message_infrastructure_type=None)
    with patch.object(runtime, "initialize") as initialize, \
            patch.object(runtime, "stop") as stop:
        with pytest.raises(ValueError) if fails else nullcontext():
            with runtime as active:
                assert active is runtime
                initialize.assert_called_once_with()
                if fails:
                    raise ValueError("body failure")
        stop.assert_called_once_with()


def stored_zero_matrix():
    return csr_matrix(([0., 2., -3.], ([0, 0, 1], [0, 2, 1])),
                      shape=(2, 3))


def test_sparse_find_readonly_with_explicit_zeros():
    matrix = stored_zero_matrix()
    original = matrix.data.copy()
    matrix.data.flags.writeable = False
    rows, columns, values = sparse.find(matrix, explicit_zeros=True)
    assert sorted(zip(rows, columns, values)) == [(0, 0, 0), (0, 2, 2),
                                                (1, 1, -3)]
    np.testing.assert_array_equal(matrix.data, original)
    assert not matrix.data.flags.writeable
    assert matrix.nnz == 3
    assert len(sparse.find(matrix)[0]) == 2


def test_sparse_find_exception_preserves_input():
    matrix = stored_zero_matrix()
    original = matrix.data.copy()
    with patch.object(sparse, "scipy_find", side_effect=RuntimeError("find")):
        with pytest.raises(RuntimeError, match="find"):
            sparse.find(matrix, explicit_zeros=True)
    np.testing.assert_array_equal(matrix.data, original)


def test_sparse_find_noncanonical_input_preserves_storage():
    matrix = csr_matrix(([0., 2., 3., 0.], [2, 1, 1, 0], [0, 4]),
                        shape=(1, 3))
    original = (matrix.data.copy(), matrix.indices.copy(), matrix.indptr.copy())
    rows, columns, values = sparse.find(matrix, explicit_zeros=True)
    np.testing.assert_array_equal(rows, [0, 0, 0])
    np.testing.assert_array_equal(columns, [0, 1, 2])
    np.testing.assert_array_equal(values, [0, 5, 0])
    for actual, expected in zip(
            (matrix.data, matrix.indices, matrix.indptr), original):
        np.testing.assert_array_equal(actual, expected)


@pytest.mark.parametrize("operation, count", [("connect", 1), ("product", 3)])
def test_network_identity_is_sparse_without_dense_allocation(operation, count):
    size = 10000
    left = gradedvecnetwork.GradedVec(shape=(size,))
    right = gradedvecnetwork.GradedVec(shape=(size,))
    constructor = gradedvecnetwork.GradedSparse
    with patch.object(gradedvecnetwork, "GradedSparse",
                      wraps=constructor) as sparse_constructor, \
            patch.object(np, "eye", side_effect=AssertionError("dense eye")):
        if operation == "connect":
            left << right
        else:
            left * right
    assert sparse_constructor.call_count == count
    for call in sparse_constructor.call_args_list:
        weights = call.kwargs["weights"]
        assert isspmatrix_csr(weights)
        assert weights.shape == (size, size)
        assert weights.nnz == size
        np.testing.assert_array_equal(weights.diagonal(), np.ones(size))


@pytest.mark.parametrize("basename", ["checkpoint", ".checkpoint", "state.bin"])
def test_checkpoint_roundtrip_in_dotted_directory(tmp_path, basename):
    directory = tmp_path / "run.v1"
    directory.mkdir()
    path = directory / basename
    serialization.save([], str(path))
    expected = path if path.suffix else directory / (basename + ".pickle")
    assert expected.is_file()
    assert serialization.load(str(path)) == ([], None)


def test_checkpoint_exact_legacy_path_takes_precedence(tmp_path):
    path = tmp_path / "checkpoint"
    with path.open("wb") as stream:
        pickle.dump(serialization.SerializationObject([], None), stream)
    path.with_suffix(".pickle").write_bytes(b"not a pickle")
    assert serialization.load(str(path)) == ([], None)


def test_checkpoint_invalid_member_does_not_overwrite(tmp_path):
    path = tmp_path / "checkpoint.pickle"
    path.write_bytes(b"existing checkpoint")
    with pytest.raises(TypeError, match="only AbstractProcess"):
        serialization.save([AbstractProcess(), object()], str(path))
    assert path.read_bytes() == b"existing checkpoint"
