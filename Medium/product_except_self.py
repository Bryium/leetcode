# Return an array where each element is the product of all other elements in the input array except itself, without using division and in linear time.
# The algorithm used here is the Prefix and Suffix Product Technique.
# The time complexity is O(n) and the space complexity is O(1).

class Solution(object):
  def productExceptSelf(self,nums):

    n = len(nums)
    answer = [1] * n

    left_product = 1
    for i in range(n):
      answer[i] = left_product
      left_product *= nums[i]

    right_product = 1
    for i in range(n-1,-1,-1):
      answer[i] *= right_product
      right_product *= nums[i]

    return answer
  
#Example usage
if __name__ =="__main__":
  solution = Solution()

  #Example 1
  nums = [1,2,3,4]
  product = solution.productExceptSelf(nums)
  print(product) 

  #Example 2
  nums = [5,6,7,4,8]
  product = solution.productExceptSelf(nums)
  print(product) 

  #Example 3
  nums = [5,6,3,9,8]
  product = solution.productExceptSelf(nums)
  print(product) 

  #Example 4
  nums = [1,2,3,4,5,6,7,8,9,10]
  product = solution.productExceptSelf(nums)
  print(product)






