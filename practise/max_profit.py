# Finding the most maximum difference between two elements in an array such that the larger element appears after the smaller element.

def maxprofit(prices):
  
  left = 0
  right = 1
  max_diff = 0

  while right < len(prices):
    if prices[left] < prices[right]:
      diff = prices[right] - prices[left]
      max_diff = max(max_diff, diff)
    else:
      left = right
    right += 1
  return max_diff

# Example usage:
if __name__ == "__main__":
  prices1 = [7,1,5,3,6,4]
  print(maxprofit(prices1))  

  prices2 = [7,6,4,3,1]
  print(maxprofit(prices2))  

  prices3 = [10,30,50,80,6,100]
  print(maxprofit(prices3))
    
