import random
import time
import matplotlib.pyplot as plt
import resource

# Priority Queue using Unsorted Array
class UnsortedArrayPriorityQueue:
    def __init__(self):
        # wait
        self.items = []

    def insert(self, item, priority):
        self.items.append((item, priority))

    def get_min(self):
        if not self.items:
            return None
        min_item = min(self.items, key=lambda x: x[1])
        return min_item[0]

    def extract_min(self):
        if not self.items:
            return None
        min_item = min(self.items, key=lambda x: x[1])
        self.items.remove(min_item)
        return min_item[0]

# Priority Queue using Sorted Array
class SortedArrayPriorityQueue:
    def __init__(self):
        self.items = []

    def insert(self, item, priority):
        self.items.append((item, priority))
        self.items.sort(key=lambda x: x[1])

    def get_min(self):
        if not self.items:
            return None
        return self.items[0][0]

    def extract_min(self):
        if not self.items:
            return None
        return self.items.pop(0)[0]

# Priority Queue using Sorted Linked List
class Node:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None

class SortedLinkedListPriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, item, priority):
        new_node = Node(item, priority)
        if not self.head or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and priority >= current.next.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def get_min(self):
        if not self.head:
            return None
        return self.head.item

    def extract_min(self):
        if not self.head:
            return None
        min_item = self.head.item
        self.head = self.head.next
        return min_item

# Priority Queue using D-ary Heap
class DHeapPriorityQueue:
    def __init__(self, d):
        self.items = []
        self.d = d

    def insert(self, item, priority):
        self.items.append((item, priority))
        self.heapify_up(len(self.items) - 1)

    def get_min(self):
        if not self.items:
            return None
        return self.items[0][0]

    def extract_min(self):
        if not self.items:
            return None
        min_item = self.items[0][0]
        last_item = self.items.pop()
        if len(self.items) > 0:
            self.items[0] = last_item
            self.heapify_down(0)
        return min_item

    def parent(self, i):
        return (i - 1) // self.d

    def heapify_up(self, i):
        while i > 0 and self.items[i][1] < self.items[self.parent(i)][1]:
            self.items[i], self.items[self.parent(i)] = self.items[self.parent(i)], self.items[i]
            i = self.parent(i)

    def heapify_down(self, i):
        min_child = self.min_child(i)
        while min_child is not None and self.items[i][1] > self.items[min_child][1]:
            self.items[i], self.items[min_child] = self.items[min_child], self.items[i]
            i = min_child
            min_child = self.min_child(i)

    def min_child(self, i):
        first_child = i * self.d + 1
        last_child = min(first_child + self.d, len(self.items))
        if first_child >= len(self.items):
            return None
        min_child = min(range(first_child, last_child), key=lambda x: self.items[x][1])
        return min_child
# Measure runtime for different input sizes
# input sizes from 1 to 1000, 5 interval
input_sizes = list(range(1, 1001, 5))

# Lists to store times for each operation and each priority queue type
insertion_times = {'Unsorted Array': [], 'Sorted Array': [], 'Sorted Linked List': [], 'D-ary Heap (d=2)': [], 'D-ary Heap (d=4)': []}
retrieval_times = {'Unsorted Array': [], 'Sorted Array': [], 'Sorted Linked List': [], 'D-ary Heap (d=2)': [], 'D-ary Heap (d=4)': []}
extraction_times = {'Unsorted Array': [], 'Sorted Array': [], 'Sorted Linked List': [], 'D-ary Heap (d=2)': [], 'D-ary Heap (d=4)': []}

