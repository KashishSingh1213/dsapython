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