class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def add(start, cur_array, cur_total):
            if cur_total == target:
                return res.append(cur_array[:])
            elif cur_total > target:
                return
            
            for i in range(start, len(nums)):
                cur_array.append(nums[i])
                add(i, cur_array, cur_total + nums[i])
                cur_array.pop()
        add(0, [], 0)
        return res