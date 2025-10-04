def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        print(f"Iteration {i}:")
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)  # Print array after each iteration
    return arr

# Example data set
data = [27, 15, 39, 21, 28, 70]
print("Original Data Set:", data)

sorted_data = insertion_sort(data)
print("\nSorted Data Set:", sorted_data)
