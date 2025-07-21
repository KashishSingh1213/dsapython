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
