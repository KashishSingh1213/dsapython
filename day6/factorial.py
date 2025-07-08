#find the factorial of the number using recurion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

def factorial_iterative(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Iterative solution
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Recursive Factorial of", num, "is", factorial(num))
    print("Iterative Factorial of", num, "is", factorial_iterative(num))
