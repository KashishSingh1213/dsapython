#search insert position
#all elemnts are arranged
#array is sorted in ascending order
nums=[1,3,4,5,8,9,14,15,19,20]
def search_insert(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low
printf("The target element %d should be inserted at index %d\n", 20, search_insert(nums,20))

#time complexity: O(log n)
#space complexity: O(1)



#another question for binary search
#ceil the floor of the array
nums=[3,4,4,4,8,9,9,10,12,12,14,15]
target = 8
floor=8
ceil=8
def search_floor_ceil(nums, target):
    low = 0
    high = len(nums) - 1
    floor = -1
    ceil = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid, mid  # Found both floor and ceil at the same index
        elif nums[mid] < target:
            floor = mid  # Update floor
            low = mid + 1
        else:
            ceil = mid  # Update ceil
            high = mid - 1
            
    return floor, ceil
print("The floor of the target element %d is at index %d and the ceil is at index %d" % (target, *search_floor_ceil(nums, target)))


#time complexity: O(log n)
#space complexity: O(1)


#optimal solution
def find_floor_and_ceil(arr, target):
    low, high = 0, len(arr) - 1
    floor_val, ceil_val = -1, -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid], arr[mid]  # Exact match is both floor and ceil
        elif arr[mid] < target:
            floor_val = arr[mid]
            low = mid + 1
        else:
            ceil_val = arr[mid]
            high = mid - 1

    return floor_val, ceil_val
