# Production module index

All 139 tracked production Python modules were parsed. This index lists their top-level definitions and direct imports; it is a navigation aid, not a claim of exhaustive semantic verification.

## src/lava/frameworks/loihi2.py

Chunk: 03 Core API. Lines: 14. Review: AST and structural risk scan.

Top-level definitions: none.

Direct imports: lava.networks.gradedvecnetwork, lava.networks.resfire, lava.magma.core.run_conditions, lava.magma.core.run_configs.

## src/lava/magma/compiler/builders/channel_builder.py

Chunk: 04 Compiler. Lines: 326. Review: AST and structural risk scan.

Top-level definitions: WatchdogEnabledMixin, ChannelBuilderMp, ServiceChannelBuilderMp, RuntimeChannelBuilderMp, ChannelBuilderNx, ChannelBuilderPyNc.

Direct imports: typing, dataclasses, multiprocessing, lava.magma.compiler.builders.interfaces, lava.magma.compiler.builders.runtimeservice_builder, lava.magma.compiler.channels.interfaces, lava.magma.compiler.utils, lava.magma.runtime.message_infrastructure.message_infrastructure_interface, lava.magma.compiler.channels.watchdog.

## src/lava/magma/compiler/builders/interfaces.py

Chunk: 04 Compiler. Lines: 152. Review: AST and structural risk scan.

Top-level definitions: AbstractBuilder, ResourceAddress, Resource, CompiledResource, MappedResource, AbstractProcessBuilder, AbstractChannelBuilder.

Direct imports: typing, abc, lava.magma.core.model.model.

## src/lava/magma/compiler/builders/py_builder.py

Chunk: 04 Compiler. Lines: 427. Review: AST and structural risk scan.

Top-level definitions: PyProcessBuilder.

Direct imports: typing, numpy, scipy.sparse, lava.magma.compiler.builders.interfaces, lava.magma.compiler.channels.interfaces, lava.magma.compiler.channels.pypychannel, lava.magma.compiler.utils, lava.magma.core.model.py.model, lava.magma.core.model.py.ports, lava.magma.core.model.py.type.

## src/lava/magma/compiler/builders/runtimeservice_builder.py

Chunk: 04 Compiler. Lines: 141. Review: AST and structural risk scan.

Top-level definitions: RuntimeServiceBuilder.

Direct imports: logging, typing, lava.magma.compiler.channels.interfaces, lava.magma.compiler.channels.pypychannel, lava.magma.core.sync.protocol, lava.magma.runtime.runtime_services.enums, lava.magma.runtime.runtime_services.runtime_service.

## src/lava/magma/compiler/channel_map.py

Chunk: 04 Compiler. Lines: 207. Review: AST and structural risk scan.

Top-level definitions: PortPair, Payload, lmt_init_id, ChannelMap.

Direct imports: itertools, typing, collections, dataclasses, lava.magma.compiler.compiler_graphs, lava.magma.compiler.utils, lava.magma.core.process.ports.ports, lava.magma.core.process.ports.ports, lava.magma.core.process.process.

## src/lava/magma/compiler/channels/interfaces.py

Chunk: 06 Channels. Lines: 82. Review: AST and structural risk scan.

Top-level definitions: AbstractCspPort, AbstractCspSendPort, AbstractCspRecvPort, Channel, ChannelType.

Direct imports: typing, abc, enum, numpy.

## src/lava/magma/compiler/channels/pypychannel.py

Chunk: 06 Channels. Lines: 405. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: Proto, CspSendPort, CspRecvQueue, CspRecvPort, CspSelector, PyPyChannel.

Direct imports: typing, dataclasses, multiprocessing, queue, threading, time, scipy.sparse, lava.utils.sparse, lava.magma.compiler.channels.watchdog, numpy, lava.magma.compiler.channels.interfaces.

## src/lava/magma/compiler/channels/watchdog.py

Chunk: 06 Channels. Lines: 222. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: EventMetadata, EventCompletionMonitor, WatchdogToken, Watchdog, WatchdogManagerInterface, WatchdogManager, NoOPWatchdog, NoOPWatchdogManager, WatchdogManagerBuilder.

Direct imports: typing, contextlib, datetime, multiprocessing, abc, dataclasses, atexit, threading, lava.magma.compiler.builders.interfaces.

## src/lava/magma/compiler/compiler.py

Chunk: 04 Compiler. Lines: 889. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: Compiler.

Direct imports: itertools, logging, os, pickle, typing, collections, lava.magma.compiler.var_model, numpy, lava.magma.compiler.builders.interfaces, lava.magma.compiler.builders.channel_builder, lava.magma.compiler.builders.runtimeservice_builder, lava.magma.compiler.channel_map, lava.magma.compiler.channels.interfaces, lava.magma.compiler.compiler_graphs, lava.magma.compiler.compiler_utils, lava.magma.compiler.executable, lava.magma.compiler.mapper, lava.magma.compiler.node, lava.magma.compiler.subcompilers.channel_builders_factory, lava.magma.compiler.subcompilers.interfaces, lava.magma.compiler.subcompilers.py.pyproc_compiler, lava.magma.compiler.utils, lava.magma.core, lava.magma.core.model.py.model, lava.magma.core.process.process, lava.magma.core.resources, lava.magma.core.run_configs, lava.magma.core.sync.domain, lava.magma.core.sync.protocols.async_protocol, lava.magma.runtime.runtime, lava.magma.runtime.runtime_services.enums, lava.magma.compiler.channels.watchdog.

## src/lava/magma/compiler/compiler_graphs.py

Chunk: 04 Compiler. Lines: 1143. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: ProcessModelTypes, NodeAnnotation, flatten_list_recursive, flatten_list_itertools, find_processes, annotate_folded_view, DiGraphBase, ProcDiGraph, AbstractProcGroupDiGraphs, ProcGroupDiGraphs.

Direct imports: importlib, importlib.util, inspect, itertools, os, pkgutil, sys, types, typing, abc, collections, enum, warnings, lava.magma.compiler.exceptions, networkx, lava.magma.core.model.model, lava.magma.core.model.py.model, lava.magma.core.model.sub.model, lava.magma.core.process.ports.ports, lava.magma.core.process.process, lava.magma.core.run_configs.

## src/lava/magma/compiler/compiler_utils.py

Chunk: 04 Compiler. Lines: 42. Review: AST and structural risk scan.

Top-level definitions: split_proc_builders_by_type.

Direct imports: typing, lava.magma.compiler.builders.interfaces, lava.magma.compiler.builders.py_builder, lava.magma.core.process.process.

