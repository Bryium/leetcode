def runningSum(nums):

  result = [nums[0]]

  for i in range(1, len(nums)):

    result.append(result[i - 1] + nums[i])

  return result

#Example usage:
if __name__ == "__main__":

  nums = [1,2,3,4,5]
  print(runningSum(nums))