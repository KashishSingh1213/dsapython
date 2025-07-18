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