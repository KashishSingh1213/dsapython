#lets solve the question of armstrong number
n = 153
num = n
result = 0

while num > 0:
    digit = num % 10         # get last digit
    result += digit ** 3     # cube it and add to result
    num = num // 10          # remove last digit

if result == n:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
    
    
#lets take a example of 1634
n=1634
num=n
result=0
while num>0:
    digit=num%10
    result+=digit**3
    num=num//10
    
if result==n:
    print("the number is armstrong")
else:
    print("the number is not armstrong")