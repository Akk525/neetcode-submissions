class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            new_subsets = []

            for subset in results:
                new_subsets.append(subset + [num])

            results += new_subsets

        return results