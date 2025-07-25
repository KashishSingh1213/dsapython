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
