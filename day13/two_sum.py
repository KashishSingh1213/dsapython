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

# If the complement is found in the dictionary, it returns the indices of the two numbers.
# If no such pair exists, it returns an empty list.


# Example outputs:
# For nums = [2, 7, 11, 15, 12, 4, 2] and target = 9, the output is [0, 1] because nums[0] + nums[1] = 2 + 7 = 9.
# If the input is changed to nums = [1, 2, 3, 4] and target = 5, the output would be [1, 2] because nums[1] + nums[2] = 2 + 3 = 5.
# If no two numbers add up to the target, it returns an empty list.
# For example, if nums = [1, 2, 3] and target = 7, the output would be [] since no two numbers sum to 7.
# The function efficiently finds the indices of the two numbers that add up to the target using a single pass through the list.


#next example
# Example with no solution
nums2 = [1, 2, 3, 4]
target2 = 8
print(two_sum(nums2, target2))  # Output: [] (no two numbers sum to 8)
# Explanation:
# In this case, the function iterates through the list but finds no two numbers that add

# up to the target value of 8, so it returns an empty list.

#time complexity
# Time complexity: O(n)
#space complexity 
# Space complexity: O(n)

#another example 
nums3 = [3, 2, 4]
target3 = 6
print(two_sum(nums3, target3))  # Output: [1, 2] (because nums[1] + nums[2] = 2 + 4 = 6)
# Explanation:
# In this case, the function finds that nums[1] + nums[2] equals the target value of 6, so it returns the indices [1, 2].
#time complexity
# Time complexity: O(n)