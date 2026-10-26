class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i:[] for i in range(numCourses)}
        visited = set()
        for i,j in prerequisites:
            courses[i].append(j)
        
        def dfs(crs):
            if crs in visited:
                return False
            elif len(courses[crs])==0:
                return True
            visited.add(crs)
            for item in courses[crs]:
                if not dfs(item): return False
            visited.remove(crs)
            courses[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True
        