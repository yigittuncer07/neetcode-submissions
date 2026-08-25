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

        def search_from_root(node: Node, word, start_index) -> bool:
            
            curr = node
            for i in range(start_index, len(word)):
                if word[i] != ".":
                    if word[i] in curr.children:
                        curr = curr.children[word[i]]
                    else:
                        return False
                else:
                    for child in curr.children.values():
                        found = search_from_root(child, word, i + 1)
                        if found:
                            return True
                    return False
            return curr.word
        
        return search_from_root(self.root, word,0)

        

