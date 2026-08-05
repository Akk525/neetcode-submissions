class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = max(1, (sum(piles) + h - 1) // h)
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            time_spent = 0

            for pile in piles:
                time_spent += (pile + mid - 1) // mid

                if time_spent > h:
                    break

            if time_spent > h:
                left = mid + 1
            else:
                right = mid

        return left