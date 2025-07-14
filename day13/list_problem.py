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

