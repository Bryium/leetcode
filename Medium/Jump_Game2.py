# You're standing at the first index in an array called nums.
# The algorithm used here is a single-pass Greedy Algorithm.
# The time complexity and space complexity are O(n) and O(1) respectively.
# Each number in nums[i] tells you the maximum jump length from that position.
 # Your goal is to reach the last index using the minimum number of jumps.



class Solution(object):
    def jump(self, nums):

        n = len(nums)

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps



#Example usage
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  nums1 = [2,3,1,1,4]
  jump = solution.jump(nums1)
  print(jump) 

  #Example 2
  nums2 = [3,2,1,0,4]
  jump = solution.jump(nums2)
  print(jump) 

  #Example 3
  nums3 = [2,0,2,0,1]
  jump = solution.jump(nums3)
  print(jump)