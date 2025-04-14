class Solution(object):
  def jump(self, nums):

    n = len(nums)
    if n == 1:
      return 0 #Already at the last index
    

    jumps = 0 # Number of Jumps needed
    max_reach = 0  # the farthest index we can reach 
    end = 0 # The current jump boundary 

    for i in range(n -1):
      max_reach = max(max_reach, i + nums[i]) #update the farthest index


      if i == end:
        jumps +=1
        end = max_reach


        if end >= n -1:
          return jumps
        
    return jumps

# Example Usage
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  nums = [2,3,1,1,4]
  solution = Solution()
  print(solution.jump(nums))

  #Example 2
  nums = [4,5,6,3,5,]
  solution = Solution()
  print(solution.jump(nums))

  #Example 3
  nums = [3,7,3,5,6,4]
  solution = Solution()
  print(solution.jump(nums))

  #Example 4
  nums = [2,6,3,5,7,4]
  solution = Solution()
  print(solution.jump(nums))
            