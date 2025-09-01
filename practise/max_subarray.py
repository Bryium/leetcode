# Given an array of integers (nums) and an integer k, 
# find the maximum sum of any contiguous subarray of length k.

from typing import List

def max_subarray(nums: List[int], k: int) -> int:
  if len(nums)< k:
    return 0
  
  current_sum = sum(nums[:k])
  max_sum = current_sum

  left, right = 0, k

  while right < len(nums):
    current_sum = current_sum - nums[left] + nums[right]

    max_sum = max(max_sum, current_sum)

    left += 1
    right += 1
  return max_sum

#Example usage:
if __name__ == "__main__": 
  nums1 = [1,2,3,4,5]
  k1 = 2
  print(max_subarray(nums1, k1))  

  nums2 = [2,1,5,1,3,2]
  k2 = 3
  print(max_subarray(nums2, k2))  

  nums3 = [1, -1, 5, -2, 3]
  k3 = 3
  print(max_subarray(nums3, k3))  