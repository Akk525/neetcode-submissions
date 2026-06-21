class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i in range(len(nums)):
            cur_comp = target - nums[i]
            if cur_comp in complement:
                return [complement[cur_comp], i]
            complement[nums[i]] = i