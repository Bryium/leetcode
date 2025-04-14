class Solution(object):
  def canJump(self, nums):

    max_reach = 0 
    for i in range(len(nums)):
      if i > max_reach:
        return False
      max_reach = max(max_reach, i + nums[i])
      if max_reach >= len(nums)- 1:
          return True
    return False
  

#Example Usage
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  nums = [2,3,1,1,4]
  jump = solution.canJump(nums)
  print(jump)

  #Example 2
  nums = [4,5,6,1,0,4]
  jump = solution.canJump(nums)
  print(jump)

   #Example 3
  nums = [3,2,1,0,4]
  jump = solution.canJump(nums)
  print(jump)