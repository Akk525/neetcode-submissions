class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = max(1, (sum(piles) + h - 1) // h)
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            time_spent = 0

            for pile in piles:
                time_spent += (pile + mid - 1) // mid

            if time_spent <= h:
                right = mid
            else:
                left = mid + 1

        return left