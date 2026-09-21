"""Bounded diagnostics for the unmodified LavaLM audit revision.

Run with PYTHONPATH=/path/to/LavaLM/src python reproduce_findings.py.
Expected output describes defects, not passing regression assertions.
No network, hardware, or live Lava actors are required.
"""
import json
import logging
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch
import numpy as np
from scipy.sparse import csr_matrix

results=[]
def record(id,description,fn):
    try: outcome=fn()
    except Exception as exc: outcome=f'{type(exc).__name__}: {exc}'
    results.append(dict(id=id,diagnostic=description,observed=outcome))

def import_context():
    run=subprocess.run([sys.executable,'-c',"import multiprocessing as mp; mp.set_start_method('spawn'); import lava.magma.runtime.runtime"],capture_output=True,text=True,timeout=10)
    return dict(exit_code=run.returncode,last_stderr=run.stderr.splitlines()[-1])
record('R01','Import after application selects spawn',import_context)

from lava.magma.runtime.runtime import Runtime
from lava.magma.core.process.process import AbstractProcess
from lava.magma.core.run_conditions import RunSteps
from lava.magma.core.learning.learning_rule import LoihiLearningRule
from lava.magma.compiler.compiler_graphs import flatten_list_recursive
from lava.magma.runtime.mgmt_token_enums import MGMT_RESPONSE
from lava.utils.serialization import save, load
from lava.utils.sparse import find

def context_binding():
    with patch.object(Runtime,'initialize'),patch.object(Runtime,'stop'):
        rt=Runtime.__new__(Runtime);rt._is_started=False
        with rt as bound: return dict(bound_is_runtime=bound is rt,bound_type=type(bound).__name__)
record('R02','Runtime context manager as binding',context_binding)

def steps():
    return [dict(value=str(v),accepted=RunSteps(v).num_steps==v) for v in (-1,1.5,True)]
record('C01','Invalid RunSteps inputs',steps)

def log_handlers():
    before=len(logging.getLogger().handlers)
    procs=[AbstractProcess() for _ in range(3)]
    return dict(created_processes=len(procs),added_root_handlers=len(logging.getLogger().handlers)-before)
record('C02','Process construction changes host root logger',log_handlers)

def serialization():
    with tempfile.TemporaryDirectory() as d:
        p=str(Path(d)/'model')
        save(AbstractProcess(),p)
        try: load(p); load_status='loaded'
        except OSError: load_status='OSError'
        save([42],str(Path(d)/'invalid.pickle'))
        return dict(saved_with_extension=Path(p+'.pickle').exists(),load_same_argument=load_status,accepted_invalid_list=load(str(Path(d)/'invalid.pickle'))[0]==[42])
record('U01','Checkpoint path symmetry and list validation',serialization)

def sparse_readonly():
    mat=csr_matrix(([0.,2.],([0,0],[0,1])),shape=(1,2))
    mat.data.flags.writeable=False
    return str(find(mat,explicit_zeros=True))
record('U02','Read-only sparse input to a query helper',sparse_readonly)

def sparse_exception():
    mat=csr_matrix(([0.,2.],([0,0],[0,1])),shape=(1,2))
    before=mat.data.copy()
    with patch('lava.utils.sparse.scipy_find',side_effect=RuntimeError('injected lookup failure')):
        try: find(mat,explicit_zeros=True)
        except RuntimeError: pass
    return dict(before=before.tolist(),after=mat.data.tolist())
record('U03','Sparse query restores input after downstream failure',sparse_exception)

def flat(): return len(flatten_list_recursive(list(range(2000))))
record('K01','Compiler flatten helper with 2000 siblings',flat)

def make_runtime():
    rt=Runtime.__new__(Runtime);rt._is_started=True;rt._is_running=False
    ev=SimpleNamespace(runtime_srv_id=0,proc_id=1,shape=(2,),dtype=np.int64)
    rt._executable=SimpleNamespace(node_configs=[SimpleNamespace(var_models={0:ev})],runtime_service_builders={0:SimpleNamespace(rs_class=object)})
    rt.runtime_to_service=[Mock()]
    return rt

def set_index():
    rt=make_runtime()
    rt.service_to_runtime=[Mock()]
    try:
        Runtime.set_var(rt,0,np.array([10,20]),idx=np.array([0,1]))
    except Exception as e:
        return dict(error=f'{type(e).__name__}: {e}',messages_sent_before_error=rt.runtime_to_service[0].send.call_count)
    finally: rt._is_started=False
record('R03','Array index is validated after SET header transmission',set_index)

def get_index():
    rt=make_runtime();rt.service_to_runtime=[Mock()]
    rt.service_to_runtime[0].recv.side_effect=[np.array([2]),np.array([10]),np.array([20])]
    try: return dict(index=0,returned=Runtime.get_var(rt,0,idx=0).tolist())
    finally: rt._is_started=False
record('R04','Runtime get index zero',get_index)

def delay_dtype():
    from lava.proc.sparse.process import DelaySparse
    return str(DelaySparse(weights=csr_matrix([[1,2]]),delays=csr_matrix(np.array([[0,1]],dtype=np.int32))))
record('P01','DelaySparse int32 delays',delay_dtype)

def invalid_epoch():
    return dict(epoch=LoihiLearningRule(dw='x0',t_epoch=1.5).t_epoch,nan_tau=bool(np.isnan(LoihiLearningRule(dw='x0',x1_tau=float('nan')).x1_tau)))
record('L01','Learning rule fractional epoch and NaN tau',invalid_epoch)

def conv_equivalence():
    a=np.arange(12).reshape(3,4);a[:,0]=0
    return dict(flat_roll_equals_axis_roll=bool(np.array_equal(np.roll(a,-1),np.roll(a,-1,axis=1))))
record('REJECT01','Check suspected ConvInTime cross-row roll defect',conv_equivalence)

def outport_config():
    from lava.magma.compiler.subcompilers.py.pyproc_compiler import PyProcCompiler, ChannelBuildersFactory
    from lava.magma.core.process.ports.connection_config import ConnectionConfig
    compiler=PyProcCompiler.__new__(PyProcCompiler)
    compiler._compile_config={'pypy_channel_size':64}
    compiler._tmp_channel_map=Mock()
    ports=[SimpleNamespace(name='out'+str(i),shape=(1,),connection_configs={'peer':ConnectionConfig()},get_incoming_transform_funcs=lambda: {}) for i in range(2)]
    with patch.object(ChannelBuildersFactory,'get_port_dtype',return_value=np.int32):
        return len(compiler._create_outport_initializers(SimpleNamespace(out_ports=ports)))
record('K02','Two output ports each with one connection configuration',outport_config)

def collection_restart():
    from lava.magma.core.process.process import Collection
    c=Collection(SimpleNamespace(name='p'),'test');c.add_members({'a':1,'b':2,'c':3})
    first=next(iter(c));remaining=list(c)
    return dict(first=first,new_iteration=remaining)
record('C03','Independent iteration after an early break',collection_restart)

def zero_interval():
    from lava.proc.io.dataloader import StateDataloader
    return StateDataloader(dataset=[(np.ones(1),0)],interval=0)
record('I01','Dataloader zero interval',zero_interval)

def failed_cleanup():
    from lava.magma.runtime.message_infrastructure.shared_memory_manager import SharedMemoryManager
    manager=SharedMemoryManager()
    manager.shutdown()
    return 'cleaned'
record('R05','Shared memory cleanup before manager starts',failed_cleanup)

# Print observations; never overwrite the committed historical evidence.
print(json.dumps(results,indent=2))
