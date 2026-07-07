class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        n = len(edges)
        parents = {i : i for i in range(1, n + 1)}
        
        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parents[rootx] = rooty
                return []

            return [x, y]
        
        for x,y in edges:
            tmp = union(x, y)
            if tmp:
                res = tmp
        
        return res