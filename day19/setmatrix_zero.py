#set matrix zero
#brute force solution
def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    # Step 1: Store the row and column index for each 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Step 2: Set rows to 0
    for i in zero_rows:
        for j in range(cols):
            matrix[i][j] = 0

    # Step 3: Set columns to 0
    for j in zero_cols:
        for i in range(rows):
            matrix[i][j] = 0

    return matrix


#explanation
#time complexity: O(m*n)
#space complexity: O(m+n)
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