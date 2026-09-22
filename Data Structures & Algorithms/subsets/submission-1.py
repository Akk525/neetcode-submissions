class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            new_subset = []

            for subset in results:
                new_subset.append(subset + [num])
            results += new_subset
        return results