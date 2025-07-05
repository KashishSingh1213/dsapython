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