## src/lava/magma/compiler/exceptions.py

Chunk: 04 Compiler. Lines: 18. Review: AST and structural risk scan.

Top-level definitions: NoProcessModelFound, ProcessAlreadyCompiled.

Direct imports: none.

## src/lava/magma/compiler/executable.py

Chunk: 04 Compiler. Lines: 50. Review: AST and structural risk scan.

Top-level definitions: Executable.

Direct imports: __future__, typing, dataclasses, lava.magma.compiler.builders.interfaces, lava.magma.compiler.channels.watchdog, lava.magma.core.sync.domain, lava.magma.compiler.node.

## src/lava/magma/compiler/mappable_interface.py

Chunk: 04 Compiler. Lines: 30. Review: AST and structural risk scan.

Top-level definitions: Mappable.

Direct imports: typing, abc, lava.magma.compiler.builders.interfaces.

## src/lava/magma/compiler/mapper.py

Chunk: 04 Compiler. Lines: 173. Review: AST and structural risk scan.

Top-level definitions: Mapper.

Direct imports: typing, lava.magma.compiler.builders.interfaces, lava.magma.compiler.channel_map, lava.magma.compiler.compiler_utils, lava.magma.compiler.executable, lava.magma.compiler.mappable_interface, lava.magma.compiler.subcompilers.address, lava.magma.compiler.subcompilers.constants, lava.magma.compiler.var_model.

## src/lava/magma/compiler/node.py

Chunk: 04 Compiler. Lines: 73. Review: AST and structural risk scan.

Top-level definitions: Node, NodeConfig.

Direct imports: __future__, typing, collections, lava.magma.core.resources, lava.magma.compiler.var_model.

## src/lava/magma/compiler/subcompilers/address.py

Chunk: 04 Compiler. Lines: 24. Review: AST and structural risk scan.

Top-level definitions: NcLogicalAddress, NcVirtualAddress.

Direct imports: dataclasses, lava.magma.compiler.builders.interfaces.

## src/lava/magma/compiler/subcompilers/channel_builders_factory.py

Chunk: 04 Compiler. Lines: 295. Review: AST and structural risk scan.

Top-level definitions: ChannelBuildersFactory.

Direct imports: typing, lava.magma.compiler.builders.channel_builder, lava.magma.compiler.channel_map, lava.magma.compiler.channels.interfaces, lava.magma.compiler.utils, lava.magma.compiler.var_model, lava.magma.core.model.model, lava.magma.core.model.py.model, lava.magma.core.process.ports.ports, lava.magma.core.process.ports.ports, lava.magma.core.process.ports.ports, lava.magma.core.model.py.ports.

## src/lava/magma/compiler/subcompilers/channel_map_updater.py

Chunk: 04 Compiler. Lines: 62. Review: AST and structural risk scan.

Top-level definitions: ChannelMapUpdater.

Direct imports: typing, lava.magma.compiler.channel_map, lava.magma.core.process.ports.ports.

## src/lava/magma/compiler/subcompilers/constants.py

Chunk: 04 Compiler. Lines: 24. Review: AST and structural risk scan.

Top-level definitions: EMBEDDED_ALLOCATION_ORDER.

Direct imports: enum.

## src/lava/magma/compiler/subcompilers/exceptions.py

Chunk: 04 Compiler. Lines: 22. Review: AST and structural risk scan.

Top-level definitions: ResourceMismatchError.

Direct imports: typing, lava.magma.core.process.process, lava.magma.core.resources.

## src/lava/magma/compiler/subcompilers/interfaces.py

Chunk: 04 Compiler. Lines: 59. Review: AST and structural risk scan.

Top-level definitions: AbstractSubCompiler, SubCompiler.

Direct imports: typing, abc, lava.magma.compiler.builders.interfaces, lava.magma.compiler.channel_map, lava.magma.compiler.compiler_graphs, lava.magma.core.process.process.

## src/lava/magma/compiler/subcompilers/py/pyproc_compiler.py

Chunk: 04 Compiler. Lines: 295. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: _Offset, Offset, PyProcCompiler.

Direct imports: typing, numpy, lava.magma.compiler.builders.py_builder, lava.magma.compiler.builders.interfaces, lava.magma.compiler.channel_map, lava.magma.compiler.compiler_graphs, lava.magma.compiler.subcompilers.channel_builders_factory, lava.magma.compiler.subcompilers.channel_map_updater, lava.magma.compiler.subcompilers.interfaces, lava.magma.compiler.utils, lava.magma.compiler.var_model, lava.magma.core.model.py.model, lava.magma.core.model.py.ports, lava.magma.core.process.ports.ports, lava.magma.core.process.ports.connection_config, lava.magma.core.process.process, lava.magma.compiler.subcompilers.constants.

## src/lava/magma/compiler/utils.py

Chunk: 04 Compiler. Lines: 156. Review: AST and structural risk scan.

Top-level definitions: VarInitializer, PortInitializer, VarPortInitializer, LoihiVarInitializer, LoihiPortInitializer, LoihiConnectedPortType, LoihiConnectedPortEncodingType, LoihiIOPortInitializer, LoihiInPortInitializer, LoihiCInPortInitializer, LoihiPyInPortInitializer, LoihiOutPortInitializer, LoihiVarPortInitializer.

Direct imports: functools, typing, dataclasses, enum, lava.magma.compiler.mappable_interface, lava.magma.compiler.subcompilers.address, lava.magma.compiler.var_model, lava.magma.core.model.spike_type, lava.magma.core.process.ports.connection_config.

## src/lava/magma/compiler/var_model.py

Chunk: 04 Compiler. Lines: 282. Review: AST and structural risk scan.

Top-level definitions: LoihiAddress, LoihiNeuronAddress, LoihiSynapseAddress, LoihiInAxonAddress, AbstractVarModel, PyVarModel, LoihiVarModel, LoihiNeuronVarModel, LoihiSynapseVarModel, CVarModel, NcVarModel, Region, ConvInVarModel, ConvNeuronVarModel, ByteEncoder, CoreEncoder, ChipEncoder, AxonEncoder, TimeCompare, DecodeConfig, SpikeEncoder, NcSpikeIOVarModel, NcConvSpikeInVarModel.

Direct imports: __future__, typing, abc, dataclasses, lava.magma.compiler.mappable_interface, lava.magma.compiler.subcompilers.address, lava.magma.core.process.ports.connection_config, lava.magma.core.process.variable.

## src/lava/magma/core/callback_fx.py

Chunk: 03 Core API. Lines: 86. Review: AST and structural risk scan.

