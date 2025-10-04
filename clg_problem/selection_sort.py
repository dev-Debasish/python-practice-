def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        print(f"Iteration {i + 1}:")
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap elements
        print(arr)  # Print array after each iteration
    return arr

# Example data set
data = [27, 15, 39, 21, 28, 70]
print("Original Data Set:", data)

sorted_data = selection_sort(data)
print("\nSorted Data Set:", sorted_data)
