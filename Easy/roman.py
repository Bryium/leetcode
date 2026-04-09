# This code is for converting a Roman numeral string to an integer. The function `romanToInt` takes a string `s` as input and returns the corresponding integer value.
# The algorithm uses a dictionary to map Roman numeral characters to their integer values. It iterates through the string, checking if the current character represents a smaller value than the next character. If it does, it subtracts the value from the total; otherwise, it adds the value to the total. Finally, it returns the computed integer value.
# Time Complexity: O(n) where n is the length of the input string `s`
# Space Complexity: O(1) as the dictionary of Roman numerals is of constant size and we are using only a constant amount of extra space for variables.
# The algorithm here is  two-pass approach 


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        for i in range(len(s)):
            if i + 1  < len(s) and roman[s[i]] < roman[s[i  +1 ]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total
    
#Example usage
if __name__ == "__main__":  
    
    solution = Solution()

    #Example 1
    s = "III"
    result = solution.romanToInt(s)
    print(result) 

    #Example 2
    s = "LVIII"
    result = solution.romanToInt(s)
    print(result)  

    #Example 3
    s = "MCMXCIV"
    result = solution.romanToInt(s)
    print(result)
