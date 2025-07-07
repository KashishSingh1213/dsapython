#check the string is palindrome using loop
# s= nitin
def is_palindrome(s):
    # Get the length of the string
    n = len(s)
    
    # Loop through half of the string
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

# Example string
s = "nitin"

# Check and print result
if is_palindrome(s):
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")


#using recursion
def is_palindrome_recursive(s, start, end):
    # Base case: if start crosses end, it's a palindrome
    if start >= end:
        return True
    # If mismatch found, not a palindrome
    if s[start] != s[end]:
        return False
    # Recursive call
    return is_palindrome_recursive(s, start + 1, end - 1)

# Example string
s = "nitin"

# Call the function
if is_palindrome_recursive(s, 0, len(s) - 1):
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")
