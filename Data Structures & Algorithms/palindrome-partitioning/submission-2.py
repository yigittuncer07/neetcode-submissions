class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        global_ans = []


        def backtrack(i, j, current_ans=[]):
            if i == j + 1:
                global_ans.append(current_ans.copy())
                return

            current = []

            for n in range(i, j + 1, 1):
                current.append(s[n])
                if self._is_palindrome(current):
                    current_ans.append("".join(current))
                    backtrack(n + 1, j, current_ans)
                    current_ans.pop()
        
        backtrack(0, len(s) - 1)

        return global_ans
    
    def _is_palindrome(self, s: List[str]) -> bool:
        return s == s[::-1]