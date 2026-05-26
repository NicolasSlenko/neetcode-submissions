class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:       
        self.time += 1
        self.tweets[userId].append((self.time+1,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetarr = []  
        tweetarr.extend(self.tweets.get(userId,[]))

        if userId in self.followees:
            for followeeId in self.followees[userId]:
                if followeeId in self.tweets:
                    tweetarr.extend(self.tweets[followeeId])
        
        heap = []
        
        for t in tweetarr:
            if len(heap) < 10:
                heapq.heappush(heap, t)
            else: 
                if t[0] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, t)
        heap.sort()
    
        return [tweetId for _, tweetId in heap][::-1]

    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees:
            self.followees[followerId].discard(followeeId)
    
        
