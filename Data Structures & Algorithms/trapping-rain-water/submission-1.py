class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        max_vol = 0
        left_vol = 0
        right_vol = 0

        while left < right:
            if height[left] <= height[right]:
                left_vol = max(left_vol, height[left])
                max_vol += left_vol - height[left]
                left += 1
            else:
                right_vol = max(right_vol, height[right])
                max_vol += right_vol - height[right]
                right -= 1
        return max_vol