# This problem is all about finding the majority element — the one that appears more than n / 2 times in an array.

class Solution(object):
  def majorityElement(self, nums):

    #Initialize the candidate and count 

    candidate = None
    count = 0

    #Iterate over the array 
    for num in nums:
      if count == 0:
          candidate = num 
      count += (1 if num == candidate else -1)  

    return candidate
  

#  Example usage 
if __name__ == "__main__":
   solution = Solution()

   # Test case 1
   nums1 = [3,2,3]
   k = solution.majorityElement(nums1)
   print(f"majority element in {nums1} is: {k}")
 

   # Test case 2
   nums2 = [2,2,1,1,2,2]
   result2 = solution.majorityElement(nums2)
   print(f"majority element in {nums2} is: {result2}")

   # Test Case 3
   nums3 = [1,4,5,6,7,1,1,1,1]
   result3 = solution.majorityElement(nums3)
   print(f"majority element in {nums3}  is: {result3}")


