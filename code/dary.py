import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Function to extract the maximum element from a d-ary max-heap
def extract_max(heap, d):
    if not heap:
        return None

    # Store the maximum element (at the root)
    max_val = heap[0]

    # Replace the root with the last element in the array
    heap[0] = heap.pop()

    # Heapify the root element down to its correct position
    heapify_down(heap, d, 0)

    return max_val

# Function to restore the max-heap property from a given index down the tree
def heapify_down(heap, d, i):
    while True:
        largest = i
        child_indices = children(i, d)

        # Find the index of the largest child
        for child_index in child_indices:
            if child_index < len(heap) and heap[child_index] > heap[largest]:
                largest = child_index

        if largest != i:
            # Swap the parent and largest child
            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest
        else:
            break

# Function to get the child indices of a node at index i
def children(i, d):
    child_indices = []
    for k in range(1, d + 1):
        child_indices.append(d * i + k)
    return child_indices

# Function to build a d-ary max-heap from a list of elements
def build_max_heap(arr, d):
    n = len(arr)
    for i in range((n - 1) // d, -1, -1):
        heapify_down(arr, d, i)

def measure_extraction_time(d, n):
    data = [random.randint(1, n * 10) for _ in range(n)]
    build_max_heap(data, d)

    def extract():
        extract_max(data, d)

    return timeit.timeit(extract, number=1)

# Chart the execution times
d_values = [2, 3, 4]  # Vary d (the arity)
n = 1000  # Number of data points
execution_times = []

for d in d_values:
    times = [measure_extraction_time(d, n) for _ in range(100)]
    execution_times.append(times)

# Calculate the average curve
average_curve = np.mean(execution_times, axis=0)

# Create a chart
plt.figure(figsize=(10, 6))
for i, d in enumerate(d_values):
    plt.plot(range(1, 101), execution_times[i], label=f'd={d}')

# Plot the average curve
plt.plot(range(1, 101), average_curve, label='Average', color='black', linewidth=3)

plt.xlabel('Iteration')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.title('Execution Time for EXTRACT-MAX in a d-ary Max-Heap')
plt.show()