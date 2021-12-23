class MinQueue:
    def __init__(self):
        self.queue = deque()
        self.minQueueHelper = deque()

    def enque(self, val):
        # if the value we are inserting is lower than the end of our
        # minQueueHelper, we can remove those elements since they 
        # can no longer ever be the min
        while len(self.minQueueHelper) > 0 and self.minQueueHelper[-1] > val:
            self.minQueueHelper.pop()
            
        self.minQueueHelper.append(val)
        self.queue.append(val)
    
    def deque(self):
        val = self.queue[0]
        self.queue.popleft()
        
        if val == self.minQueueHelper[0]:
            self.minQueueHelper.popleft()
       
    def get_min(self):
        return self.minQueueHelper[0]
    
class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.minQueueHelper = deque()

    def enque(self, val):
        # if the value we are inserting is lower than the end of our
        # minQueueHelper, we can remove those elements since they 
        # can no longer ever be the min
        while len(self.minQueueHelper) > 0 and self.minQueueHelper[-1] < val:
            self.minQueueHelper.pop()
            
        self.minQueueHelper.append(val)
        self.queue.append(val)
    
    def deque(self):
        val = self.queue[0]
        self.queue.popleft()
        
        if val == self.minQueueHelper[0]:
            self.minQueueHelper.popleft()
       
    def get_max(self):
        return self.minQueueHelper[0]