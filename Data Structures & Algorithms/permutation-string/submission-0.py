class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_hash = Counter(s1)
        left = 0

        for right in range(window_size - 1, len(s2)):
            print(right, s2[left:right+1])
            if Counter(s2[left:right+1]) == s1_hash:
                return True
            left += 1
        return False