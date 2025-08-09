# longest palindrome substring

def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    start = 0
    max_length = 1

    def expand_around_center(left: int, right: int):
        nonlocal start, max_length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > max_length:
                start = left
                max_length = current_length
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)     # Odd length palindrome
        expand_around_center(i, i + 1) # Even length palindrome

    return s[start:start + max_length]
print("Longest palindrome substring:", longestPalindrome("babad"))  # Example usage
print("Longest palindrome substring:", longestPalindrome("cbbd"))    # Example usage

# explanation
# time complexity: O(n^2)
# space complexity: O(1)
# explanation: The algorithm checks all possible centers for palindromes and expands around them,
# leading to a quadratic time complexity. The space complexity is constant since we only use a few variables.
# Test cases
if __name__ == "__main__":
    # Test case 1
    print(longestPalindrome("babad"))  # Expected output: "bab" or "aba"

    # Test case 2
    print(longestPalindrome("cbbd"))   # Expected output: "bb"

    # Test case 3
    print(longestPalindrome("a"))      # Expected output: "a"

    # Test case 4
    print(longestPalindrome("ac"))     # Expected output: "a" or "c"
    # Test case 5
    print(longestPalindrome("racecar"))  # Expected output: "racecar"