Top-level definitions: CallbackFx, NxSdkCallbackFx, IterableCallBack.

Direct imports: numpy, abc, typing.

## src/lava/magma/core/decorator.py

Chunk: 03 Core API. Lines: 168. Review: AST and structural risk scan.

Top-level definitions: implements, requires, tag.

Direct imports: typing, lava.magma.core.model.model, lava.magma.core.process.process, lava.magma.core.resources, lava.magma.core.sync.protocol.

## src/lava/magma/core/learning/constants.py

Chunk: 07 Learning. Lines: 96. Review: AST and structural risk scan.

Top-level definitions: GradedSpikeCfg.

Direct imports: enum, lava.magma.core.learning.string_symbols.

## src/lava/magma/core/learning/learning_rule.py

Chunk: 07 Learning. Lines: 751. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: LoihiLearningRule, Loihi2FLearningRule, Loihi3FLearningRule.

Direct imports: typing, numpy, re, lava.magma.core.learning.string_symbols, lava.magma.core.learning.symbolic_equation, lava.magma.core.learning.product_series.

## src/lava/magma/core/learning/learning_rule_applier.py

Chunk: 07 Learning. Lines: 328. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: AbstractLearningRuleApplier, LearningRuleApplierFloat, LearningRuleApplierBitApprox.

Direct imports: numpy, abc, asteval, lava.magma.core.learning.product_series, lava.magma.core.learning.constants.

## src/lava/magma/core/learning/product_series.py

Chunk: 07 Learning. Lines: 750. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: Factor, Product, ProductSeries.

Direct imports: typing, lava.magma.core.learning.string_symbols, lava.magma.core.learning.symbolic_equation.

## src/lava/magma/core/learning/random.py

Chunk: 07 Learning. Lines: 139. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: AbstractRandomGenerator, TraceRandom, ConnVarRandom.

Direct imports: typing, numpy, abc, lava.magma.core.learning.constants.

## src/lava/magma/core/learning/string_symbols.py

Chunk: 07 Learning. Lines: 44. Review: AST and structural risk scan.

Top-level definitions: none.

Direct imports: none.

## src/lava/magma/core/learning/symbolic_equation.py

Chunk: 07 Learning. Lines: 885. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: Symbol, SymbolList, Operator, Addition, Subtraction, Multiplication, FactorSym, Dependency, X0, Y0, Uk, Variable, Expression, BracketExpression, SgnExpression, Literal, SymbolicEquation.

Direct imports: re, abc, typing, ast, lava.magma.core.learning.string_symbols.

## src/lava/magma/core/learning/utils.py

Chunk: 07 Learning. Lines: 78. Review: AST and structural risk scan.

Top-level definitions: stochastic_round, apply_mask, float_to_literal.

Direct imports: numpy, typing.

## src/lava/magma/core/model/interfaces.py

Chunk: 03 Core API. Lines: 39. Review: AST and structural risk scan.

Top-level definitions: AbstractPortImplementation.

Direct imports: typing, abc, lava.magma.compiler.channels.interfaces.

## src/lava/magma/core/model/model.py

Chunk: 03 Core API. Lines: 107. Review: AST and structural risk scan.

Top-level definitions: AbstractProcessModel.

Direct imports: __future__, typing, logging, abc, lava.magma.core.resources, lava.magma.core.sync.protocol.

## src/lava/magma/core/model/py/connection.py

Chunk: 03 Core API. Lines: 1566. Review: AST and structural risk scan.

Top-level definitions: AbstractLearningConnection, PyLearningConnection, LearningConnectionModelBitApproximate, LearningConnectionModelFloat.

Direct imports: abc, lava.utils.sparse, numpy, typing, scipy.sparse, lava.magma.core.learning.learning_rule, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.learning.constants, lava.magma.core.learning.random, lava.magma.core.learning.product_series, lava.magma.core.learning.learning_rule_applier, lava.magma.core.learning.string_symbols, lava.utils.weightutils, lava.magma.core.learning.utils, logging.

## src/lava/magma/core/model/py/model.py

Chunk: 03 Core API. Lines: 777. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: AbstractPyProcessModel, PyLoihiProcessModel, PyAsyncProcessModel, _get_attr_dict, _get_callable_dict, PyLoihiModelToPyAsyncModel.

Direct imports: typing, abc, logging, lava.utils.sparse, numpy, scipy.sparse, platform, lava.magma.compiler.channels.pypychannel, lava.magma.core.model.model, lava.magma.core.model.py.ports, lava.magma.runtime.mgmt_token_enums, lava.magma.core.sync.protocols.async_protocol.

## src/lava/magma/core/model/py/neuron.py

Chunk: 03 Core API. Lines: 105. Review: AST and structural risk scan.

Top-level definitions: LearningNeuronModel, LearningNeuronModelFixed, LearningNeuronModelFloat.

Direct imports: lava.magma.core.model.py.model, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, numpy.

## src/lava/magma/core/model/py/ports.py

Chunk: 03 Core API. Lines: 1015. Review: AST and structural risk scan.

Top-level definitions: AbstractPyPort, AbstractPyIOPort, AbstractTransformer, IdentityTransformer, VirtualPortTransformer, PyInPort, PyInPortVectorDense, PyInPortVectorSparse, PyInPortScalarDense, PyInPortScalarSparse, PyOutPort, PyOutPortVectorDense, PyOutPortVectorSparse, PyOutPortScalarDense, PyOutPortScalarSparse, VarPortCmd, PyRefPort, PyRefPortVectorDense, PyRefPortVectorSparse, PyRefPortScalarDense, PyRefPortScalarSparse, PyVarPort, PyVarPortVectorDense, PyVarPortVectorSparse, PyVarPortScalarDense, PyVarPortScalarSparse, RefVarTypeMapping.

Direct imports: functools, typing, abc, numpy, lava.magma.compiler.channels.interfaces, lava.magma.compiler.channels.pypychannel, lava.magma.core.model.interfaces, lava.magma.core.model.model, lava.magma.runtime.mgmt_token_enums.

## src/lava/magma/core/model/py/type.py

Chunk: 03 Core API. Lines: 16. Review: AST and structural risk scan.

Top-level definitions: LavaPyType.

Direct imports: typing, dataclasses, lava.magma.core.model.py.ports.

## src/lava/magma/core/model/spike_type.py

Chunk: 03 Core API. Lines: 16. Review: AST and structural risk scan.

Top-level definitions: SpikeType.

Direct imports: enum.

## src/lava/magma/core/model/sub/model.py

