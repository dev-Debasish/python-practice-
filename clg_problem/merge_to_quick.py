import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Generate a large random dataset
data_size = 10000
random_data = [random.randint(1, 100000) for _ in range(data_size)]

# Measure Merge Sort time
merge_data = random_data[:]
start_time = time.time()
merge_sort(merge_data)
merge_time = time.time() - start_time

# Measure Quick Sort time
quick_data = random_data[:]
start_time = time.time()
quick_sort(quick_data, 0, len(quick_data) - 1)
quick_time = time.time() - start_time

# Print results
print(f"Merge Sort Time: {merge_time:.6f} seconds")
print(f"Quick Sort Time: {quick_time:.6f} seconds")

if merge_time <= quick_time:
    print("Merge Sort is more effective than Quick Sort!")
else:
    print("Quick Sort is more effective than Merge Sort!")
