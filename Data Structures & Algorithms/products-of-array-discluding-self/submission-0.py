import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # pre = [1, 1, 2, 8]
        # post = [48, 24, 6, 1]
        # res = [48, 24, 12, 8]

        res = [1] * len(nums)

        # prefix pass
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # suffix pass
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res