#search insert position
#all elemnts are arranged
#array is sorted in ascending order
nums=[1,3,4,5,8,9,14,15,19,20]
def search_insert(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low
printf("The target element %d should be inserted at index %d\n", 20, search_insert(nums,20))
# Additional example
printf("The target element %d should be inserted at index %d\n", 7, search_insert(nums,7))

#time complexity: O(log n)
#space complexity: O(1)



#another question for binary search
#ceil the floor of the array
nums=[3,4,4,4,8,9,9,10,12,12,14,15]
target = 8
floor=8
ceil=8
def search_floor_ceil(nums, target):
    low = 0
    high = len(nums) - 1
    floor = -1
    ceil = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid, mid  # Found both floor and ceil at the same index
        elif nums[mid] < target:
            floor = mid  # Update floor
            low = mid + 1
        else:
            ceil = mid  # Update ceil
            high = mid - 1
            
    return floor, ceil
print("The floor of the target element %d is at index %d and the ceil is at index %d" % (target, *search_floor_ceil(nums, target)))
# Additional example
target2 = 11
print("The floor of the target element %d is at index %d and the ceil is at index %d" % (target2, *search_floor_ceil(nums, target2)))


#time complexity: O(log n)
#space complexity: O(1)


#optimal solution
def find_floor_and_ceil(arr, target):
    low, high = 0, len(arr) - 1
    floor_val, ceil_val = -1, -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid], arr[mid]  # Exact match is both floor and ceil
        elif arr[mid] < target:
            floor_val = arr[mid]
            low = mid + 1
        else:
            ceil_val = arr[mid]
            high = mid - 1

    return floor_val, ceil_val


#explantion
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
    
    # Step 3: Set zeroes based on marks
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Step 4: Set first row and column to zero if needed
    if row_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    if col_zero:
        for i in range(m):
            matrix[i][0] = 0


    # Test the optimal function
if __name__ == "__main__":
    # Test case 1
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    print("Original matrix:")
    for row in matrix1:
        print(row)
    
    setZeroesOptimal(matrix1)
    print("\nAfter setting zeroes:")
    for row in matrix1:
        print(row)
    
    # Test case 2
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print("\nOriginal matrix:")
    for row in matrix2:
        print(row)
    
    setZeroesOptimal(matrix2)
    print("\nAfter setting zeroes:")
    for row in matrix2:
        print(row)

    # Additional example
    matrix3 = [[1,2,3],[4,0,6],[7,8,9]]
    print("\nOriginal matrix:")
    for row in matrix3:
        print(row)
    
    setZeroesOptimal(matrix3)
    print("\nAfter setting zeroes:")
    for row in matrix3:
        print(row)

#search insert position
def printf(format, *args):  
    print(format % args)

#zigzag conversion
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    index, step = 0, 1

    for char in s:
        rows[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(rows)

#time complexity is O(n) where n is the length of the string s
#space complexity is O(n) as well, for the storage of the rows
# The overall complexity is efficient for the problem at hand.
# Test the zigzag conversion function
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    result = convert(s, numRows)
    print(f"The zigzag conversion of '{s}' with {numRows} rows is: '{result}'")

    # Additional example
    s2 = "HELLOZIGZAG"
    numRows2 = 4
    result2 = convert(s2, numRows2)
    print(f"The zigzag conversion of '{s2}' with {numRows2} rows is: '{result2}'")
# Longest consecutive sequence in an array
def longest_consecutive(nums):  
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:  # Only start counting from the beginning of a sequence
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
# Test the longest consecutive sequence function
if __name__ == "__main__":
    # Test case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Longest consecutive sequence in {nums1}: {longest_consecutive(nums1)}")

    # Test case 2
    nums2 = [0, 0, 1, 1, 2, 2, 3, 3]
    print(f"Longest consecutive sequence in {nums2}: {longest_consecutive(nums2)}")

    # Test case 3
    nums3 = []
    print(f"Longest consecutive sequence in {nums3}: {longest_consecutive(nums3)}")
