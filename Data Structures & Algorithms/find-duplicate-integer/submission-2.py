class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow is fast:
                break
            
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow is slow2:
                return slow
