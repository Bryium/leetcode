# This problem is all about removing duplicates from a sorted array in-place, while preserving the original order of unique elements.

class Solution:
  def removeDuplicates(self,nums):
    
    if not nums:
      return 0
    
    k = 1 #unique element

    for i in range(1, len(nums)):
         if nums[i] != nums[i -1]:
            nums[k] = nums[i]
            k += 1
    return k
  
#Example usage

if __name__ == "__main__":
  #Example 1

  nums = [1, 2, 3, 4, 4, 5,6,6,6,6, 6, 7, 7, 7, 8, 9, 10]
  solution = Solution()
 
  k = solution.removeDuplicates(nums)
  print("Number of unique elements:", k)
  print("Unique elements:", nums[:k])

  #Example 2
  nums = [0,0,1,1,1,2,2,3,3,4]
  k = solution.removeDuplicates(nums)   

  print("Number of unique elements:", k)
  print("Unique elements:", nums[:k])

  