from typing import List

class Solution(object):
  def removeElement(self, nums, val):
    k = 0 
    for i in range(len(nums)):
      if nums[i] !=  val:
        nums[k] = nums[i] 
        k += 1 
    return k 
      

# example Usage:
if __name__=="__main__":
   # Example 1
   nums1 = [3,2,2,3]
   val1= 3
   solution = Solution()  
   k1 = solution.removeElement (nums1, val1)
   print("Number of elements not equal to val:" , k1)
   print("Modified nums:", nums1[:k1])


   # Example 2
   nums2 = [0, 1, 2, 2, 3, 0, 4 ,2]
   val2 = 0
   k2 = solution.removeElement(nums2, val2)
   print("\nNumber of Elements not equal to val:", k2)
   print("Modified nums:" , nums2[:k2])