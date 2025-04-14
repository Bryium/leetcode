# this problem is all about finding the maximum possible profit by buying the stock and selling it on the future day 


class Solution(object):
  def maxProfit(self, prices):

    #initialize variables
    min_price = float("inf") # set intial minimum price to infinity
    max_profit =0 # set initial max profit to 0

    #lopp through the prices
    for price in prices:
      #update min_price if a lower price is found
      if price < min_price:
        min_price = price

      #calculate potenetial profit and update max_profit if it's higher
      elif price - min_price > max_profit:
        max_profit = price - min_price

    return max_profit # return maximum profit found
  

# Example usage
if __name__ == "__main__":
  solution = Solution()

  # Example 1
  prices = [7,1,5,3,6,4]
  profit = solution.maxProfit(prices)
  print(profit)


  # Example 2
  prices = [7,6,4,3,2,1]
  profit = solution.maxProfit(prices)
  print(profit)

  # Example 3
  prices = [8,3,4,3,2,1]
  profit = solution.maxProfit(prices)
  print(profit)