class Solution(object):
  def hIndex(self, citations):

    citations.sort(reverse=True) #sort citations in descending order
    h_index = 0

    for i, citation in enumerate(citations):
      if citation >= i + 1:
        h_index = i + 1 #update h-iindex

      else:
        break # stop when the condition is met


    return h_index
  

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


  