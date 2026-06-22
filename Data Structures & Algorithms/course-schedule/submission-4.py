class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prevMap[course] == []:
                return True
            
            visited.add(course)

            for pre in prevMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True