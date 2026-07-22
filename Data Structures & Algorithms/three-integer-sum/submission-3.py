class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = set()
        print(nums)
        
        for index1, num1 in enumerate(nums):
            if index1 > 0 and num1 == nums[index1 - 1]:
                continue

            target = -num1

            index2 = index1 + 1
            index3 = len(nums) - 1

            while index2 < index3:
                if index1 == 1:
                    print(index2, index3)
                num2 = nums[index2]
                num3 = nums[index3]
                if num2 + num3 == target:
                    answers.add((num1, num2, num3))
                    index2 += 1
                elif num2 + num3 < target:
                    index2 +=1
                else:
                    index3 -=1
        return list(answers)
        

