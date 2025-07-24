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
