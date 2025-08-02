# #find the largest numberin array
# nums=[55,32,97,99,3,67]
# def find_largest(nums):
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest

# print(find_largest(nums))


#find the second largest number in array
nums=[55,34,87,22,12]
def find_second_largest(nums):
    largest = second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
print(find_second_largest(nums))

#time complexity: O(n)
#space complexity: O(1)