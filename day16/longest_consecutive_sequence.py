#longest consecutive sequence
nums=[1,99,101,98,2,5,99,100]
n=len(nums)
max_length=0
#longest consecutive sequence using brute force approach
for i in range(0,n):
    current_length=1
    for j in range(i+1,n):
        if nums[j]==nums[i]+current_length:
            current_length+=1
    max_length=max(max_length,current_length)
print("Longest consecutive sequence length (brute force):", max_length)
