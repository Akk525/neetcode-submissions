class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         counts = Counter(nums)
         sort = sorted(counts, key=counts.get, reverse=True)
         return sort[:k]
         