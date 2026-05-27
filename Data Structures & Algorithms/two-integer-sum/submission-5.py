class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
            
        for i, n in enumerate(nums):
            diff = target - n
            if diff in index:
                return sorted([i, index[diff]])
            index[n] = i
            