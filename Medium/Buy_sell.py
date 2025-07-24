# This problem is all about finding the maximum possible profit by buying the stock on one day and selling it on a future day. 

class Solution(object):
  def maxProfit(self, prices):

    max_profit = 0

    for i in range(1, len(prices)):
      if  prices[i] > prices[i-1]:
        max_profit += prices[i] - prices[i-1]
    return max_profit
  
#Example Usage 
if __name__ ==  "__main__":
  solution  =  Solution()

  #example 1
  price1 = [1,2,3,4,5]
  maximum_profit = solution.maxProfit(price1)   
  print(maximum_profit)

  #example 3
  price2 = [7,6,4,3,1]
  maximum_profit = solution.maxProfit(price2)   
  print(maximum_profit)

  #example 3
  price3 = [7,1,5,3,6,4]
  maximum_profit= solution.maxProfit(price3)
  print(maximum_profit)

