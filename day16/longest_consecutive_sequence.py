#longest consecutive sequence
nums = [1, 99, 101, 98, 2, 5, 99, 100]
max_length = 0

for num in nums:
    current = num
    current_length = 1

    # Check next numbers in sequence
    while current + 1 in nums:
        current += 1
        current_length += 1

    max_length = max(max_length, current_length)

print("Longest consecutive sequence length (brute force):", max_length)

#longest consecutive sequence using optimal solution
nums = [1, 99, 101, 98, 2, 5, 99, 100]
num_set = set(nums)
max_length = 0

for num in num_set:
    if num - 1 not in num_set:  # Check if it's the start of a sequence
        current = num
        current_length = 1

        while current + 1 in num_set:
            current += 1
            current_length += 1

        max_length = max(max_length, current_length)

print("Longest consecutive sequence length (optimal):", max_length)
# The output of each function is printed
# The output of each function is printed