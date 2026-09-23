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