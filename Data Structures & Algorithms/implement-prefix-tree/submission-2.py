class PrefixTree:

    def __init__(self):
        self.hmap = {}

    def insert(self, word: str) -> None:
        curr = self.hmap
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
            
        curr["Done"] = True

    def search(self, word: str) -> bool:
        curr = self.hmap
        for letter in word:
            if letter in curr:
                curr = curr[letter]
            else:
                return False
        if "Done" in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.hmap
        for letter in prefix:
            if letter in curr:
                curr = curr[letter]
            else:
                return False
        return True
        