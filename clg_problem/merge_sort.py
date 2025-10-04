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
            print("Merging:", arr)
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            print("Merging:", arr)
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            print("Merging:", arr)

# Example data set
data = [27, 15, 39, 21, 28, 70]
print("Original Data Set:", data)

merge_sort(data)
print("\nSorted Data Set:", data)