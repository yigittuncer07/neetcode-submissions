class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_COUNT = len(board)
        COL_COUNT = len(board[0])
        WORD_LEN = len(word)

        def dfs(i, j, word_index, visited = set()) -> bool:
            if i == ROW_COUNT or i == -1 or j == COL_COUNT or j == -1 or (i,j) in visited:
                return False

            cur = board[i][j]

            if cur != word[word_index]:
                return False
            
            if word_index == WORD_LEN - 1:
                return True

            visited = visited.copy()
            visited.add((i,j))
            

            return dfs(i + 1, j, word_index + 1, visited) or dfs(i - 1, j, word_index + 1, visited) or dfs(i, j + 1, word_index + 1, visited) or dfs(i, j - 1, word_index + 1, visited)
        
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                res = dfs(i,j,0)
                if res:
                    return True
        return False
        


        