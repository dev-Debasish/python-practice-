def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        print(f"Iteration {i + 1}:")
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True
            print(arr)  # Print array after each swap
        if not swapped:  # If no swaps occur, the array is already sorted
            break
    return arr

# Example data set
data = [27, 15, 39, 21, 28, 70]
print("Original Data Set:", data)

sorted_data = bubble_sort(data)
print("\nSorted Data Set:", sorted_data)
