#charhashing
s = "hellohash"
hash_array = [0] * 26  # Initialize array of size 26 with 0

for char in s:
    index = ord(char) - ord('a')  # convert char to index (0-25)
    #🔹 index = ord(char) - ord('a')
 #ord(char) → kisi character ka ASCII value deta hai
#ord('a') → 97 hota hai
    hash_array[index] += 1

# Print frequency of each character
for i in range(26):
    if hash_array[i] > 0:
        print(f"{chr(i + ord('a'))} = {hash_array[i]}")



# Check if Two Strings are Anagrams
#"listen" and "silent"
def are_anagrams(str1, str2):
    # If lengths are not equal, can't be anagrams
    if len(str1) != len(str2):
        return False

    # Initialize hash arrays for character frequency (only lowercase a-z)
    freq1 = [0] * 26
    freq2 = [0] * 26

    # Count frequency of each character in str1
    for ch in str1:
        freq1[ord(ch) - ord('a')] += 1

    # Count frequency of each character in str2
    for ch in str2:
        freq2[ord(ch) - ord('a')] += 1

    # Compare both frequency arrays
    return freq1 == freq2


# Test the function
s1 = "listen"
s2 = "silent"

if are_anagrams(s1, s2):
    print(f'"{s1}" and "{s2}" are anagrams.')
else:
    print(f'"{s1}" and "{s2}" are NOT anagrams.')
