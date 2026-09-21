# Copyright (C) 2023 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause
# See: https://spdx.org/licenses/

import typing as ty

from scipy.sparse import csr_matrix, find as scipy_find


def find(mat: csr_matrix,
         explicit_zeros: bool = False) -> ty.Tuple:
    """Behaves like scipy.sparse.find but also returns explict zeros.

    Parameters
    ==========
    mat: csr_matrix
        Return col, row and values of this sparse matrix.
    explicit_zeros: bool
        Include explicit zeros
    """
    if not explicit_zeros:
        return scipy_find(mat)

    # Preserve the caller's storage, including when scipy_find raises or the
    # input data is read-only. Keep scipy's ordering/coalescing semantics.
    nonzero_pattern = mat.copy()
    nonzero_pattern.data[nonzero_pattern.data == 0] = 1
    dst, src, _ = scipy_find(nonzero_pattern)

    vals = mat[dst, src].A1  # A1 returns values in flattened array

    return dst, src, vals
