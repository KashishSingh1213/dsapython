#max consecuter ones
#find ones kitni bar a rha hai
nums= [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]
count = 0
max_count = 0

for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print("Max consecutive ones:", max_count)

#explantion
# The code iterates through the list of numbers and counts consecutive ones.s the actual sum to find the missing number.
# The function find_max_consecutive_ones counts the maximum number of consecutive ones in a binary array.s the actual sum to find the missing number.
# The function find_max_consecutive_ones counts the maximum number of consecutive ones in a binary array.

# Time complexity: O(n)
# Space complexity: O(1)