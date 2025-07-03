#check the palindrome
# lets take a example of n=1234 and i want to check the this is palindrome or not 

# n = 1234
# num = n
# result = 0

# while num > 0:
#     ld = num % 10                 # get last digit
#     result = (result * 10) + ld   # build reversed number
#     num = num // 10               # remove last digit

# print("The n value is:", result)



#lets take a 2nd example
n= 5873
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num = num//10
    print("the value of n is:",result)