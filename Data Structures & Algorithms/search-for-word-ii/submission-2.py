class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def insert(self, word, root) -> None:
        curr = root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = TrieNode()
        for word in words:
            trie.insert(word=word, root=trie)

        ans = set()

        def dfs(i, j, visited, curr, word=''):
            if i < 0 or j < 0 or len(board) == i or len(board[0]) == j or (i,j) in visited:
                return
            
            c = board[i][j]

            if c not in curr.children:
                return

            word += c
            curr = curr.children[c]

            if curr.word:
                nonlocal ans
                ans.add(word)

            

            

            visited.add((i,j))

            dfs(i + 1, j, visited, curr, word)
            dfs(i - 1, j, visited, curr, word)
            dfs(i, j + 1, visited, curr, word)
            dfs(i, j - 1, visited, curr, word)

            visited.remove((i,j))


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,set(), trie) 
        return list(ans)
