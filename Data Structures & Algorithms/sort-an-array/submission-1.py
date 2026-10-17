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
        def quicksort(l, r):
            if l >= r:
                return

            middle = (l + r) // 2
            middleElem = nums[middle]
            i, j = l, r
            while i <= j:
                while nums[i] < middleElem:
                    i+= 1
                while nums[j] > middleElem:
                    j-= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            quicksort(l, j)
            quicksort(i, r)

        quicksort(0, len(nums) - 1)
        return nums
            
