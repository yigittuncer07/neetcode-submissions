class Node:
    def __init__(self, val: str = None, children = []):
        self.val = val
        self.children = {}
        self.word = False


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root.children

        for c in word:
            if c not in curr:
                curr[c] = Node(c)
                
            last_node = curr[c]
            curr = curr[c].children
        last_node.word = True
        



    def search(self, word: str) -> bool:
        curr = self.root.children

        for c in word:
            if c not in curr:
                return False
            last_node = curr[c]
            curr = curr[c].children

        return last_node.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root.children

        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c].children
        return True
        
        