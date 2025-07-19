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
<<<<<<< HEAD


#longest consecutive sequence using brute force
nums = [1, 99, 101, 98, 2, 5    , 99, 100]
max_length = 0

=======
# The output of each function is printed
# The output of each function is printed

#solve other example
nums = [100, 4, 200, 1, 3, 2]
max_length = 0
>>>>>>> 8ec3498cc91d29801439eea4769e3ef62b1b1a5a
for num in nums:
    current = num
    current_length = 1

    # Check next numbers in sequence
    while current + 1 in nums:
        current += 1
        current_length += 1

    max_length = max(max_length, current_length)

print("Longest consecutive sequence length (brute force):", max_length)
<<<<<<< HEAD
=======

#longest consecutive sequence using optimal solution
nums = [100, 4, 200, 1, 3, 2]
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

#solve another example
>>>>>>> 8ec3498cc91d29801439eea4769e3ef62b1b1a5a




#explation
# The brute force solution checks each number and counts how many consecutive numbers follow it.
# The optimal solution uses a set to check if a number is the start of a sequence,
# which reduces the time complexity significantly.
# The optimal solution has a time complexity of O(n) compared to the brute force O(n)
# solution.
# The output of each function is printed


# This code sets matrix elements to zero based on the presence of zeroes in the matrix.
# The brute force solution has a time complexity of O(m*n*(m+n)) and space