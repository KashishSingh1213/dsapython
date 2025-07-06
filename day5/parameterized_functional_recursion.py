#print sum of 1 to n
def param_rec(sum, i, n):
    if i > n:
        print("Sum:", sum)
        return
    param_rec(sum + i, i + 1, n)

param_rec(0, 1, 5)  # Sum of 1 to 5 = 15


#functional recursion
def get_numbers(i, n):
    if i > n:
        return []
    return [i] + get_numbers(i + 1, n)

result = get_numbers(1, 10)
print("Numbers from 1 to 10:", result)
