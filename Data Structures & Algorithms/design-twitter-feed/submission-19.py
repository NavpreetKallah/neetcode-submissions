class Twitter:

    def __init__(self):
        self.time = 0
        self.userHeaps = {}
        self.userFollows = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userFollows:
            self.userFollows[userId] = set([userId])
        if userId not in self.userHeaps:
            self.userHeaps[userId] = []
        self.userHeaps[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        for followeeId in self.userFollows[userId]:
            if followeeId in self.userHeaps:
                index = len(self.userHeaps[followeeId]) - 1
                count, tweetId = self.userHeaps[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.userHeaps[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollows:
            self.userFollows[followerId] = set([followerId])
        self.userFollows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.userFollows[followerId].discard(followeeId)
        
