#two sum
nums=[2, 7, 11, 15,12,4,2]
target=9
def two_sum(nums, target):  
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
print(two_sum(nums, target))  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)

# Explanation:
# The function two_sum uses a dictionary to store the indices of the numbers.
# It iterates through the list, calculating the complement for each number.