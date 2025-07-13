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