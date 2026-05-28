class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        post_fix = 1
        for i in range(len(nums)-2, -1, -1):
            post_fix *= nums[i+1]
            res[i] *= post_fix

        return res