## Longest Substring Without Repeating Characters
## Time complexity: O(n) where n is the length of the string.
## Space complexity: O(min(n, m)) where m is the size of the character set.
## the algorithm uses a sliding window approach with a set to keep track of characters in the current window.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        seen = set()
        left = 0
        max_length = 0
    

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    print("Length of the longest substring without repeating characters:", result)

    s = "abcbashfbhwknfmwibrdjmbww"
    result = solution.lengthOfLongestSubstring(s)
    print("Length of the longest substring without repeating characters:", result)