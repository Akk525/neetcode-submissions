class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lvol = rvol = vol = 0

        while left < right:
            if height[left] <= height[right]:
                lvol = max(lvol, height[left])
                vol += lvol - height[left]
                left += 1
            else:
                rvol = max(rvol, height[right])
                vol += rvol - height[right]
                right -= 1
        return vol