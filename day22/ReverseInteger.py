#reverse integer
def reverse_integer(x: int) -> int:
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_x = 0
    while x != 0:
        digit = x % 10
        x //= 10
        reversed_x = reversed_x * 10 + digit
    reversed_x *= sign
    return reversed_x if -2**31 <= reversed_x <= 2**31 - 1 else 0

# Example usage
if __name__ == "__main__":
    print(reverse_integer(123))   # Output: 321
    print(reverse_integer(-123))  # Output: -321
    print(reverse_integer(120))   # Output: 21
    print(reverse_integer(0))     # Output: 0
    print(reverse_integer(1534236469))  # Output: 0 (out of bounds)
# Explanation
# The function reverses the digits of a given integer while preserving its sign.