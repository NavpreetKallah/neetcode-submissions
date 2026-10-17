class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quicksort(l, r):
            if l >= r:
                return
            
            pivot = nums[(l + r) // 2]
            i, j = l, r
            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            quicksort(l, j)
            quicksort(i, r)

        quicksort(0, len(nums) - 1)
        