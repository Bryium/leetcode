# this problem is all about finding the maximum possible profit by buying the stock and selling it on the future day 
# The algorithm sed here is single-pass Greedy Algorithm


class Solution(object):
  def maxProfit(self,prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
      if price < min_price:
        min_price = price
      elif price - min_price > max_profit:
        max_profit = price - min_price

    return max_profit

#Example usage
if __name__ == "__main__":
  solution = Solution()

  #example 1
  num1 = [1,2,3,4,5]
  maximum_profit  = solution.maxProfit(num1)
  print(maximum_profit) 

  #example 2
  num2 = [3,5,6,7,8,9]
  maximum_profit  = solution.maxProfit(num2)
  print(maximum_profit) 

  #example 3
  nums3 = [7,6,3,2,1]
  maximum_profit = solution.maxProfit(nums3)
  print(maximum_profit)

