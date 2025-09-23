def search(nums,target):
  high = len(nums) -1
  low = 0

  while low <=high:
    mid = (low+high) // 2

    if target > nums[mid]:
      low = mid + 1
    elif target < nums[mid]:
      high = mid - 1
    else:
      return mid
  return -1
  
#Example usage:
if __name__ == "__main__":
  nums1 = [-1,0,3,5,9,12]
  target1 = 9
  print(search(nums1,target1))  

  nums2 = [-1,0,3,5,9,12]
  target2 = 2
  print(search(nums2,target2))  

  nums3 = [5]
  target3 = 5
  print(search(nums3,target3))


    