Chunk: 03 Core API. Lines: 71. Review: AST and structural risk scan.

Top-level definitions: AbstractSubProcessModel.

Direct imports: typing, abc, collections, lava.magma.core.model.model, lava.magma.core.process.process, dataclasses.

## src/lava/magma/core/process/connection.py

Chunk: 03 Core API. Lines: 108. Review: AST and structural risk scan.

Top-level definitions: LearningConnectionProcess.

Direct imports: typing, lava.magma.core.learning.learning_rule, lava.magma.core.process.ports.ports, lava.magma.core.process.process, lava.magma.core.process.variable.

## src/lava/magma/core/process/interfaces.py

Chunk: 03 Core API. Lines: 79. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: AbstractProcessMember, IdGeneratorSingleton.

Direct imports: __future__, typing, abc, math.

## src/lava/magma/core/process/message_interface_enum.py

Chunk: 03 Core API. Lines: 9. Review: AST and structural risk scan.

Top-level definitions: ActorType.

Direct imports: enum.

## src/lava/magma/core/process/neuron.py

Chunk: 03 Core API. Lines: 59. Review: AST and structural risk scan.

Top-level definitions: LearningNeuronProcess.

Direct imports: typing, lava.magma.core.process.ports.ports, lava.magma.core.learning.learning_rule, lava.magma.core.process.variable.

## src/lava/magma/core/process/ports/connection_config.py

Chunk: 03 Core API. Lines: 60. Review: AST and structural risk scan.

Top-level definitions: SpikeIOInterface, SpikeIOPort, SpikeIOMode, ConnectionConfig.

Direct imports: dataclasses, enum, typing.

## src/lava/magma/core/process/ports/exceptions.py

Chunk: 03 Core API. Lines: 90. Review: AST and structural risk scan.

Top-level definitions: ReshapeError, DuplicateConnectionError, ConcatShapeError, ConcatIndexError, TransposeShapeError, TransposeIndexError, VarNotSharableError.

Direct imports: typing.

## src/lava/magma/core/process/ports/ports.py

Chunk: 03 Core API. Lines: 1023. Review: AST and structural risk scan.

Top-level definitions: to_list, is_disjoint, create_port_id, AbstractPort, AbstractIOPort, AbstractRVPort, AbstractSrcPort, AbstractDstPort, OutPort, InPort, RefPort, VarPort, ImplicitVarPort, AbstractVirtualPort, ReshapePort, ConcatPort, TransposePort.

Direct imports: __future__, typing, abc, math, numpy, functools, lava.magma.core.process.interfaces, lava.magma.core.process.ports.exceptions, lava.magma.core.process.ports.connection_config, lava.magma.core.process.ports.reduce_ops, lava.magma.core.process.variable.

## src/lava/magma/core/process/ports/reduce_ops.py

Chunk: 03 Core API. Lines: 15. Review: AST and structural risk scan.

Top-level definitions: AbstractReduceOp, ReduceSum.

Direct imports: abc.

## src/lava/magma/core/process/process.py

Chunk: 03 Core API. Lines: 653. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: ProcessPostInitCaller, AbstractProcess, ProcessParameters, LogConfig, ProcessServer, Collection.

Direct imports: __future__, logging, typing, _collections, dataclasses, lava.magma.compiler.executable, lava.magma.core.process.interfaces, lava.magma.core.process.message_interface_enum, lava.magma.core.process.ports.ports, lava.magma.core.process.variable, lava.magma.core.run_conditions, lava.magma.core.run_configs, lava.magma.runtime.runtime.

## src/lava/magma/core/process/variable.py

Chunk: 03 Core API. Lines: 231. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: Var, VarServer.

Direct imports: typing, numpy, scipy.sparse, lava.utils.sparse, lava.magma.core.process.interfaces.

## src/lava/magma/core/resources.py

Chunk: 03 Core API. Lines: 132. Review: AST and structural risk scan.

Top-level definitions: AbstractResource, AbstractComputeResource, CPU, HostCPU, GPU, ECPU, LMT, PB, NeuroCore, Loihi1NeuroCore, Loihi2NeuroCore, AbstractPeripheralResource, DVS, HardDrive, HeadNodeHardDrive, AbstractNode, GenericNode, HeadNode, Loihi1System, KapohoBay, Nahuku, Pohoiki, Loihi2System, OheoGulch, KapohoPoint, Unalaska.

Direct imports: abc.

## src/lava/magma/core/run_conditions.py

Chunk: 03 Core API. Lines: 51. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: AbstractRunCondition, RunSteps, RunContinuous.

Direct imports: abc.

## src/lava/magma/core/run_configs.py

Chunk: 03 Core API. Lines: 479. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: RunConfig, AbstractLoihiRunCfg, AbstractLoihiHWRunCfg, AbstractLoihiSimRunCfg, Loihi1SimCfg, Loihi1HwCfg, Loihi2SimCfg, Loihi2HwCfg.

Direct imports: __future__, logging, typing, abc, itertools, lava.magma.core.resources, lava.magma.core.model.py.model, lava.magma.core.callback_fx, lava.magma.core.sync.domain, lava.magma.compiler.subcompilers.constants.

## src/lava/magma/core/sync/domain.py

Chunk: 03 Core API. Lines: 51. Review: AST and structural risk scan.

Top-level definitions: SyncDomain.

Direct imports: typing, lava.magma.core.sync.protocol.

## src/lava/magma/core/sync/protocol.py

Chunk: 03 Core API. Lines: 33. Review: AST and structural risk scan.

Top-level definitions: AbstractSyncProtocol.

Direct imports: abc.

## src/lava/magma/core/sync/protocols/async_protocol.py

Chunk: 03 Core API. Lines: 47. Review: AST and structural risk scan.

Top-level definitions: AsyncProtocol.

Direct imports: dataclasses, lava.magma.core.resources, lava.magma.core.sync.protocol, lava.magma.runtime.runtime_services.runtime_service.

## src/lava/magma/core/sync/protocols/loihi_protocol.py

Chunk: 03 Core API. Lines: 134. Review: AST and structural risk scan.

Top-level definitions: Phase, LoihiProtocol.

Direct imports: collections, dataclasses, lava.magma.core.resources, lava.magma.core.sync.protocol, lava.magma.runtime.mgmt_token_enums, lava.magma.runtime.runtime_services.runtime_service.

## src/lava/magma/runtime/message_infrastructure/factory.py

Chunk: 05 Runtime. Lines: 20. Review: AST and structural risk scan.

Top-level definitions: MessageInfrastructureFactory.

