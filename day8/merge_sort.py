def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
print("Merge sort completed.")

# Another example
arr2 = [5, 2, 4, 6, 1, 3]
print("Original array 2:", arr2)
merge_sort(arr2)
print("Sorted array 2:", arr2)
print("Merge sort completed.")

# This code implements the merge sort algorithm, which is a divide-and-conquer sorting technique.
# It recursively divides the array into halves, sorts each half, and then merges them back together
# in sorted order. The example usage demonstrates how to use the `merge_sort` function on two different arrays.
# The output will show the original and sorted arrays for both examples.
# Merge sort is efficient for large datasets and has a time complexity of O(n log n).
# It is a stable sort, meaning that it maintains the relative order of equal elements.
# Merge sort is particularly useful for sorting linked lists and large datasets that do not fit into memory.
# It is also used in external sorting algorithms where data is too large to fit into memory.