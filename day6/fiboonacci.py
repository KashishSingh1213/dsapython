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

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
terms = int(input("Enter the number of terms: "))

print("Fibonacci sequence (recursive):")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()

print("Fibonacci sequence (iterative):")
for i in range(terms):
    print(fibonacci_iterative(i), end=" ")
print()
