class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parantheses_dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }



        for c in s:
            if c in list(parantheses_dict.values()):
                stack.append(c)
            else:
                if not stack:
                    return False
                elif stack.pop() != parantheses_dict[c]:
                    return False
        
        return len(stack) == 0
        