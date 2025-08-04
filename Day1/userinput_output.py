x = input("enter your name: ")
print("hello", x)

# This code takes user input and prints a greeting message.
x= input("enter your age")
print("age",+x)

x= input("enter your city")
print("city",x)

# This code takes user input for name, age, and city, and prints a message for each.
# This code sets matrix elements to zero based on the presence of zeroes in the matrix.

age = int(input("Enter your age: "))
print("Age:", age)
if age >= 16 and age < 24:
    print("students")
else:
    print("child")

#for average time:- best case + worst case / 2
# Python program for the above approach
# Function to count frequencies of array items
def countFreq(arr, n):
    freq = dict()
    
    # Traverse through array elements and count frequencies
    for i in arr:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
        
    # Traverse through map and print frequencies
    for x in freq:
        print(x, freq[x])
# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3]
    n = len(arr)
    countFreq(arr, n)
    