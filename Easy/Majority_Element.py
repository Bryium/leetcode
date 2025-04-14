class Solution(object):
  def majorityElement(self, nums):

    #Initialize the candidate and count 

    candidate = None
    count = 0

    #Iterate over the array 
    for num in nums:
      if count == 0:
          candidate = num # set the new candidate
      count += (1 if num == candidate else -1)  # Increent or decrement the count 

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

# for older version sof python 

# Example usage
# if __name__ == "__main__":
#     solution = Solution()

#     # Test case 1
#     nums1 = [3, 2, 3]
#     result1 = solution.majorityElement(nums1)
#     print("Majority element in " + str(nums1) + " is: " + str(result1))

#     # Test case 2
#     nums2 = [2, 2, 1, 1, 2, 2]
#     result2 = solution.majorityElement(nums2)
#     print("Majority element in " + str(nums2) + " is: " + str(result2))
