#fibbonachi number using recurion
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
terms = int(input("Enter the number of terms: "))

print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")
