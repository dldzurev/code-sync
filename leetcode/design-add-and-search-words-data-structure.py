class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def dfs(self,curr,word):
        if not word:
            return curr.is_word
        if word[0] == ".":
            for child in curr.children.values():
                if self.dfs(child, word[1:]):
                    return True
            return False
        if word[0] not in curr.children:
            return False
        return self.dfs(curr.children[word[0]], word[1:])
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True
    def search(self, word: str) -> bool:
        curr = self.root
        for index,char in enumerate(word):
            if (char == "."):
                return self.dfs(curr,word[index:])
            elif char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)