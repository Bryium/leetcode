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






