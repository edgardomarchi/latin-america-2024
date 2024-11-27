# Cache coherence responses

### Question 1

Q: For algorithm 1, does increasing the number of threads improve performance or hurt performance? Use data to back up your answer.

A:

| Threads | Time (avrg.) |
|---------|--------------|
| 1       | 0.3 ms       |
| 2       | 0.6 ms       |
| 4       | 0.6 ms       |
| 8       | 0.55 ms      |
| 16      | 0.6 ms       |

The performance is hurt when using more than one thread.
For multi-threading, the performance does not improve when incresing the number of threads.

### Question 2

(a) Q: For algorithm 6, does increasing the number of threads improve performance or hurt performance? Use data to back up your answer.

A:

| Threads | Time (avrg.) |
|---------|--------------|
| 1       | 0.3 ms       |
| 2       | 0.25 ms      |
| 4       | 0.2 ms       |
| 8       | 0.45 ms      |
| 16      | 0.6 ms       |

For this experiment increasing the number of threads improves performance but only for a small number of threads.
As it can be seen, best performance is achieved with 4 threads.
Increasing the number of threads beyond that hurts performance also.

(b) Q: What is the speedup when you use 2, 4, 8, and 16 threads (only answer with up to the number of cores on your system).

A: The maximum achieved speedup is about 1.5 with 4 threads.

### Question 3

(a) Q: Using the data for all 6 algorithms, what is the most important optimization, chunking the array, using different result addresses, or putting padding between the result addresses?

A: According to the runtimes, the most important optimization is putting padding between the result address.

(b) Q: Speculate how the hardware implementation is causing this result. What is it about the hardware that causes this optimization to be most important?

A: It seems that keeping coherence between different low level caches it is producing the performance issue. Since using different blocks by different cores produces the best results.

### Question 4

(a) Q: What is the speedup of algorithm 1 and speedup of algorithm 6 on *16 cores* as estimated by gem5?

A: Algorithm 1 produces no speedup since runtime is 0.917 ms, and algorithm 6 produces a considerable speedup with a runtime of 0.111 ms. Base time for 1 thread is: 0.866 ms.

(b) Q: How does this compare to what you saw on the real system?

A: In my real system the performance loss comparing the single thraded vs the multi thraded Naive algorithm is much more significant.
In the other hand, when running algorithm 6, the performance gain is not as significant as in the simulation. Moreover, for 16 threads in the real system the performance is identical to the obtained with algorithm 1.

### Question 5

Q: Which optimization (chunking the array, using different result addresses, or putting padding between the result addresses) has the biggest impact on the *hit ratio?*

Show the data you use to make this determination.
Discuss which algorithms you are comparing and why.

A:

Simulation times:

| Algorithm 1 | Algorithm 2 | Algorithm 3 | Algorithm 4 | Algorithm 5 | Algorithm 6 |
|-------------|-------------|-------------|-------------|-------------|-------------|
| 0.000917    | 0.000915    | 0.000686    | 0.000687    | 0.000145    | 0.000111    |

It can be seen that putting padding between the results (each thread writing in a different block) produces the most significative improvement.

### Question 6

Q: Which optimization (chunking the array, using different result addresses, or putting padding between the result addresses) has the biggest impact on the *read sharing?*

Show the data you use to make this determination.
Discuss which algorithms you are comparing and why.

A:

### Question 7

Q: Which optimization (chunking the array, using different result addresses, or putting padding between the result addresses) has the biggest impact on the *write sharing?*

Show the data you use to make this determination.
Discuss which algorithms you are comparing and why.

A:

### Question 8

Let's get back to the question we're trying to answer. From [question 3](#question-3) above, "What is it about the hardware that causes this optimization to be most important?"

So:
(a) Q: Out of the three characteristics we have looked at, the L1 hit ratio, the read sharing, or the write sharing, which is most important for determining performance?
Use the average memory latency (and overall performance) to address this question.

A:

Finally, you should have an idea of what optimizations have the biggest impact on the hit ratio, the read sharing performance, and the write sharing performance.

So:
(b) Q: Using data from the gem5 simulations, now answer what hardware characteristic *causes* the most important optimization to be the most important.

A:

### Question 9

Run using a `xbar_latency` of 1 cycle and 25 cycles (in addition to the 10 cycles that you have already run).

Q: As you increase the cache-to-cache latency, how does it affect the importance of the different optimizations?

You don't have to run all algorithms.
You can probably get away with just running algorithm 1 and algorithm 6.

A:
