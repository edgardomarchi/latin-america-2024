"""
This example demonstrates how to set up a simple gem5 simulation with a
single-core Timing CPU, a private L1 and shared L2 cache hierarchy, and
DDR4 memory. We'll use the 'x86-getting-started-benchmark-suite' to
run a sample workload. The steps include:

1. Importing necessary gem5 modules.
2. Creating memory, cache hierarchy, and processor components.
3. Setting up a SimpleBoard with these components.
4. Obtaining the benchmark suite resource.
5. Printing available workloads and input groups.
6. Filtering and selecting a specific workload.
7. Setting the workload on the board.
8. Running the simulation.
"""

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_shared_l2_cache_hierarchy import (
    PrivateL1SharedL2CacheHierarchy,
)
from gem5.components.memory.single_channel import SingleChannelDDR4_2400

from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA

from gem5.resources.resource import obtain_resource

from gem5.simulate.simulator import Simulator
