class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            valid = strs[0][i]
            if not all(len(string) > i for string in strs) or not all(string[i] == valid for string in strs):
                return strs[0][0:i]
        return strs[0]