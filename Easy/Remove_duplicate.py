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

  