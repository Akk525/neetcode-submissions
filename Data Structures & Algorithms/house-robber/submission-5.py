class Solution:
    def rob(self, nums: List[int]) -> int:
        max1 = max2 = 0
        n = len(nums)

        for i in range(n):
            tmp = max(max1 + nums[i], max2)
            max1 = max2
            max2 = tmp
        return max2