Direct imports: lava.magma.core.process.message_interface_enum, lava.magma.runtime.message_infrastructure.multiprocessing.

## src/lava/magma/runtime/message_infrastructure/message_infrastructure_interface.py

Chunk: 05 Runtime. Lines: 45. Review: AST and structural risk scan.

Top-level definitions: MessageInfrastructureInterface.

Direct imports: typing, abc, lava.magma.compiler.channels.interfaces, lava.magma.core.sync.domain.

## src/lava/magma/runtime/message_infrastructure/multiprocessing.py

Chunk: 05 Runtime. Lines: 148. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: SystemProcess, MultiProcessing.

Direct imports: typing, multiprocessing, os, traceback, lava.magma.compiler.channels.interfaces, lava.magma.compiler.channels.pypychannel, lava.magma.runtime.message_infrastructure.shared_memory_manager, lava.magma.core.sync.domain, lava.magma.runtime.message_infrastructure.message_infrastructure_interface, platform.

## src/lava/magma/runtime/message_infrastructure/nx.py

Chunk: 05 Runtime. Lines: 40. Review: AST and structural risk scan.

Top-level definitions: NxBoardMsgInterface.

Direct imports: typing, lava.magma.compiler.channels.interfaces, lava.magma.core.sync.domain, lava.magma.runtime.message_infrastructure.message_infrastructure_interface.

## src/lava/magma/runtime/message_infrastructure/shared_memory_manager.py

Chunk: 05 Runtime. Lines: 31. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: SharedMemoryManager.

Direct imports: multiprocessing.managers, multiprocessing.shared_memory, typing.

## src/lava/magma/runtime/mgmt_token_enums.py

Chunk: 05 Runtime. Lines: 75. Review: AST and structural risk scan.

Top-level definitions: enum_to_np, enum_equal, MGMT_COMMAND, MGMT_RESPONSE.

Direct imports: typing, numpy.

## src/lava/magma/runtime/runtime.py

Chunk: 05 Runtime. Lines: 627. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: target_fn, Runtime.

Direct imports: __future__, logging, sys, traceback, typing, numpy, scipy.sparse, lava.magma.compiler.var_model, lava.magma.core.process.message_interface_enum, lava.magma.runtime.message_infrastructure.factory, lava.magma.runtime.message_infrastructure.message_infrastructure_interface, lava.magma.runtime.mgmt_token_enums, lava.magma.runtime.runtime_services.runtime_service, lava.magma.compiler.channels.pypychannel, lava.magma.compiler.builders.channel_builder, lava.magma.compiler.builders.interfaces, lava.magma.compiler.builders.py_builder, lava.magma.compiler.builders.runtimeservice_builder, lava.magma.compiler.channels.interfaces, lava.magma.compiler.executable, lava.magma.compiler.node, lava.magma.core.process.ports.ports, lava.magma.core.run_conditions, lava.magma.compiler.channels.watchdog, multiprocessing.

## src/lava/magma/runtime/runtime_services/channel_broker/channel_broker.py

Chunk: 05 Runtime. Lines: 231. Review: AST and structural risk scan.

Top-level definitions: AbstractChannelBroker, generate_channel_name, ChannelBroker.

Direct imports: threading, abc, logging, numpy, typing, lava.magma.compiler.channels.interfaces, lava.magma.compiler.channels.pypychannel, lava.magma.runtime.message_infrastructure.shared_memory_manager.

## src/lava/magma/runtime/runtime_services/enums.py

Chunk: 05 Runtime. Lines: 45. Review: AST and structural risk scan.

Top-level definitions: LoihiVersion, LoihiPhase, NxSdkPhase.

Direct imports: enum, lava.magma.runtime.mgmt_token_enums.

## src/lava/magma/runtime/runtime_services/interfaces.py

Chunk: 05 Runtime. Lines: 42. Review: AST and structural risk scan.

Top-level definitions: AbstractRuntimeService.

Direct imports: typing, abc, lava.magma.compiler.channels.pypychannel, lava.magma.core.sync.protocol.

## src/lava/magma/runtime/runtime_services/runtime_service.py

Chunk: 05 Runtime. Lines: 525. Review: AST and structural risk scan.

Top-level definitions: PyRuntimeService, LoihiPyRuntimeService, AsyncPyRuntimeService.

Direct imports: logging, typing, abc, numpy, lava.magma.compiler.channels.pypychannel, lava.magma.core.sync.protocol, lava.magma.runtime.mgmt_token_enums, lava.magma.runtime.runtime_services.enums, lava.magma.runtime.runtime_services.interfaces.

## src/lava/networks/gradedvecnetwork.py

Chunk: 09 IO and networks. Lines: 324. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: InputVec, OutputVec, LIFVec, GradedVec, ProductVec, GradedDense, GradedSparse, NormalizeNet.

Direct imports: numpy, typing, lava.proc.graded.process, lava.proc.graded.process, lava.proc.sparse.process, lava.proc.dense.process, lava.proc.prodneuron.process, lava.proc.graded.process, lava.proc.lif.process, lava.proc.io, network.

## src/lava/networks/network.py

Chunk: 09 IO and networks. Lines: 154. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: NetworkList, Network, AlgebraicVector, AlgebraicMatrix.

Direct imports: numpy, typing, scipy.sparse, lava.magma.core.process.ports.ports, lava.magma.core.process.process.

## src/lava/networks/resfire.py

Chunk: 09 IO and networks. Lines: 45. Review: AST and structural risk scan.

Top-level definitions: ResFireVec.

Direct imports: numpy, network, lava.proc.resfire.process.

## src/lava/proc/atrlif/models.py

Chunk: 08 Process library. Lines: 267. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: PyATRLIFModelFloat, PyATRLIFModelFixed.

Direct imports: numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.atrlif.process.

## src/lava/proc/atrlif/process.py

Chunk: 08 Process library. Lines: 138. Review: AST and structural risk scan.

Top-level definitions: ATRLIF.

Direct imports: numpy, typing, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/bit_check/models.py

Chunk: 08 Process library. Lines: 117. Review: AST and structural risk scan.

Top-level definitions: AbstractPyBitCheckModel, AbstractBitCheckModel, LoihiBitCheckModel.

Direct imports: numpy, typing, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.bit_check.process.

## src/lava/proc/bit_check/process.py

Chunk: 08 Process library. Lines: 93. Review: AST and structural risk scan.

Top-level definitions: BitCheck.

Direct imports: typing, lava.magma.core.process.process, lava.magma.core.process.ports.ports, lava.magma.core.process.variable.

