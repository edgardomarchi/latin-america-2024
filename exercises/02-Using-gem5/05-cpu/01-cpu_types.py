
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor
from m5.objects.BranchPredictor import (
    BiModeBP,
    MultiperspectivePerceptronTAGE64KB,
)
from m5.objects import RiscvO3CPU
from gem5.isas import ISA
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy

class BigO3(RiscvO3CPU):
    def __init__(self):
        super().__init__()
        self.fetchWidth = 8
        self.decodeWidth = 8
        self.renameWidth = 8
        self.dispatchWidth = 8
        self.issueWidth = 8
        self.wbWidth = 8
        self.commitWidth = 8

        self.numROBEntries = 256
        self.numPhysIntRegs = 512
        self.numPhysFloatRegs = 512

        self.branchPred = MultiperspectivePerceptronTAGE64KB()

class LittleO3(RiscvO3CPU):
    def __init__(self):
        super().__init__()
        self.fetchWidth = 2
        self.decodeWidth = 2
        self.renameWidth = 2
        self.dispatchWidth = 2
        self.issueWidth = 2
        self.wbWidth = 2
        self.commitWidth = 2

        self.numROBEntries = 30
        self.numPhysIntRegs = 40
        self.numPhysFloatRegs = 40

class BigCore(BaseCPUCore):
    def __init__(self):
        core = BigO3()
        super().__init__(core, ISA.RISCV)

class LittleCore(BaseCPUCore):
    def __init__(self):
        core = LittleO3()
        super().__init__(core, ISA.RISCV)

class BigProcessor(BaseCPUProcessor):
    def __init__(self):
        super().__init__(
            cores=[BigCore()]
        )

class LittleProcessor(BaseCPUProcessor):
    def __init__(self):
        super().__init__(
            cores=[LittleCore()]
        )

#processor = SimpleProcessor(
#    cpu_type=CPUTypes.ATOMIC,
#    isa=ISA.RISCV,
#    num_cores=1
#    )

processor = BigProcessor()

board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=SingleChannelDDR4_2400(),
    cache_hierarchy=PrivateL1CacheHierarchy(l1d_size="128KiB",
                                            l1i_size="128KiB")
    )

workload = obtain_resource("riscv-matrix-multiply-run")
board.set_workload(workload)
sim = Simulator(board=board)

sim.run()
