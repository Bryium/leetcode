def runningSum(nums):

  result = [nums[0]]

  for i in range(1, len(nums)):

    result.append(result[i - 1] + nums[i])

  return result

# Edge Cases:

# This code assumes nums is not empty. If nums is [], nums[0] will raise an error.
# A safe version would be:

def runningSumSafe(nums):

  if not nums:
    
    return[]
  result = [nums[0]]

  for num in nums[1:]:
    result.append(result[-1] + num)

  return result
  

#Example usage:
if __name__ == "__main__":

  nums = [1,2,3,4,5]
  print(runningSum(nums))