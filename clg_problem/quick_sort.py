def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(f"Partition at index {pi}: {arr}")
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

# Example data set
data = [27, 15, 39, 21, 28, 70]
print("Original Data Set:", data)

quick_sort(data, 0, len(data) - 1)
print("\nSorted Data Set:", data)