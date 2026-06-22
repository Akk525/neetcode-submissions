class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        setMap = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            setMap[key].append(word)
        return list(setMap.values())