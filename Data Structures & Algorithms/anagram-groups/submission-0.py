class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in anagramsDict.keys():
                anagramsDict[key] = [string]
            else:
                anagramsDict[key].append(string)
        return list(anagramsDict.values())
        