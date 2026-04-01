# Rain water problem: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Time Complexity: O(n) where n is the number of bars in the elevation map  
# Space Complexity: O(1) as we are using only a constant amount of extra space for pointers and variables
# The algorithm uses two pointers to traverse the elevation map from both ends towards the center, calculating


class Solution(object):
  def trap(self, height):

    if not height or len(height) < 3:
      return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
      if height[left] < height[right]:
        left += 1
        left_max = max(left_max, height[left])
        water += left_max - height[left]
      else:
        right -= 1
        right_max = max(right_max, height[right])
        water += max(0, right_max - height[right])
    return water
  
#Example usage
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  height = [0,1,0,2,1,0,1,3,2,1,2,1]
  result = solution.trap(height)
  print(result) 

  #Example 2
  height = [4,2,0,3,2,5]
  result = solution.trap(height)
  print(result)  

  #Example 3
  height = [3,0,2,0,4]
  result = solution.trap(height)
  print(result)