## src/lava/proc/clp/id_broadcast/models.py

Chunk: 08 Process library. Lines: 32. Review: AST and structural risk scan.

Top-level definitions: IdBroadcastModel.

Direct imports: numpy, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.sync.protocols.loihi_protocol, lava.proc.clp.id_broadcast.process.

## src/lava/proc/clp/id_broadcast/process.py

Chunk: 08 Process library. Lines: 34. Review: AST and structural risk scan.

Top-level definitions: IdBroadcast.

Direct imports: typing, lava.magma.core.process.ports.ports, lava.magma.core.process.variable, lava.magma.core.process.process.

## src/lava/proc/clp/novelty_detector/models.py

Chunk: 08 Process library. Lines: 71. Review: AST and structural risk scan.

Top-level definitions: PyNoveltyDetectorModel.

Direct imports: numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.clp.novelty_detector.process.

## src/lava/proc/clp/novelty_detector/process.py

Chunk: 08 Process library. Lines: 44. Review: AST and structural risk scan.

Top-level definitions: NoveltyDetector.

Direct imports: lava.magma.core.process.ports.ports, lava.magma.core.process.process, lava.magma.core.process.variable.

## src/lava/proc/clp/nsm/models.py

Chunk: 08 Process library. Lines: 149. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: PyReadoutModel, PyAllocatorModel.

Direct imports: numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.clp.nsm.process, lava.proc.clp.nsm.process.

## src/lava/proc/clp/nsm/process.py

Chunk: 08 Process library. Lines: 88. Review: AST and structural risk scan.

Top-level definitions: Readout, Allocator.

Direct imports: typing, numpy, lava.magma.core.process.ports.ports, lava.magma.core.process.process, lava.magma.core.process.variable.

## src/lava/proc/clp/prototype_lif/models.py

Chunk: 08 Process library. Lines: 117. Review: AST and structural risk scan.

Top-level definitions: PrototypeLIFBitAcc.

Direct imports: numpy, lava.magma.core.model.py.neuron, lava.proc.clp.prototype_lif.process, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.type, lava.magma.core.model.py.ports, lava.magma.core.resources, lava.magma.core.decorator, lava.proc.lif.models.

## src/lava/proc/clp/prototype_lif/process.py

Chunk: 08 Process library. Lines: 52. Review: AST and structural risk scan.

Top-level definitions: PrototypeLIF.

Direct imports: numpy, typing, lava.proc.lif.process, lava.magma.core.learning.learning_rule, lava.magma.core.process.process, lava.magma.core.process.ports.ports.

## src/lava/proc/conv/models.py

Chunk: 08 Process library. Lines: 79. Review: AST and structural risk scan.

Top-level definitions: AbstractPyConvModel, PyConvModelFloat, PyConvModelFixed.

Direct imports: numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.conv.process, lava.proc.conv.

## src/lava/proc/conv/process.py

Chunk: 08 Process library. Lines: 145. Review: AST and structural risk scan.

Top-level definitions: Conv.

Direct imports: typing, numpy, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports, lava.proc.conv.

## src/lava/proc/conv/utils.py

Chunk: 08 Process library. Lines: 491. Review: AST and structural risk scan.

Top-level definitions: TensorOrder, make_tuple, signed_clamp, output_shape, conv, conv_scipy, conv_to_sparse.

Direct imports: typing, numpy, scipy, enum.

## src/lava/proc/conv_in_time/models.py

Chunk: 08 Process library. Lines: 99. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: AbstractPyConvInTimeModel, PyConvInTimeFloat, PyConvInTimeFixed.

Direct imports: numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.conv_in_time.process, lava.proc.conv.

## src/lava/proc/conv_in_time/process.py

Chunk: 08 Process library. Lines: 86. Review: AST and structural risk scan.

Top-level definitions: ConvInTime.

Direct imports: numpy, typing, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/dense/models.py

Chunk: 08 Process library. Lines: 352. Review: AST and structural risk scan.

Top-level definitions: AbstractPyDenseModelFloat, PyDenseModelFloat, AbstractPyDenseModelBitAcc, PyDenseModelBitAcc, PyLearningDenseModelFloat, PyLearningDenseModelBitApproximate, AbstractPyDelayDenseModel, PyDelayDenseModelFloat, PyDelayDenseModelBitAcc.

Direct imports: numpy, lava.magma.core.model.py.connection, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.dense.process, lava.utils.weightutils.

## src/lava/proc/dense/process.py

Chunk: 08 Process library. Lines: 277. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: Dense, LearningDense, DelayDense.

Direct imports: numpy, typing, lava.magma.core.learning.constants, lava.magma.core.learning.learning_rule, lava.magma.core.process.connection, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/graded/models.py

Chunk: 08 Process library. Lines: 254. Review: AST and structural risk scan.

Top-level definitions: AbstractGradedVecModel, PyGradedVecModelFixed, AbstractGradedReluVecModel, PyGradedReluVecModelFixed, NormVecDelayModel, InvSqrtModelFloat, make_fpinv_table, clz, inv_sqrt, InvSqrtModelFP.

Direct imports: numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.graded.process.

## src/lava/proc/graded/process.py

Chunk: 08 Process library. Lines: 197. Review: AST and structural risk scan.

Top-level definitions: loihi2round, GradedVec, GradedReluVec, NormVecDelay, InvSqrt.

Direct imports: numpy, typing, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/io/__init__.py

Chunk: 09 IO and networks. Lines: 8. Review: AST and structural risk scan.

Top-level definitions: none.

Direct imports: ..

## src/lava/proc/io/dataloader.py

Chunk: 09 IO and networks. Lines: 215. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: AbstractDataloader, AbstractPyDataloaderModel, StateDataloader, AbstractPyStateDataloaderModel, PyStateModelFixed, PyStateModelFloat, SpikeDataloader, AbstractPySpikeDataloaderModel, PySpikeModelFixed, PySpikeModelFloat.

Direct imports: typing, numpy, lava.magma.core.process.process, lava.magma.core.process.ports.ports, lava.magma.core.process.variable, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model.

## src/lava/proc/io/encoder.py

Chunk: 09 IO and networks. Lines: 295. Review: AST and structural risk scan.

Top-level definitions: Compression, DeltaEncoder, AbstractPyDeltaEncoderModel, PyDeltaEncoderModelDense, PyDeltaEncoderModelSparse.

Direct imports: typing, numpy, enum, lava.magma.core.process.process, lava.magma.core.process.ports.ports, lava.magma.core.process.variable, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model.

