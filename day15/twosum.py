#two sum problem in python
nums=[5,9,1,2,4,15,6,3]
target=13
n=len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print("Indices:", i, j)
            print("Numbers:", nums[i], nums[j])
            
        

            
