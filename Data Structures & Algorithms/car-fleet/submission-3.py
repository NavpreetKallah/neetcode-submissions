class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars: List = [(position[i], speed[i]) for i in range(len(position))]

        cars.sort(reverse=True)

        for pos, speed in cars:
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= time:
                stack.pop()

        return len(stack)


