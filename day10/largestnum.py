# #find the largest numberin array
# nums=[55,32,97,99,3,67]
# def find_largest(nums):
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest

# print(find_largest(nums))


#find the second largest number in array
nums=[55,34,87,22,12]
def find_second_largest(nums):
    largest = second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
print(find_second_largest(nums))

#time complexity: O(n)
#space complexity: O(1)
#find the second largest number in array
# This function iterates through the list once, keeping track of the largest and second largest numbers
def setZeroesOptimal(matrix):
    if not matrix or not matrix[0]:
        return
    
    m, n = len(matrix), len(matrix[0])
    row_zero = False
    col_zero = False
    
    # Step 1: Check if first row and column need to be zeroed
    for i in range(m):
        if matrix[i][0] == 0:
            col_zero = True
            break
    
    for j in range(n):
        if matrix[0][j] == 0:
            row_zero = True
            break
    # Step 2: Use first row and column to mark zeroes
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

#time complexity
    # O(m * n)
#space complexity