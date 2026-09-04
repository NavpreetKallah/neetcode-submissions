class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        for card in sorted(counts.keys()):
            needed = counts[card]
            if needed > 0:
                for i in range(groupSize):
                    if counts[card + i] < needed:
                        return False
                    counts[card + i] -= needed
        return True
        
                
