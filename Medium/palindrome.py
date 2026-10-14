## This function finds the longest palindromic substring in a given string `s`. 
## Time complexity: O(n^2) where n is the length of the string.
## Space complexity: O(1) since we are using a constant amount of space.
## The algorithm uses a center expansion approach, where we expand around each character (and each pair of characters) to find palindromes.




class Solution:
    def longestPalindrome(self, s):
        best_start = 0
        best_length = 1

        for i in range(len(s)):

            # Odd-length palindromes, such as "radar".
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1

                if current_length > best_length:
                    best_start = left
                    best_length = current_length

                left -= 1
                right += 1

            # Even-length palindromes, such as "abba".
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1

                if current_length > best_length:
                    best_start = left
                    best_length = current_length

                left -= 1
                right += 1

        return s[best_start : best_start + best_length]

## example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s = "babad"
    result = solution.longestPalindrome(s)
    print(result) 

    # Example 2
    s = "cbbd"
    result = solution.longestPalindrome(s)
    print(result)  

    # Example 3
    s = "a"
    result = solution.longestPalindrome(s)
    print(result)  

    # Example 4
    s = "ac"
    result = solution.longestPalindrome(s)
    print(result)  

    # Example 5
    s = "racecar"
    result = solution.longestPalindrome(s)
    print(result)  
