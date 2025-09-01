# Given a sorted array nums (non-decreasing, may contain negatives), return a new array with the squares of each number, sorted in non-decreasing order.

from typing import List

def sorted_squares(nums: List[int]) -> List[int]:

  left = 0
  right =len(nums) -1
  result = []

  while left <= right:
    if abs(nums[left]) > abs(nums[right]):
      result.append(nums[left] ** 2)
      left += 1
    else:
      result.append(nums[right] ** 2)
      right -= 1
  return result[::-1]

#Example usage:
if __name__ == "__main__":
  nums1 = [-4,-1,0,3,10]
  print(sorted_squares(nums1)) 

  nums2 = [-7,-3,2,3,11]
  print(sorted_squares(nums2)) 

