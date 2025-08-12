def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Width and height for current container
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Test the function
if __name__ == "__main__":
    # Example heights
    heights = [1,8,6,2,5,4,8,3,7]
    
    # Calculate the maximum area of water that can be contained
    result = maxArea(heights)
    
    print(f"The maximum area of water that can be contained is: {result}")

    # Test case 1
    heights1 = [1,1]    
    print("Test case 1 result:", maxArea(heights1))  # Expected: 1
    # Test case 2
    heights2 = [4,3,2,1,4]
    print("Test case 2 result:", maxArea(heights2))  # Expected: 16
    # Test case 3
    heights3 = [1,2,1]
    print("Test case 3 result:", maxArea(heights3))  # Expected: 2
    # Test case 4
    heights4 = [1,2,3,4,5]  
    print("Test case 4 result:", maxArea(heights4))  # Expected: 6
    # Test case 5
    heights5 = [5,4,3,2,1]
    print("Test case 5 result:", maxArea(heights5))  # Expected: 6
    # Test case 6
    heights6 = [1,3,2,5,4]
    print("Test case 6 result:", maxArea(heights6))  # Expected: 12

    #explanation
    # Time complexity: O(n)
    # Space complexity: O(1)
# The two-pointer technique is used to find the maximum area of water that can be contained between the lines represented by the heights.
# Selection sort is not applicable here as we are not sorting the array but finding the maximum area.
# Selection sort is not applicable here as we are not sorting the array but finding the maximum area.
# The two-pointer technique is efficient for this problem, allowing us to find the solution in linear time.