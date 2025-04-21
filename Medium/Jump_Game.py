class Solution(object):
  def canJump(self, nums):
    
    farthest = 0

    for i in range(len(nums)):
      if i > farthest:
        return False
      farthest = max(farthest, i + nums[i])

    return True
  
#Example usage
if __name__ == "__main__":
  Solution = Solution()

  #Example 1
  nums = [2,3,1,1,4]
  can_Jump = Solution.canJump(nums)
  print(can_Jump) 

   #Example 2
  nums = [3, 2, 1, 0, 4]
  can_Jump = Solution.canJump(nums)
  print(can_Jump) 

   #Example 3
  nums = [2, 0, 2, 0, 1]
  can_Jump = Solution.canJump(nums)
  print(can_Jump) 

  #Example 4
  nums = [2, 4, 0, 1, 0, 2, 0]
  can_Jump = Solution.canJump(nums)
  print(can_Jump) 