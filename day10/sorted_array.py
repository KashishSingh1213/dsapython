#check the array is sorted or not
num=[1,2,3,4,5,6,7,8,9]
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(is_sorted(num))  # Output: True

#check the array is not sorted
num2=[1,2,3,4,5,6,7,8,9,0]
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(is_sorted(num2))  # Output: False