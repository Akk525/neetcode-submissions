class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        parents = {i : i for i in range(n)}

        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parents[rootx] = rooty
                return -1
            else:
                return 0
        
        for x,y in edges:
            res += union(x,y)
        return res