# lets take the example of prime factore
n = 10
print("Factors of", n, "are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# the question is n=20
n=20
print("factors n is",n)

for i in range(1,n+1):
    if n%i==0:
        print(i)