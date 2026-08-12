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
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        userHeaps = [self.userHeaps[uid] for uid in (self.userFollows[userId]) if uid in self.userHeaps]
        userHeaps = [element for heap in userHeaps for element in heap]
        heapq.heapify_max(userHeaps)
        res = []
        while userHeaps and len(res) < 10:
            time, tweetId = heapq.heappop_max(userHeaps)
            res.append(tweetId)            
                
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollows:
            self.userFollows[followerId] = set([followerId])
        self.userFollows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.userFollows[followerId].discard(followeeId)
        
