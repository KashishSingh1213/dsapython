#method 1 to store the no.
nums = [1, 2, 4, 5, 3, 5, 7, 7, 1, 2, 3, 5]
freqmap = dict()

for i in range(len(nums)):
    if nums[i] in freqmap:
        freqmap[nums[i]] += 1
    else:
        freqmap[nums[i]] = 1

print("Frequency Map:", freqmap)


#method 2 to store the no.
# Using a dictionary as a HashMap to store frequency
nums = [1, 2, 4, 5, 3, 5, 7, 7, 1, 2, 3, 5]
hashmap = {}  # This is your HashMap

for num in nums:
    if num in hashmap:
        hashmap[num] += 1
    else:
        hashmap[num] = 1

print("Frequency using HashMap:",hashmap)
print("Frequency of 5:", hashmap.get(5, 0))  # Get frequency of 5, default to 0 if not found
