def is_Palindorome(s: str) -> bool:

  left = 0
  right = len(s) - 1

  while left <= right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1

  return True 

#Example usage:
if __name__ == "__main__":
  s1 = "racecar"
  print(is_Palindorome(s1))  

  s2 = "hello"
  print(is_Palindorome(s2)) 
  
  s3 = "madam"
  print(is_Palindorome(s3))