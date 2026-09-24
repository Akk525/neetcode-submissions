class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binarySearch(l, r):
            if l == r:
                return l
            mid = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                return binarySearch(l, mid)
            return binarySearch(mid + 1, r)
        return binarySearch(0, len(nums) - 1)