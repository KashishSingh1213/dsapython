def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
#time complexity: O(S) where S is the sum of all characters in all strings
# space complexity: O(1) since we are using a constant amount of space for the prefix variable