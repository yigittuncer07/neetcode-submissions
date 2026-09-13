class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i:set() for i in range(numCourses)}

        for course, pre in prerequisites:
            courses[course].add(pre)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not courses[course]:
                return True


            visited.add(course)
            for pre in courses[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            courses[course] = set()
            return True
        
        ans = True
        for i in range(numCourses):
            ans = ans and dfs(i)        
        return ans