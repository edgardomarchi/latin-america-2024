import argparse

from gem5.simulate.simulator import Simulator
from gem5.components.boards.test_board import TestBoard
from gem5.components.memory.simple import SingleChannelSimpleMemory
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.memory.multi_channel import ChanneledMemory
from gem5.components.memory.dram_interfaces.lpddr5 import LPDDR5_6400_1x16_BG_BL32
from gem5.components.processors.linear_generator import LinearGenerator
from gem5.components.processors.random_generator import RandomGenerator
from gem5.components.cachehierarchies.classic.no_cache import NoCache

parser = argparse.ArgumentParser()
parser.add_argument("rate", type=str, help="The rate of the generator")
parser.add_argument("percentage", type=int, help="The read percentage for the generator")
parser.add_argument("memory", type=str, help="The memory type to use")
parser.add_argument("--random", action="store_true", help="Use a random generator")

args = parser.parse_args()

simple_memory = SingleChannelSimpleMemory(
        latency="20ns", bandwidth="32GiB/s",
        latency_var="0s", size="1GiB")

# ddr4 = SingleChannelDDR4_2400()


#lpddr5 = ChanneledMemory(LPDDR5_6400_1x16_BG_BL32, 1, 64)


def get_memory(mem_type: str):
    if mem_type == "simple":
        return SingleChannelSimpleMemory(
            latency="20ns", bandwidth="32GiB/s", latency_var="0s", size="1GiB"
        )
    elif mem_type == "DDR4":
        return SingleChannelDDR4_2400()
    elif mem_type == "SC_LPDDR5":
        return ChanneledMemory(LPDDR5_6400_1x16_BG_BL32, 4, 64)


generator = RandomGenerator(num_cores=1,
                            rate=args.rate,
                            rd_perc=args.percentage) if args.random else\
            LinearGenerator(num_cores=1,
                            rate=args.rate,
                            rd_perc=args.percentage)

board = TestBoard(
    clk_freq="3GHz", # ignored
    generator=generator,
    memory=get_memory(args.memory),
    cache_hierarchy=NoCache(),
)

simulator = Simulator(board=board)
simulator.run()

stats = simulator.get_simstats()
seconds = stats.simTicks.value / stats.simFreq.value
total_bytes = (
    stats.board.processor.cores[0].generator.bytesRead.value
    + stats.board.processor.cores[0].generator.bytesWritten.value
)
latency = (
   stats.board.processor.cores[0].generator.totalReadLatency.value
    / stats.board.processor.cores[0].generator.totalReads.value
)
print(f"Total bandwidth: {total_bytes / seconds / 2**30:0.2f} GiB/s")
print(f"Average latency: {latency / stats.simFreq.value * 1e9:0.2f} ns")

