class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in charSet:
                left = max(charSet[s[right]] + 1, left)
            charSet[s[right]] = right
            result = max(result, right - left + 1)
        return result