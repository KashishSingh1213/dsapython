#2d matrix
#how to represent a 2d matrix in python
class matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Index out of bounds")

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Index out of bounds")
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


# Creating a 2D matrix (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the matrix
print("Matrix:")
for row in matrix:
    print(row)

# Accessing an element
print("\nElement at row 2, col 3:", matrix[1][2])  # Indexing starts from 0

# Modifying an element
matrix[0][0] = 10
print("\nModified Matrix:")
for row in matrix:
    print(row)

# Using the matrix class