for size in input_sizes:
    print(size)
    data = [(random.randint(1, 100), random.randint(1, 1000)) for _ in range(size)]
    
    # Measure insertion time
    start_time = time.time()
    unsorted_pq = UnsortedArrayPriorityQueue()
    for item, priority in data:
        unsorted_pq.insert(item, priority)
    insertion_times['Unsorted Array'].append(time.time() - start_time)

    start_time = time.time()
    sorted_pq = SortedArrayPriorityQueue()
    for item, priority in data:
        sorted_pq.insert(item, priority)
    insertion_times['Sorted Array'].append(time.time() - start_time)

    start_time = time.time()
    sorted_ll_pq = SortedLinkedListPriorityQueue()
    for item, priority in data:
        sorted_ll_pq.insert(item, priority)
    insertion_times['Sorted Linked List'].append(time.time() - start_time)

    start_time = time.time()
    d_heap_pq2 = DHeapPriorityQueue(2)  # D-ary heap with d=2
    for item, priority in data:
        d_heap_pq2.insert(item, priority)
    insertion_times['D-ary Heap (d=2)'].append(time.time() - start_time)

    start_time = time.time()
    d_heap_pq4 = DHeapPriorityQueue(4)  # D-ary heap with d=4
    for item, priority in data:
        d_heap_pq4.insert(item, priority)
    insertion_times['D-ary Heap (d=4)'].append(time.time() - start_time)

    # Measure retrieval time
    start_time = time.time()
    for _ in range(size):
        unsorted_pq.get_min()
    retrieval_times['Unsorted Array'].append((time.time() - start_time) / size)

    start_time = time.time()
    for _ in range(size):
        sorted_pq.get_min()
    retrieval_times['Sorted Array'].append((time.time() - start_time) / size)

    start_time = time.time()
    for _ in range(size):
        sorted_ll_pq.get_min()
    retrieval_times['Sorted Linked List'].append((time.time() - start_time) / size)

    start_time = time.time()
    for _ in range(size):
        d_heap_pq2.get_min()
    retrieval_times['D-ary Heap (d=2)'].append((time.time() - start_time) / size)

    start_time = time.time()
    for _ in range(size):
        d_heap_pq4.get_min()
    retrieval_times['D-ary Heap (d=4)'].append((time.time() - start_time) / size)

    # Measure extraction time
    start_time = time.time()
    for _ in range(size):
        unsorted_pq.extract_min()
    extraction_times['Unsorted Array'].append((time.time() - start_time) / size)

    start_time = time.time()
    for _ in range(size):
        sorted_pq.extract_min()
    extraction_times['Sorted Array'].append((time.time() - start_time) / size)

    start_time = time.time()
    for _ in range(size):
        sorted_ll_pq.extract_min()
    extraction_times['Sorted Linked List'].append((time.time() - start_time) / size)

    start_time = time.time()
    for _ in range(size):
        d_heap_pq2.extract_min()
    extraction_times['D-ary Heap (d=2)'].append((time.time() - start_time) / size)

    start_time = time.time()
    for _ in range(size):
        d_heap_pq4.extract_min()
    extraction_times['D-ary Heap (d=4)'].append((time.time() - start_time) / size)

# Plot runtimes for insertion
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
for pq_type, times in insertion_times.items():
    plt.plot(input_sizes, times, label=pq_type)
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.title("Insertion Time")
plt.legend()

# Plot runtimes for retrieval
plt.subplot(1, 3, 2)
for pq_type, times in retrieval_times.items():
    plt.plot(input_sizes, times, label=pq_type)
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.title("Retrieval Time")
plt.legend()

# Plot runtimes for extraction
plt.subplot(1, 3, 3)
for pq_type, times in extraction_times.items():
    plt.plot(input_sizes, times, label=pq_type)
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.title("Extraction Time")
plt.legend()

plt.tight_layout()
plt.savefig("pq_operations.png")


plt.clf()
# Measure runtime for different values of d
d_values = list(range(2, 11))
d_heap_runtimes = []

for d in d_values:
    data = [(random.randint(1, 100), random.randint(1, 1000)) for _ in range(1000)]

    start_time = time.time()
    d_heap_pq = DHeapPriorityQueue(d)
    for item, priority in data:
        d_heap_pq.insert(item, priority)
    d_heap_times = time.time() - start_time
    d_heap_runtimes.append(d_heap_times)

# Plot runtimes for different d values
plt.plot(d_values, d_heap_runtimes, marker='o')
plt.xlabel("Value of d")
plt.ylabel("Runtime (seconds)")
plt.title("D-ary Heap Priority Queue Runtimes")
plt.xticks(d_values)
plt.grid()
plt.savefig("d_heap.png")

plt.clf()

d_values = list(range(2, 11))
d_heap_resources = []

for d in d_values:
    data = [(random.randint(1, 100), random.randint(1, 1000)) for _ in range(1000)]

    # Start measuring resource usage
    resource_usage_start = resource.getrusage(resource.RUSAGE_SELF)

    start_time = time.time()
    d_heap_pq = DHeapPriorityQueue(d)
    for item, priority in data:
        d_heap_pq.insert(item, priority)
    d_heap_times = time.time() - start_time

    # End measuring resource usage
    resource_usage_end = resource.getrusage(resource.RUSAGE_SELF)

    # Calculate resource usage statistics
    cpu_time_user = resource_usage_end.ru_utime - resource_usage_start.ru_utime
    max_resident_set_size = resource_usage_end.ru_maxrss

    d_heap_resources.append({
        "d": d,
        "cpu_time_user": cpu_time_user,
        "max_resident_set_size": max_resident_set_size,
        "execution_time": d_heap_times
    })

# Extract resource usage data
cpu_times_user = [data['cpu_time_user'] for data in d_heap_resources]
max_resident_set_sizes = [data['max_resident_set_size'] for data in d_heap_resources]

# Plot resource usage for different d values
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(d_values, cpu_times_user, marker='o')
plt.xlabel("Value of d")
plt.ylabel("CPU Time (User) (seconds)")
plt.title("CPU Time (User) vs. d")

plt.subplot(1, 2, 2)
plt.plot(d_values, max_resident_set_sizes, marker='o', color='orange')
plt.xlabel("Value of d")
plt.ylabel("Maximum Resident Set Size (Memory) (KB)")
plt.title("Maximum Resident Set Size (Memory) vs. d")

plt.tight_layout()
plt.savefig("d_heap_resources.png")