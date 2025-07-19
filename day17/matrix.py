#set matrix element to zero
#solve brute force

def setZeroes(matrix):
    """
    Brute force approach to set matrix zeroes
    Time complexity: O(m*n*(m+n))
    Space complexity: O(m+n)
    """
    if not matrix or not matrix[0]:
        return
    
    m, n = len(matrix), len(matrix[0])
    zero_positions = []
    
    # Step 1: Find all zero positions
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))
    
    # Step 2: Set rows and columns to zero
    for row, col in zero_positions:
        # Set entire row to zero
        for j in range(n):
            matrix[row][j] = 0
        
        # Set entire column to zero
        for i in range(m):
            matrix[i][col] = 0

# Test the function
if __name__ == "__main__":
    # Test case 1
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    print("Original matrix:")
    for row in matrix1:
        print(row)
    
    setZeroes(matrix1)
    print("\nAfter setting zeroes:")
    for row in matrix1:
        print(row)
    
    # Test case 2
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print("\nOriginal matrix:")
    for row in matrix2:
        print(row)
    
    setZeroes(matrix2)
    print("\nAfter setting zeroes:")
    for row in matrix2:
        print(row)

        #explation
# The brute force solution iterates through the matrix to find zeroes and then sets the corresponding rows and columns to zero.
# The time complexity is O(m*n*(m+n)) due to the nested loops for finding zeroes and setting rows/columns.
#solve optimal solution
def setZeroesOptimal(matrix):
    """
    Optimal approach to set matrix zeroes
    Time complexity: O(m*n)
    Space complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return
    
    m, n = len(matrix), len(matrix[0])
    row_zero = False
    col_zero = False
    
    # Step 1: Check if first row and first column need to be zeroed
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
    max_length = max(max_length, current_length)
print("Longest consecutive sequence length (brute force):", max_length)

# time complexity: O(n^2)
# The optimal solution uses the first row and column to mark zeroes, reducing space complexity to O(1).


#solve another question
# This code sets matrix elements to zero based on the presence of zeroes in the matrix.
# The brute force solution has a time complexity of O(m*n*(m+n)) and space
# complexity of O(m+n).
# The optimal solution has a time complexity of O(m*n) and space complexity of O(1).
# The brute force solution iterates through the matrix to find zeroes and then sets the corresponding