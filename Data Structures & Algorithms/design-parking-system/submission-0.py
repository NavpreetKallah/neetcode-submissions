class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.counts = {1:0, 2:0, 3:0}
        self.maxes = {1:big, 2:medium, 3:small}

    def addCar(self, carType: int) -> bool:
        if self.counts[carType] < self.maxes[carType]:
            self.counts[carType] += 1
            return True
        return False   
