class Solution:
    """
    
    Quicksort
    grab middle of the array 
    anything smaller put to left anything bigger to the right
    recursively perform quicksort on left and right

    5, 10, 2, 1, 3

    middle = 2
    left = 1
    right = 5, 10, 3

    middle = 10
    left = 5, 3

    middle = 3


    """
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(array):
            if len(array) < 2:
                return array
            middle = len(array) // 2
            middleElem = array[middle]
            left = []
            right = []
            for idx, num in enumerate(array):
                if idx == middle:
                    continue
                if num > middleElem:
                    right.append(num)
                else:
                    left.append(num)
            return quicksort(left) + [middleElem] + quicksort(right)
        return quicksort(nums)
