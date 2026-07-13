class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for val in counts:
            if counts[val] > 1:
                return val