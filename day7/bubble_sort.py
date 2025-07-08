#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swapping happened
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if elements are out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping happened, array is already sorted
        if not swapped:
            break

# Example usage
arr = [5, 3, 8, 4, 2]
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
