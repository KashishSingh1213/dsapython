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