## src/lava/proc/io/extractor.py

Chunk: 09 IO and networks. Lines: 277. Review: AST and structural risk scan.

Top-level definitions: Extractor, PyLoihiExtractorModel, PyLoihiExtractorModelAsync, VarWire, PyLoihiVarWireModel.

Direct imports: numpy, typing, lava.magma.core.process.process, lava.magma.core.process.ports.ports, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.magma.core.model.py.model, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.sync.protocols.async_protocol, lava.magma.core.model.py.type, lava.magma.core.model.py.ports, lava.magma.compiler.channels.pypychannel, lava.magma.runtime.message_infrastructure.multiprocessing, lava.proc.io.

## src/lava/proc/io/injector.py

Chunk: 09 IO and networks. Lines: 171. Review: AST and structural risk scan.

Top-level definitions: Injector, PyLoihiInjectorModel, PyLoihiInjectorModelAsync.

Direct imports: numpy, typing, lava.magma.core.process.process, lava.magma.core.process.ports.ports, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.magma.core.model.py.model, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.sync.protocols.async_protocol, lava.magma.core.model.py.type, lava.magma.core.model.py.ports, lava.proc.io.

## src/lava/proc/io/reset.py

Chunk: 09 IO and networks. Lines: 81. Review: AST and structural risk scan.

Top-level definitions: Reset, AbstractPyReset, PyResetFixed, PyResetFloat.

Direct imports: numpy, typing, lava.magma.core.process.variable, lava.magma.core.process.ports.ports, lava.magma.core.process.process, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.type, lava.magma.core.model.py.ports.

## src/lava/proc/io/sink.py

Chunk: 09 IO and networks. Lines: 148. Review: AST and structural risk scan.

Top-level definitions: RingBuffer, AbstractPyReceiveModel, PyReceiveModelFloat, PyReceiveModelFixed, Read, AbstractPyRead, PyReadFixed, PyReadFloat.

Direct imports: numpy, typing, lava.magma.core.process.variable, lava.magma.core.process.process, lava.magma.core.process.ports.ports, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.type, lava.magma.core.model.py.ports.

## src/lava/proc/io/source.py

Chunk: 09 IO and networks. Lines: 61. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: RingBuffer, AbstractPyRingBuffer, PySendModelFloat, PySendModelFixed.

Direct imports: numpy, lava.magma.core.process.variable, lava.magma.core.process.process, lava.magma.core.process.ports.ports, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.type, lava.magma.core.model.py.ports.

## src/lava/proc/io/utils.py

Chunk: 09 IO and networks. Lines: 282. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: SendFull, send_full_blocking, send_full_non_blocking_drop, ReceiveEmpty, receive_empty_blocking, receive_empty_non_blocking_zeros, ReceiveNotEmpty, receive_not_empty_fifo, receive_not_empty_accumulate, ChannelConfig, validate_shape, validate_buffer_size, validate_channel_config.

Direct imports: enum, dataclasses, typing, numpy, warnings, lava.magma.compiler.channels.pypychannel.

## src/lava/proc/learning_rules/r_stdp_learning_rule.py

Chunk: 08 Process library. Lines: 84. Review: AST and structural risk scan.

Top-level definitions: RewardModulatedSTDP.

Direct imports: lava.magma.core.learning.learning_rule, lava.magma.core.learning.utils.

## src/lava/proc/learning_rules/stdp_learning_rule.py

Chunk: 08 Process library. Lines: 68. Review: AST and structural risk scan.

Top-level definitions: STDPLoihi.

Direct imports: lava.magma.core.learning.learning_rule, lava.magma.core.learning.utils.

## src/lava/proc/lif/models.py

Chunk: 08 Process library. Lines: 561. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: AbstractPyLifModelFloat, AbstractPyLifModelFixed, PyLifModelFloat, PyLifModelBitAcc, PyTernLifModelFloat, PyTernLifModelFixed, PyLifResetModelFloat, PyLifResetModelBitAcc, PyLifRefractoryModelFloat, PyLearningLIFModelFixed, PyLearningLifModelFloat.

Direct imports: lava.magma.core.model.py.neuron, numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.lif.process.

## src/lava/proc/lif/process.py

Chunk: 08 Process library. Lines: 418. Review: AST and structural risk scan.

Top-level definitions: AbstractLIF, LIF, LearningLIF, TernaryLIF, LIFReset, LIFRefractory.

Direct imports: numpy, typing, lava.magma.core.learning.learning_rule, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports, lava.magma.core.process.neuron.

## src/lava/proc/monitor/models.py

Chunk: 08 Process library. Lines: 61. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: PyMonitorModel.

Direct imports: numpy, lava.magma.core.model.py.ports, lava.proc.monitor.process, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.model, lava.magma.core.model.py.type, lava.magma.core.decorator, lava.magma.core.resources.

## src/lava/proc/monitor/process.py

Chunk: 08 Process library. Lines: 268. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: Monitor.

Direct imports: lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/prodneuron/models.py

Chunk: 08 Process library. Lines: 38. Review: AST and structural risk scan.

Top-level definitions: PyProdNeuronModelFixed.

Direct imports: numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.prodneuron.process.

## src/lava/proc/prodneuron/process.py

Chunk: 08 Process library. Lines: 50. Review: AST and structural risk scan.

Top-level definitions: ProdNeuron.

Direct imports: numpy, typing, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/receiver/models.py

Chunk: 08 Process library. Lines: 30. Review: AST and structural risk scan.

Top-level definitions: ReceiverModel.

Direct imports: numpy, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.sync.protocols.loihi_protocol, lava.proc.receiver.process.

## src/lava/proc/receiver/process.py

Chunk: 08 Process library. Lines: 59. Review: AST and structural risk scan.

Top-level definitions: Receiver, Receiver32Bit.

Direct imports: typing, lava.magma.core.process.ports.ports, lava.magma.core.process.process, lava.magma.core.process.variable.

## src/lava/proc/resfire/models.py

Chunk: 08 Process library. Lines: 49. Review: AST and structural risk scan.

Top-level definitions: PyRFZeroModelFixed.

Direct imports: numpy, lava.proc.resfire.process, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model.

## src/lava/proc/resfire/process.py

Chunk: 08 Process library. Lines: 65. Review: AST and structural risk scan.

Top-level definitions: RFZero.

Direct imports: numpy, typing, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/rf/models.py

Chunk: 08 Process library. Lines: 145. Review: AST and structural risk scan.

Top-level definitions: AbstractPyRFModelFloat, PyRFModelFloat, AbstractPyRFModelFixed, PyRFModelFixed.

