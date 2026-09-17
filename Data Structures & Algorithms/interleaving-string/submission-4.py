class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        hmap = {}
        def recurse(s1i, s2i, s3i):
            if s3i == len(s3) and s1i == len(s1) and s2i == len(s2):
                return True
            if s3i == len(s3):
                return False
            if (s1i, s2i) in hmap:
                return hmap[(s1i, s2i)]

            answer = False
            if s1i < len(s1): 
                if s1[s1i] == s3[s3i]:
                    answer = answer or recurse(s1i + 1, s2i, s3i + 1)   
            if s2i < len(s2):
                if s2[s2i] == s3[s3i]:
                    answer = answer or recurse(s1i, s2i + 1, s3i + 1)
            hmap[(s1i, s2i)] = answer
            return answer

        return recurse(0,0,0)

