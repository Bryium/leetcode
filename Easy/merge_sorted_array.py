# This problem is all about merging two sorted arrays into one sorted array.

from typing import List 

class Solution:
  def merge(self, nums1:list[int], m:int, nums2:list[int], n:int) -> None:

    p1 = m-1
    p2 = n-1
    p = m+n-1

    #Transverse both arrays from the back
    while p1 >=0 and p2 >=0:
      if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -=1
      else:
          nums1[p] = nums2[p2]
          p2 -=1
      p -= 1

    #Remaining elements in p2
    while p2 >=0:
      nums1[p] = nums2[p2]
      p2 -=1
      p -= 1


#Example usage:
if __name__ == "__main__":
    #Test Case 1
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution = Solution()
    solution.merge(nums1,m,nums2,n)
    print(nums1)

    #Test Case 2
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution = Solution()
    solution.merge(nums1,m,nums2,n)
    print(nums1)

    #Test case 3
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3 
    solution = Solution()
    solution.merge(nums1,m,nums2,n)
    print(nums1)





    
    