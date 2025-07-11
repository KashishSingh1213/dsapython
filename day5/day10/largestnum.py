#find the largest numberin array
nums=[55,32,97,99,3,67]
def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

print(find_largest(nums))
