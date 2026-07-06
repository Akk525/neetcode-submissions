class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(nums):
            prev2 = prev1 = 0
            for money in nums:
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        return max(
            rob_line(nums[:-1]),  # don't rob last
            rob_line(nums[1:])    # don't rob first
        )