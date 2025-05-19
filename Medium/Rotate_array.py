# This problem is all about rotating an array k times to the right — shifting elements toward the right and wrapping around the end back to the start.


class Solution():
  def rotate(self,nums,k):
    
    n = len(nums)

    k = k % n

    nums.reverse()

    nums[:k] = reversed(nums[:k])

    nums[k:] = reversed(nums[k:])

#Example usage
if __name__ == "__main__":
  solution = Solution()

  #Test Case 1
  nums = [1,2,3,4,5,6,7]
  k = 3
  solution.rotate(nums,k)
  print(nums) 

  #Test Case 2
  nums = [-1,-100,3,99]
  k = 2
  solution.rotate(nums,k)
  print(nums) 
