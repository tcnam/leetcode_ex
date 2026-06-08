from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue: deque = deque()

    def ping(self, t: int) -> int:
        lower_t: int = t - 3000
        self.queue.append(t)
        while self.queue:
            if self.queue[0] < lower_t:
                self.queue.popleft()
            else:
                break
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)