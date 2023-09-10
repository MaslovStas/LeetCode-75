class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_key = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_key = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_key

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
param_2 = obj.search('word')
param_3 = obj.startsWith('wo')
print(param_3)
