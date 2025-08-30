#maximum subarray sum
#using brute for solution
# Maximum Subarray Sum - Brute Force Solution
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)
maxi = float('-inf')  # Initialize with the lowest possible number

for i in range(n):
    total = 0
    for j in range(i, n):
        total += nums[j]
        maxi = max(maxi, total)

print("Maximum Subarray Sum (Brute Force):", maxi)

#solve in otimal solution
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n=len(nums)
maxi = float('-inf')  # Initialize with the lowest possible number
total = 0
for i in range(n):
    total += nums[i]
    maxi = max(maxi, total)
    if total < 0:
        total = 0
print("Maximum Subarray Sum (Optimal):", maxi)




def max_subarray_sum(arr):
    max_sum = arr[0]         # overall max sum
    current_sum = arr[0]     # sum till current index
    
    for i in range(1, len(arr)):
        # either extend the previous subarray or start new from current element
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray_sum(arr))
