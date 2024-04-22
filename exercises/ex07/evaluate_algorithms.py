"""Functions that implement sorting algorithms."""

__author__ = "730476889"

import matplotlib.pyplot as plt
from runtime_analysis_functions import evaluate_runtime
from runtime_analysis_functions import evaluate_memory_usage


START_SIZE: int = 0
END_SIZE: int = 1000
times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - 730476889")
plt.show()


START_SIZE: int = 0
END_SIZE: int = 1000
times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - 730476889")
plt.show()


START_SIZE: int = 0
END_SIZE: int = 1000
usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - 730476889")
plt.show()


START_SIZE: int = 0
END_SIZE: int = 1000
usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - 730476889")
plt.show()
