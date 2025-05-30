# Rain water problem 42

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


