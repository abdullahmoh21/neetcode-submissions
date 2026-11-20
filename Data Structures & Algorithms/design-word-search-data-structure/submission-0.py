class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True
        
    def _search(self, node, word, i):
        for j, c in enumerate(word[i:], start=i):   # j is now the real index
            # handle *
            if c == ".":
                for child in node.keys():
                    if child == "$":                 # skip end marker
                        continue
                    if self._search(node[child], word, j + 1):   # resume after the dot
                        return True
                return False
                
            if c not in node:
                return False

            node = node.get(c)

        return node.get("$", False)

    def search(self, word: str) -> bool:
        return self._search(self.root, word, 0)


