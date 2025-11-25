# This problem is about Finding two numbers in the list whose sum equals the target and return their indices.
# The algorithm used here is Hash Map for constant time look-up.
# Time Complexity: O(n) we traverse the list only once  
# Space Complexity: O(n) for storing elements in the hash map

class Solution(object):
    def twoSum(self, nums, target):

      seen = {}

      for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
          return [seen[complement], i]

        seen[num] = i

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(result1)  

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(result2)  