class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def steps(n):
            if n in memo: return memo[n]
            if n == 1: return 1
            if n == 2: return 2
            res = steps(n - 1) + steps(n - 2)
            memo[n] = res
            return res
        return steps(n)