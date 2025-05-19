# You have an array called citations.
# Each element citations[i] tells you how many times the researcher’s ith paper has been cited.
# Your goal is to find the h-index, which means:
# The highest number h such that the researcher has at least h papers with h or more citations.

class Solution(object):
  def hIndex(self, citations):
    citations.sort(reverse=True)
    h = 0

    for i, c in enumerate(citations):
      if c >= i + 1:
        h = i + 1
      else:
        break
    return h
  

# Example Usage
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  citations = [3,0,6,1,5]
  print(solution.hIndex(citations))

   # Example 2
  citations = [1, 3, 1]
  print(solution.hIndex(citations))  

    # Example 3
  citations = [10, 8, 5, 4, 3]
  print(solution.hIndex(citations))  

    # Example 4
  citations = [0, 0, 0, 0]
  print(solution.hIndex(citations))  


  