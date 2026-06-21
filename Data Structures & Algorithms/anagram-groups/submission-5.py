class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyMap = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            keyMap[key].append(word)
        return list(keyMap.values())