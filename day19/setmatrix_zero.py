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