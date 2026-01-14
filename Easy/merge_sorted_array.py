# This problem is all about merging two sorted arrays into one sorted array.
# The algorithm used here is two-pointer technique
# Time Complexity: O(m+n) each element from both arrays is processed once
# Space Complexity: O(1) no need for extra space as we are modifying nums1 in place



from typing import List 

class Solution:
  def merge(self, nums1:list[int], m:int, nums2:list[int], n:int) -> None:

    p1 = m-1 #last valid element in nums1
    p2 = n-1 #last valid element in nums2
    p = m+n-1 #last position in nums1

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

    #Test case 4
    nums1 = [1,2,3,5,7,8,0,0,0]
    m = 6
    nums2 = [2,5,6]
    n = 3 
    solution = Solution()
    solution.merge(nums1,m,nums2,n)
    print(nums1)

    #Test case 5
    nums1 = [34,67,76,78,94,0,0,0,0]
    m = 5
    nums2 = [20,30,45,70]
    n = 4
    solution = Solution()
    solution.merge(nums1,m,nums2,n)
    print(nums1)

    #Test case 6 - Example with strings/letters (works the same way!)
    # Note: The type hints say int, but the algorithm logic works with any comparable type
    # nums1_str = ['a', 'c', 'e', '', '', '']
    # m_str = 3
    # nums2_str = ['b', 'd', 'f']
    # n_str = 3
    # solution.merge(nums1_str, m_str, nums2_str, n_str)  # Would produce: ['a', 'b', 'c', 'd', 'e', 'f']





    
    