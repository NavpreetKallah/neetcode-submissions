class Solution:

    """
    
    get maximum digit of num while left is maximum increase the curr
    
    
    we sort it into 98863
                    98368


    we sort it into 9931
                    1993

    """
    def maximumSwap(self, num: int) -> int:
        listNum = [int(digit) for digit in str(num)]
        sortedList = sorted(listNum, reverse=True)

        curr = 0
        while sortedList[curr] == listNum[curr] and curr < len(listNum) - 1:
            curr += 1
        
        if curr == len(listNum):
            return num

        lookingFor = sortedList[curr]

        right = len(listNum) - 1
        while listNum[right] != lookingFor and right > 0:
            right -= 1

        listNum[right], listNum[curr] = listNum[curr], listNum[right]

        return int("".join(map(str, listNum)))
