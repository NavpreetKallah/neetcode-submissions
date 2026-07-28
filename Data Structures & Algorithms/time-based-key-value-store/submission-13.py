class TimeMap:

    """
    
    have a map of timestamps to maps
    have a map of key to timestamps

    if key is not in any timestamps it does not exist
    if a key is not in the current timestamp then check the timestamp before it


    
    """

    def __init__(self):
        self.timestampToMap = {}
        self.keyToTimestamp = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.timestampToMap:
            self.timestampToMap[timestamp] = {}

        timestampMap = self.timestampToMap[timestamp]
        timestampMap[key] = value
        if key not in self.keyToTimestamp:
            self.keyToTimestamp[key] = []
        self.keyToTimestamp[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyToTimestamp:
            return ""
        timestamps = self.keyToTimestamp[key]

        l = 0
        r = len(timestamps) - 1
        biggest = -1


        while l <= r:
            mid = (l + r) // 2

            if timestamps[mid] == timestamp:
                biggest = timestamp
                break

            elif timestamps[mid] > timestamp:
                r = mid - 1
            else:
                biggest = max(biggest, timestamps[mid])
                l = mid + 1

        if biggest != -1:
            return self.timestampToMap[biggest][key]
        else:
            return ""
        
