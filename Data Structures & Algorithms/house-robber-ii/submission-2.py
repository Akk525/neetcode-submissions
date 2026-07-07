class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robbing(houses):
            prev1 = prev2 = 0
            for num in houses:
                tmp = max(prev1 + num, prev2)
                prev1 = prev2
                prev2 = tmp
            return prev2
        
        return max(robbing(nums[1:]), robbing(nums[:-1]))