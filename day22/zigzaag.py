#zigzag converstion
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
# Test the function
if __name__ == "__main__":
    test_cases = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
        ("AB", 1),
        ("ABCD", 2),
    ]

    for s, numRows in test_cases:
        result = convert(s, numRows)
        print(f"convert({s}, {numRows}) = {result}")
        