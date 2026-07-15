class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = set()

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            longest = max(longest, right - left + 1)

        return longest