#hashing
n = [5, 6, 4, 3, 3, 5, 6, 2, 2, 1, 1, 10]
m = [10, 10, 5, 4, 3, 4, 3, 4, 5, 5, 1]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(f"{num} occurs {count} times in n")
#tc=o(n*m)
#sc=o(1)