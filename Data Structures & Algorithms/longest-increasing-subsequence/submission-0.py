class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def helper(A: List[int]):
            n = len(A)

            dp = [1] * n

            for i in range(n):
                for j in range(i):
                    if A[j] < A[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)
        
        return helper(nums)