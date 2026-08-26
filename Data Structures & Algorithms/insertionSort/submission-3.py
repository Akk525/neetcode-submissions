# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        result = []
        
        for j in range(n):
            key = pairs[j]
            i = j - 1
            while i >= 0 and pairs[i].key > key.key:
                pairs[i + 1] = pairs[i]
                i -= 1
            pairs[i + 1] = key
            result.append(pairs.copy())

        return result