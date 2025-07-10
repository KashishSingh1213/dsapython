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
    