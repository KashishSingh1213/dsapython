#linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0  
    return arr
print(linear_search([1, 2, 3, 4, 5], 3))  # Output: 2


#merge two sorted arrays
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    # Compare elements from both arrays and add the smaller one
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements if any
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

result = merge_sorted_arrays(arr1, arr2)
print("Merged Sorted Array:", result)


#find the missing number in an array
def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    return total_sum - array_sum
print(find_missing_number([1, 2, 4, 5], 5))  # Output: 3


# Explanation:
# The function linear_search iterates through the array and checks each element against the target.
# If it finds the target, it returns the index; otherwise, it returns -1.
# The function merge_sorted_arrays merges two sorted arrays into one sorted array.
# The function find_missing_number calculates the expected sum of numbers from 1 to n and subtract

#solve linear search
#s the actual sum of the array to find the missing number.
# The output of each function is printed    