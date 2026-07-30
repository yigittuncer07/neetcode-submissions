class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position,speed))
        pairs.sort(key=lambda x: x[0], reverse=True)

        stack = []

        for car2 in pairs:
            car1 = stack[-1] if stack else None
            if stack and ((target - car1[0]) / car1[1]) >= ((target - car2[0]) / car2[1]):
                continue

            stack.append(car2)
        
        return len(stack)
