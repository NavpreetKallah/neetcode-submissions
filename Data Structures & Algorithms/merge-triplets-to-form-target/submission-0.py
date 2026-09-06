class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets = [triplet for triplet in triplets if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]]
        f1 = False
        f2 = False
        f3 = False
        for one, two, three in triplets:
            if one == target[0]:
                f1 = True
            if two == target[1]:
                f2 = True
            if three == target[2]:
                f3 = True
            if f1 and f2 and f3:
                return True
        return False