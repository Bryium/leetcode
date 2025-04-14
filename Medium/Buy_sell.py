class Solution(object):
  def maxProfit(self, prices):

    profit = 0
    for i in range(1, len(prices)):
      if prices[i] > prices[i-1]: #If today's price is higher than yesterday's
        profit += prices[i] - prices[i-1] # Capture the difference as profit 

    return profit
  
#Example usage
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  prices = [7,1,5,3,6,4]
  profit = solution.maxProfit(prices)
  print(profit)

  #Example 2
  prices = [1,2,3,4,5]
  profit = solution.maxProfit(prices)
  print(profit)

  #Example 3
  prices = [7,6,4,3,1]
  print(solution.maxProfit(prices))