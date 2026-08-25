class Node:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = Node()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:

        def search_from_root(node: Node, word) -> bool:
            
            curr = node
            for i, c in enumerate(word):
                if c != ".":
                    if c in curr.children:
                        curr = curr.children[c]
                    else:
                        return False
                else:
                    found = False
                    for child in curr.children.values():
                        found = found or search_from_root(child, word[i+1:])
                    return found
            return curr.word
        
        return search_from_root(self.root, word)

        

