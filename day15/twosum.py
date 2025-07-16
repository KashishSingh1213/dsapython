#two sum problem in python
#using brute force approach
nums=[5,9,1,2,4,15,6,3]
target=13
n=len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print("Indices:", i, j)
            print("Numbers:", nums[i], nums[j])

        
#two sum problem in python using optimal soutions
nums=[5,9,1,2,4,15,6,3]
n=len(nums)
target=13
hash_map={}
for i in range(0,n):
    remaining=target-nums[i]
    if remaining in hash_map:
        print("Indices:", hash_map[remaining], i)
        print("Numbers:", nums[hash_map[remaining]], nums[i])
    
# The output of each function is printed
            
