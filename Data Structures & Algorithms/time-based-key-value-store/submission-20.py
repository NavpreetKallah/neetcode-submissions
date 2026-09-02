class TimeMap:

    """
    
    have a map of timestamps to maps
    have a map of key to timestamps

    if key is not in any timestamps it does not exist
    if a key is not in the current timestamp then check the timestamp before it

    This works though try to optimise for space next time
    
    """

    def __init__(self):
        self.kToT = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kToT:
            self.kToT[key] = []
        self.kToT[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kToT:
            return ""
        values = self.kToT[key]
        l = 0
        r = len(values) - 1
        biggest = -1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                l = mid + 1
                biggest = mid
            else:
                r = mid - 1
        return values[biggest][1] if biggest != -1 else ""
