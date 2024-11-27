
from components.boards import HWX86Board
from components.processors import HWO3CPU
from components.cache_hierarchies import HWMESITwoLevelCacheHierarchy
from components.memories import HWDDR4

from gem5.resources.resource import BinaryResource
from gem5.simulate.simulator import Simulator
from gem5.simulate.exit_event import ExitEvent

from workloads.roi_manager import exit_event_handler
from workloads.array_sum_workload import (NaiveArraySumWorkload,
                                          ChunkingArraySumWorkload,
                                          NoResultRaceArraySumWorkload,
                                          ChunkingNoResultRaceArraySumWorkload,
                                          NoCacheBlockRaceArraySumWorkload,
                                          ChunkingNoBlockRaceArraySumWorkload)

cache_hierarchy = HWMESITwoLevelCacheHierarchy(xbar_latency=10)

memory = HWDDR4()

processor = HWO3CPU(num_cores=16)

board = HWX86Board(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

workload = NaiveArraySumWorkload(32768, 1)

board.set_workload(workload)

sim = Simulator(board=board,
                full_system=False,
                on_exit_event=exit_event_handler
)

sim.run()
