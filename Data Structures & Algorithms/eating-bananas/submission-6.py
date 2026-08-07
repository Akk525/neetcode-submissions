class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (right + left) // 2
            cur_time = 0

            for pile in piles:
                cur_time += math.ceil(pile / mid)

            if cur_time <= h:
                right = mid
            else:
                left = mid + 1
        return left