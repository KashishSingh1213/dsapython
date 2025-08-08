#remove duplicate elements from an array
def remove_duplicates(arr): 
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
# Explanation:  
# The function remove_duplicates iterates through the input array and uses a set to track seen elements.
# If an element is not in the set, it is added to both the set and the result list.
# This ensures that only unique elements are included in the final result.

#right rotate array by 1 place
def right_rotate(arr):
    if len(arr) == 0:
        return arr
    last_element = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element
    return arr
print(right_rotate([1, 2, 3, 4, 5]))  # Output: [5, 1, 2, 3, 4]
# Explanation:      
# The function right_rotate takes an array and rotates it to the right by one position.
# It stores the last element, shifts all other elements to the right, and places the last   
# element at the start of the array.
# Example outputs:
# The array [1, 2, 3, 4, 5] becomes
# [5, 1, 2, 3, 4] after the right rotation.
#left rotate array by 1 place
def left_rotate(arr):
    if len(arr) == 0:
        return arr
    first_element = arr[0]
    for i in range(0, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = first_element
    return arr
print(left_rotate([1, 2, 3, 4, 5]))  # Output: [2, 3, 4, 5, 1]
# Explanation:
# The function left_rotate takes an array and rotates it to the left by one position.   
# It stores the first element, shifts all other elements to the left, and places the first
# element at the end of the array.
# Example outputs:
# The array [1, 2, 3, 4, 5] becomes
# [2, 3, 4, 5, 1] after the left
# rotation.

#right rotate array by k places
def right_rotate_k(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n  # Handle cases where k is greater than n
    return arr[-k:] + arr[:-k]
print(right_rotate_k([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
# Explanation:  
# The function right_rotate_k takes an array and rotates it to the right by k positions.
# It calculates the effective rotation by taking k modulo the length of the array.
# The last k elements are moved to the front, and the rest are shifted accordingly.
# Example outputs:
# The array [1, 2, 3, 4, 5] becomes
# [4, 5, 1, 2, 3] after the right rotation.

#moves all zeroes to the end of the array
def move_zeroes_to_end(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0
    return arr
print(move_zeroes_to_end([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
# Explanation:
# The function move_zeroes_to_end iterates through the array and moves all non-zero elements
# to the front, keeping track of the index for non-zero elements.

# The remaining elements are set to zero.
# Example outputs:
# The array [0, 1, 0, 3, 12] becomes
# [1, 3, 12, 0, 0] after moving zeroes to the end.
# This code implements the right and left rotation of an array, as well as removing duplicates and moving zeroes to the end.
# This code implements the right and left rotation of an array, as well as removing duplicates and moving zeroes to the end.
