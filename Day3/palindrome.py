#check the palindrome
# lets take a example of n=1234 and i want to check the this is palindrome or not 

n = 1234
num = n
result = 0

while num > 0:
    ld = num % 10                 # get last digit
    result = (result * 10) + ld   # build reversed number
    num = num // 10               # remove last digit

print("The n value is:", result)



#lets take a 2nd example
n= 5873
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num = num//10
    print("the value of n is:",result)
    
    
# the question is 121
n=121
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num = num//10
    print('the value of n is:',result)
    
    
# the question is 222
n=222
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num = num//10
    print("the value is",result)




#solve the question of palindrome
def is_palindrome_number(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse

# Example number
num = 13431

# Check and print result
if is_palindrome_number(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


# Function to check if a number is a palindrome
def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse

# Example usage
number = 12321
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

    # Explanation
    # Time complexity: O(n)
    # Space complexity: O(1)
# The function checks if a number is a palindrome by reversing it and comparing it to the original.
# The algorithm runs in linear time, as it processes each digit of the number once.
# The space complexity is constant, as we are using a fixed amount of extra space.
## Example number
num = 1234321
# Check and print result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# Example number
num = 1234321
# Check and print result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
# Example number
num = 1234321
# Check and print result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

    #another example
    num = 98789
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
# Example number
num = 1234321
# Check and print result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#time complexity
# The time complexity of the is_palindrome function is O(n), where n is the number of digits in the input number.
# This is because the function processes each digit of the number exactly once.
# The space complexity is O(1) since it uses a fixed amount of extra space regardless of the input size.
# Example number
num = 1234321
# Check and print result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
