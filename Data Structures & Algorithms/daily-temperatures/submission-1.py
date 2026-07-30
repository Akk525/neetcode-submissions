class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for left in range(n):
            right = left + 1

            while right < n and temperatures[right] <= temperatures[left]:
                right += 1

            if right < n:
                res[left] = right - left

        return res