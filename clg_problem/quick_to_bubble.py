import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Generate a large random dataset
data_size = 1000
random_data = [random.randint(1, 10000) for _ in range(data_size)]

# Measure Bubble Sort time
bubble_data = random_data[:]
start_time = time.time()
bubble_sort(bubble_data)
bubble_time = time.time() - start_time

# Measure Quick Sort time
quick_data = random_data[:]
start_time = time.time()
quick_sort(quick_data, 0, len(quick_data) - 1)
quick_time = time.time() - start_time

# Print results
print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
print(f"Quick Sort Time: {quick_time:.6f} seconds")

if quick_time < bubble_time:
    print("Quick Sort is faster than Bubble Sort!")
else:
    print("Bubble Sort is faster than Quick Sort!")
