class Twitter:

    def __init__(self):
        self.posts = collections.defaultdict(list) 
        self.follow_map = collections.defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = self.posts[userId][-10:]
        for u_id in self.follow_map[userId]:
            candidates = candidates + self.posts[u_id][-10:]

        candidates.sort(key=lambda x: x[0], reverse=True)
        return [tweetId for _, tweetId in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)