class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)
        
        visitedSet = set()

        def dfs(course):
            if course in visitedSet:
                return False
            if prevMap[course] == []:
                return True
            visitedSet.add(course)
            for pre in prevMap[course]:
                if not dfs(pre):
                    return False
            visitedSet.remove(course)
            prevMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True