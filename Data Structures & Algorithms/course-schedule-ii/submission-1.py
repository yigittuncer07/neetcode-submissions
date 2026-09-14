class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        a_s = {i:set() for i in range(numCourses)}

        for course, pre in prerequisites:
            a_s[course].add(pre)

        answer = []
        visited = set()

        def dfs(course):

            if not a_s[course]:
                answer.append(course)
                return True

            if course in visited:
                return False

            res = True
            visited.add(course)
            for pre in a_s[course]:
                res = res and dfs(pre)
                if not res:
                    return False
            a_s[course] = set()
            answer.append(course)
            visited.remove(course)


            return res

        res = True
        for i in range(numCourses):
            res = res and dfs(i)
        
        if res:
            return list(dict.fromkeys(answer))
        else:
            return []
