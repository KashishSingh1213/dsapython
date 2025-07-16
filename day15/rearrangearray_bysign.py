#rearrange array by sign
def rearrange_array(arr):
    positive = []
    negative = []
    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    # Rearrange the array by alternating positive and negative numbers
    rearranged = []
    i, j = 0, 0
    while i < len(positive) and j < len(negative):
        rearranged.append(positive[i])
        rearranged.append(negative[j])
        i += 1
        j += 1
    # Append any remaining elements from either list
    rearranged.extend(positive[i:])
    rearranged.extend(negative[j:])
    return rearranged

# Example usage
array = [1, -2, 3, -4, 5, -6]
result = rearrange_array(array)
print("Rearranged array:", result)



#solve another example of rearranging array by sign
def rearrange_array_by_sign(arr):
    positive = []
    negative = []
    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    # Rearrange the array by alternating positive and negative numbers
    rearranged = []
    i, j = 0, 0
    while i < len(positive) and j < len(negative):
        rearranged.append(positive[i])
        rearranged.append(negative[j])
        i += 1
        j += 1
    # Append any remaining elements from either list
    rearranged.extend(positive[i:])
    rearranged.extend(negative[j:])
    return rearranged
