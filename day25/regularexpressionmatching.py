def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(2, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2] or (
                    (p[j-2] == '.' or p[j-2] == s[i-1]) and dp[i-1][j]
                )

    return dp[m][n]
# time complexity: O(m * n) where m is the length of s and n is the length of p
#space complexity: O(m * n) for the dp table used to store results of subproblems
def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (
                    (p[j - 2] == '.' or p[j - 2] == s[i - 1]) and dp[i - 1][j]
                )

    return dp[m][n]
# time complexity: O(m * n) where m is the length of s and n is the length of p
# space complexity: O(m * n) for the dp table used to store results of subproblems