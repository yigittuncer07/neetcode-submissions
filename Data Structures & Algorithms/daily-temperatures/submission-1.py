class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            depth = 0
            if stack and temp > stack[-1][0]:
                while stack and temp > stack[-1][0]:

                    val = stack.pop()
                    depth += 1
                    if val[1] != -1:
                        result[val[1]] = depth
                
                for _ in range(depth):
                    stack.append([-1,-1])


            stack.append((temp, i))
        
        return result