#insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr1 = [64, 34, 25, 12, 22, 11, 90]
print("Original array 1:", arr1)
insertion_sort(arr1)
print("Sorted array 1:", arr1)

# Another example
arr2 = [5, 2, 8, 1, 9, 3]
print("\nOriginal array 2:", arr2)
insertion_sort(arr2)
print("Sorted array 2:", arr2)

# Question: Sort the following array using insertion sort and print the result
arr3 = [12, 4, 7, 3, 15, 2]
print("\nOriginal array 3:", arr3)
insertion_sort(arr3)
print("Sorted array 3:", arr3)
