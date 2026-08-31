class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []

        def backtrack(current, counter, stack_len):

            if counter == 0 and stack_len == 0:
                answer.append("".join(current))
                return

            if counter == 0:
                current.append(')')
                backtrack(current, counter, stack_len - 1)
                current.pop()
                return
            
            current.append('(')
            backtrack(current, counter - 1, stack_len + 1)

            current.pop()

            if stack_len:
                current.append(')')
                backtrack(current, counter, stack_len - 1)
                current.pop()

        backtrack([], n, 0)
        return answer

