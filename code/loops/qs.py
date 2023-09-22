import random
import time
import matplotlib.pyplot as plt

# bucket sort
def bucket_sort(arr):
    if not arr:
        return []

    # Determine minimum and maximum values in the list
    min_val, max_val = min(arr), max(arr)

    # Create buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Place elements into buckets
    for num in arr:
        index = int(((num - min_val) * (bucket_count - 1)) / (max_val - min_val))
        buckets[index].append(num)

    # Sort each bucket and gather results
    sorted_data = []
    for bucket in buckets:
        quicksort(bucket)  # Using QuickSort for individual buckets
        sorted_data.extend(bucket)

    return sorted_data


# QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Randomized QuickSort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Generate 100 data points of size 1000 with random integers between 1 to 10000
data_points = [random.sample(range(1, 10001), 1000) for _ in range(100)]

# Measure sorting time for each data point using QuickSort
quicksort_durations = []
for data in data_points:
    start_time = time.time()
    quicksort(list(data))
    quicksort_durations.append(time.time() - start_time)

# Measure sorting time for each data point using Bucket Sort
bucket_sort_durations = []
for data in data_points:
    start_time = time.time()
    bucket_sort(list(data))
    bucket_sort_durations.append(time.time() - start_time)

randomized_quicksort_durations = []
for data in data_points:
    start_time = time.time()
    randomized_quicksort(list(data))
    randomized_quicksort_durations.append(time.time() - start_time)

# Plotting the results
plt.figure(figsize=(12, 6))

# X-axis labels
labels = list(range(1, 101))

# Plotting the durations
plt.plot(labels, quicksort_durations, color='blue', marker='o', label='QuickSort')
plt.plot(labels, bucket_sort_durations, color='green', marker='o', label='Bucket Sort')
plt.plot(labels, randomized_quicksort_durations, color='red', marker='o', label='Randomized QuickSort')

# Configuring the chart
plt.xlabel('Data Point')
plt.ylabel('Duration (seconds)')
plt.title('QuickSort vs. Bucket Sort vs. Randomized QuickSort')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Display the chart
plt.savefig('qs.png')