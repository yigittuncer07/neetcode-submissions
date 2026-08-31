class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if not digits:
            return answer

        num_to_chars = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        def backtrack(current = [], index = 0):
            if index == len(digits):
                answer.append("".join(current))
                return

            for c in num_to_chars[int(digits[index])]:
                current.append(c)
                backtrack(current, index + 1)
                current.pop()

        backtrack()

        return answer