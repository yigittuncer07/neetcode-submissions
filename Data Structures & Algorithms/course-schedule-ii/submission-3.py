class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        a_s = {i:set() for i in range(numCourses)}

        for course, pre in prerequisites:
            a_s[course].add(pre)

        answer = []
        visited = set()
        cycle = set()

        def dfs(course):

            if course in cycle:
                return False

            if course in visited:
                return True

            visited.add(course)
            cycle.add(course)
            for pre in a_s[course]:
                if not dfs(pre):
                    return False

            answer.append(course)
            cycle.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return answer