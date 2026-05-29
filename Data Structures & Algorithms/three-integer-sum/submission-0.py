class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        results = []

        for i in range(len(sorted_nums)):
            cur_nums = sorted_nums[i]
            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                left_num = sorted_nums[left]
                right_num = sorted_nums[right]

                if left_num + right_num == -cur_nums:
                    if [cur_nums, left_num, right_num] not in results:
                        results.append([cur_nums, left_num, right_num])
                    left += 1
                    right -= 1
                elif left_num + right_num < -cur_nums:
                    left += 1
                else:
                    right -= 1
        return results
            