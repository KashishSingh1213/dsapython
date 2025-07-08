#selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)

# Another example
arr2 = [29, 10, 14, 37, 13]
print("Original array 2:", arr2)
selection_sort(arr2)
print("Sorted array 2:", arr2)


