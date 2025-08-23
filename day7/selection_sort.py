# Selection sort

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


#explaintion
# Time complexity: O(n^2)
# Space complexity: O(1)
# Explanation: The selection sort algorithm repeatedly finds the minimum element from the unsorted part of the array and swaps it with the first unsorted element. This results in a time complexity of O(n^2) due to the nested loops, while the space complexity is O(1) since it sorts the array in place.
# Time complexity: O(n^2)
# Space complexity: O(1)
# The selection sort algorithm is a simple sorting algorithm that divides the input list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest (or largest, depending on the order) element from the unsorted part and moves it to the end of the sorted part.
#explain steps
# 1. Start with the first element as the minimum.
# 2. Compare it with the rest of the elements to find the smallest one.
# 3. Swap the found minimum element with the first unsorted element.
# 4. Move the boundary of the sorted part one element to the right.
# 5. Repeat the process until the entire array is sorted.
# Example usage
