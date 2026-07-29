class MinStack:

    def __init__(self):
        self.__min = []
        self.__stack = []
        

    def push(self, val: int) -> None:
        self.__min.append(min(self.__min[-1], val) if self.__min else val)
        self.__stack.append(val)

    def pop(self) -> None:
        self.__min.pop()
        return self.__stack.pop()        

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min[-1]
        
