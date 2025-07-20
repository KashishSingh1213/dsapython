#binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] < target:
            low = mid + 1  # Search in right half
        else:
            high = mid - 1  # Search in left half

    return -1  # Target not found


#question: Find the index of a target element in a sorted array using binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Your array and target
n = [2, 4, 6, 7, 8, 9, 10]
target = 6

# Call the function
result = binary_search(n, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")

#explanation
# The binary_search function takes a sorted array and a target value as input.
# It uses a while loop to repeatedly divide the search interval in half.
# If the target value is found, it returns the index; otherwise, it returns -1