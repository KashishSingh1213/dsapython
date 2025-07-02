#Time complexity
#three case's are in the time complexity
#1.best case  2.average case    3. worst case
#1. for checking best case the the tc is 2
age=90
if age >=80:
    print("super senior")
if age>=60 and age<80:
    print('senior')
if age >=24 and age<60:
    print("working")
if age>=16 and age<24:
    print("students")
else:
    print("child")

# checking the worst time complexity
#in the worst case the tc take time 5 
age=10
if age >=80:
    print("super senior")
if age>=60 and age<80:
    print('senior')
if age >=24 and age<60:
    print("working")
if age>=16 and age<24:
    print("students")
else:
    print("child")


#for average time:- best case + worst case / 2



# Python program for the above approach

# Function to count frequencies of array items
def countFreq(arr, n):
    freq = dict()
    
    # Traverse through array elements and
    # count frequencies
    for i in arr:
        if i not in freq:
            freq[i] = 0
        freq[i]+=1
        
    # Traverse through map and print frequencies
    for x in freq:
        print(x, freq[x])

# Driver Code

# Given array
arr =  [10, 20, 20, 10, 10, 20, 5, 20 ]
n = len(arr)

# Function Call
countFreq(arr, n)


#Finding the sum of array
def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

input_array = [1, 2, 3, 4, 5]
result = array_sum(input_array)
print(result)