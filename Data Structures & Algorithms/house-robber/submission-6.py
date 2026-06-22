class Solution:
    def rob(self, nums: List[int]) -> int:
        max1 = max2 = 0

        for num in nums:
            tmp = max(max2, max1 + num)
            max1 = max2
            max2 = tmp
        return max2
