class Solution(object):
  def intoRoman(self, num):

    values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
    (1, "I")]

    result = ""

    for value,symbol in values:
      while num >= value:
        result += symbol
        num -= value
    return result
  

# example usahe 
if __name__ == "__main__":
  solution = Solution()

  #Example 1
  num = 3
  result = solution.intoRoman(num)
  print(result) 

  #Example 2
  num = 58
  result = solution.intoRoman(num)
  print(result)  

  #Example 3
  num = 1994
  result = solution.intoRoman(num)
  print(result)


