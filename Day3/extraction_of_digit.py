#example we have a number=5873 and i want to print the digit one by one like reverse num. 3,7,8,5

num = 5873

while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

#count digits
#let num=5438
num = 5438
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Number of digits:", count)



#count no. 
def count_digits(n):
    # Base case
    if n == 0:
        return 0
    # Recursive case
    return 1 + count_digits(n // 10)

# Example number
num = 13456

# Special case for 0
if num == 0:
    print("Number of digits: 1")
else:
    print("Number of digits:", count_digits(num))


# Extracting digits from a number
def extract_digits(n):
    digits = []
    while n > 0:
        last_digit = n % 10
        digits.append(last_digit)
        n = n // 10
    return digits[::-1]  # Reverse to maintain original order
    # Example number
num = 12345 
print("Extracted digits:", extract_digits(num))

# Example of if-else statement
num = 10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# Example of extracting digits from a number