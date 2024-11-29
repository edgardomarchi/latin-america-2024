
from gem5.components.boards.x86_board import X86Board
from gem5.components.processors.simple_switchable_processor import SimpleSwitchableProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy

from gem5.components.memory.multi_channel import DualChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA

from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.simulate.exit_event import ExitEvent

import m5



cache = PrivateL1CacheHierarchy(
    l1d_size="32kB",
    l1i_size="32kB"
    )

memory = DualChannelDDR4_2400(
    size="3GiB"
)

processor = SimpleSwitchableProcessor(
    starting_core_type=CPUTypes.KVM,
    switch_core_type=CPUTypes.TIMING,
    isa=ISA.X86,
    num_cores=2,
)

board = X86Board(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache,
)


board.set_workload(
    obtain_resource("npb-ep-a")
)

board.append_kernel_arg("interactive=true")

for proc in processor.start:
    proc.core.usePerf = False

def exit_event_handler():
    print("first exit event: Kernel booted")
    yield False
    print("second exit event: In after boot")
    yield False
    print("third exit event: After run script")
    yield True

def workbegin_handler():
    print("Done booting Linux")

    print("Dump the current stats")
    m5.stats.dump()

    print("Switching from KVM to TIMING CPU")
    processor.switch()

    simulator.set_max_ticks(1000_000_000)

    print("Resetting stats at the start of ROI!")
    m5.stats.reset()

    yield False


simulator = Simulator(
    board=board,txt
# Set up the exit event handlers
    on_exit_event= {
        ExitEvent.WORKBEGIN: workbegin_handler(),
    }
#
)

simulator.run()
