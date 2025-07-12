#remove duplicate elements from an array
def remove_duplicates(arr): 
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
# Explanation:  
# The function remove_duplicates iterates through the input array and uses a set to track seen elements.
# If an element is not in the set, it is added to both the set and the result list.
# This ensures that only unique elements are included in the final result.

