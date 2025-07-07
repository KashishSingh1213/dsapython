#solve the quesion of revese an array using recurion
#num=[5,7,3,2,6,1,5,9]

def reverse_array(arr, start, end):
    # Base case
    if start >= end:
        return
    # Swap elements
    arr[start], arr[end] = arr[end], arr[start]
    # Recursive call
    reverse_array(arr, start + 1, end - 1)

# Given array
num = [5, 7, 3, 2, 6, 1, 5, 9]

print("Original array:", num)

# Call the function
reverse_array(num, 0, len(num) - 1)

print("Reversed array:", num)



# num=[3,4,5,7,8,9]
def reverse_array(arr,start,end):
    if start>=end:
        return
        arr[start],arr[end]=arr[end],arr[start]
          reverse_array(arr, start + 1, end - 1)#call the function

          # Given array
 num=[3,4,5,7,8,9]
print("Original array:", num)

# Call the function
reverse_array(num, 0, len(num) - 1)

print("Reversed array:", num)
