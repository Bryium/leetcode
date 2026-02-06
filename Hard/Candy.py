# Distribute candies to children so that each child has at least one candy and children with higher ratings than their neighbors get more candies, while minimizing the total candies given.
# Time Complexity: O(n) where n is the number of children
# Space Complexity: O(n) where n is the number of children
# The algorithm used here is a two-pass approach to ensure that each child has at least one candy and children with higher ratings than their neighbors get more candies.

class Solution(object):
  def candy(self, ratings):

    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
      if ratings [i] >  ratings [ i -1]:
        candies[i] = candies[i -1] + 1

    for i in range(n-2, -1, -1):
        if ratings [i] > ratings [ i + 1]:
          candies[ i ] = max(candies[i], candies[i +1] + 1)

    return sum(candies)
  
#Example usage
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  ratings = [1,0,2]
  result = solution.candy(ratings)
  print(result) 

  #Example 2
  ratings = [1,2,2]
  result = solution.candy(ratings)
  print(result) 

  #Example 3
  ratings = [1, 3, 4, 5, 2]
  result = solution.candy(ratings)
  print(result) 

  #Example 4
  ratings = [1,3,2,1]
  result = solution.candy(ratings)
  print(result) 
