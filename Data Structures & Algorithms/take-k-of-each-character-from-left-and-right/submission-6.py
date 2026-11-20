class Solution:
    """
    
    if we have a sliding window of size k up to n starting at the start
    if we then wrap around and go back we can count the amount of items within
    
    """
    def validate(self, counts):
        if (counts["a"] <= self.cs["a"] - self.k and
           counts["b"] <= self.cs["b"] - self.k and
           counts["c"] <= self.cs["c"] - self.k):
            return True

    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        self.cs = Counter(s)
        self.k = k
        for key in "abc":
            if self.cs[key] < k:
                return -1


        l = r = 0
        max_window = 0
        counts = {"a": 0, "b": 0, "c": 0}
        while r < len(s):
            counts[s[r]] += 1
            r += 1

            while not self.validate(counts):
                counts[s[l]] -= 1
                l += 1

            max_window = max(r - l, max_window)
        return len(s) - max_window


        

            
