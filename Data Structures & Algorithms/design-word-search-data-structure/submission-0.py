class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur = cur.children[c]
        cur.ends = True

    def search(self, word: str) -> bool:
        def dfs(cur, word):
            if word=="":
                return cur.ends
            p = False
            if word[0] in cur.children:
                cur = cur.children[word[0]]
                return dfs(cur, word[1:])
            if "."==word[0]:
                for c in cur.children:
                    p = p or dfs(cur.children[c], word[1:])
                return p
            return False
        return dfs(self.root, word)


        
