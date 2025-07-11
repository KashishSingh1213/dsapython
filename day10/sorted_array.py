#check the array is sorted or not
num=[1,2,3,4,5,6,7,8,9]
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(is_sorted(num))  # Output: True

#check the array is not sorted
num2=[1,2,3,4,5,6,7,8,9,0]
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(is_sorted(num2))  # Output: False

# Explanation:
# The function is_sorted checks if the given array is sorted in ascending order.
# It iterates through the array and compares each element with the next one.
# If it finds any element greater than the next, it returns False (not sorted).
# Otherwise, it returns True (sorted).
# Example outputs:
# num is sorted, so is_sorted(num) returns True.
# num2 is not sorted (last element is 0), so is_sorted(num2) returns False.