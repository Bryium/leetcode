# This problem is about modifying a sorted array in-place so that each element appears at most twice, while keeping their original order.
# The algorithm used here is the Two-Pointer Technique.
# The time complexity is O(n) and the space complexity is O(1).

class Solution():
  def removeDuplicates(self, nums):
    if len(nums) <= 2:
      return len(nums)
    
    k = 2 #unique element 

    for i in range(2, len(nums)):
      if nums[i] != nums[k - 2]:
        nums[k] = nums[i]
        k += 1

    return k
  
# Example Usage
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  nums = [1,1,1,2,2,3]
  k = solution.removeDuplicates(nums)
  print("Number of unique elements:", k)
  print("Unique elements:", nums[:k])

  #Example 2
  nums = [1,1,1,2,2,3,4,5]
  k = solution.removeDuplicates(nums)
  print("Number of unique elements:", k)
  print("Unique elements:", nums[:k])

  #Example 3
  nums = [1,1,1,2,2,3,4,4,4,6,7,8,9]
  k = solution.removeDuplicates(nums)
  print("Number of unique elements:", k)
  print("Unique elements:", nums[:k])