Direct imports: numpy, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.rf.process.

## src/lava/proc/rf/process.py

Chunk: 08 Process library. Lines: 88. Review: AST and structural risk scan.

Top-level definitions: RF.

Direct imports: typing, numpy, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/rf_iz/models.py

Chunk: 08 Process library. Lines: 58. Review: AST and structural risk scan.

Top-level definitions: PyRF_IZModelFloat, PyRF_IZModelFixed.

Direct imports: lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.resources, numpy, lava.magma.core.decorator, lava.proc.rf_iz.process, lava.proc.rf.models.

## src/lava/proc/rf_iz/process.py

Chunk: 08 Process library. Lines: 9. Review: AST and structural risk scan.

Top-level definitions: RF_IZ.

Direct imports: lava.proc.rf.process.

## src/lava/proc/s4d/models.py

Chunk: 08 Process library. Lines: 234. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: S4dModel, AbstractSigmaS4dDeltaModel, PySigmaS4dDeltaModelFloat, SubDenseLayerModel.

Direct imports: numpy, typing, lava.proc.sdn.models, lava.magma.core.decorator, lava.magma.core.sync.protocols.loihi_protocol, lava.proc.s4d.process, lava.magma.core.resources, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.model.sub.model, lava.proc.sparse.process, lava.magma.core.model.py.model.

## src/lava/proc/s4d/process.py

Chunk: 08 Process library. Lines: 244. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: S4d, SigmaS4dDelta, SigmaS4dDeltaLayer.

Direct imports: typing, numpy, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports, lava.proc.sdn.process.

## src/lava/proc/sdn/models.py

Chunk: 08 Process library. Lines: 316. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: ReLU, AbstractSigmaModel, AbstractDeltaModel, AbstractSigmaDeltaModel, PySigmaModelFloat, PySigmaModelFixed, PyDeltaModelFloat, PyDeltaModelFixed, PySigmaDeltaModelFloat, PySigmaDeltaModelFixed, PySigmaDeltaModelFixedCorrected.

Direct imports: numpy, typing, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.sdn.process.

## src/lava/proc/sdn/process.py

Chunk: 08 Process library. Lines: 198. Review: AST and structural risk scan.

Top-level definitions: ActivationMode, Sigma, Delta, SigmaDelta.

Direct imports: typing, enum, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports.

## src/lava/proc/sparse/models.py

Chunk: 08 Process library. Lines: 372. Review: AST and structural risk scan.

Top-level definitions: AbstractPySparseModelFloat, PySparseModelFloat, AbstractPySparseModelBitAcc, PySparseModelBitAcc, PyLearningSparseModelFloat, PyLearningSparseModelBitApproximate, AbstractPyDelaySparseModel, PyDelaySparseModelFloat, PyDelaySparseModelBitAcc.

Direct imports: numpy, scipy.sparse, lava.magma.core.model.py.connection, lava.magma.core.sync.protocols.loihi_protocol, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.proc.sparse.process, lava.utils.weightutils.

## src/lava/proc/sparse/process.py

Chunk: 08 Process library. Lines: 294. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: Sparse, LearningSparse, DelaySparse.

Direct imports: numpy, scipy.sparse, typing, lava.magma.core.process.process, lava.magma.core.process.variable, lava.magma.core.process.ports.ports, lava.magma.core.process.connection, lava.magma.core.learning.constants, lava.magma.core.learning.learning_rule.

## src/lava/proc/spiker/models.py

Chunk: 08 Process library. Lines: 39. Review: AST and structural risk scan.

Top-level definitions: SpikerModel.

Direct imports: numpy, lava.magma.core.decorator, lava.magma.core.model.py.model, lava.magma.core.model.py.ports, lava.magma.core.model.py.type, lava.magma.core.resources, lava.magma.core.sync.protocols.loihi_protocol, lava.proc.spiker.process.

## src/lava/proc/spiker/process.py

Chunk: 08 Process library. Lines: 114. Review: AST and structural risk scan.

Top-level definitions: Spiker, Spiker32bit.

Direct imports: typing, numpy.typing, numpy, lava.magma.core.process.ports.ports, lava.magma.core.process.process, lava.magma.core.process.variable.

## src/lava/utils/dataloader/mnist.py

Chunk: 10 Utilities. Lines: 124. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: MnistDataset.

Direct imports: os, numpy.

## src/lava/utils/loihi.py

Chunk: 10 Utilities. Lines: 123. Review: AST and structural risk scan.

Top-level definitions: ChipGeneration, use_slurm_host, use_ethernet_host, is_installed.

Direct imports: os, typing, importlib.util, enum, lava.utils.

## src/lava/utils/plots.py

Chunk: 10 Utilities. Lines: 104. Review: AST and structural risk scan.

Top-level definitions: raster_plot.

Direct imports: typing, numpy, matplotlib.pyplot, matplotlib.figure.

## src/lava/utils/profiler.py

Chunk: 10 Utilities. Lines: 41. Review: AST and structural risk scan.

Top-level definitions: Profiler.

Direct imports: warnings, typing, lava.magma.core.run_configs.

## src/lava/utils/serialization.py

Chunk: 10 Utilities. Lines: 128. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: SerializationObject, save, load.

Direct imports: pickle, typing, os, lava.magma.core.process.process, lava.magma.compiler.executable.

## src/lava/utils/slurm.py

Chunk: 10 Utilities. Lines: 239. Review: AST and structural risk scan.

Top-level definitions: is_available, enable, disable, set_board, set_partition, partition, get_partitions, get_partition_info, PartitionInfo, get_boards, get_board_info, BoardInfo, try_run_command.

Direct imports: __future__, os, subprocess, typing, dataclasses.

## src/lava/utils/sparse.py

Chunk: 10 Utilities. Lines: 32. Review: AST and structural risk scan; focused review with cited finding.

Top-level definitions: find.

Direct imports: typing, scipy.sparse.

## src/lava/utils/system.py

Chunk: 10 Utilities. Lines: 78. Review: AST and structural risk scan.

Top-level definitions: deprecated, staticproperty, Loihi2.

Direct imports: os, typing.

## src/lava/utils/weightutils.py

Chunk: 10 Utilities. Lines: 295. Review: AST and structural risk scan.

Top-level definitions: SignMode, determine_sign_mode, OptimizedWeights, optimize_weight_bits, _validate_weights, _determine_weight_exp, _determine_num_weight_bits, truncate_weights, clip_weights.

Direct imports: numpy, scipy.sparse, typing, enum, dataclasses.
