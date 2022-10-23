class PriorityQueue(object):
    def __init__(self):
        self.queue = {}
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def put(self, key, value):
        self.queue[key] = value
    
    # for popping an element based on Priority
    def pop(self):
        key = min(self.queue.keys())
        item = {}
        item = [key, self.queue[key]]
        self.queue.pop(key)
        return item

    def keys(self):
        return self.queue.keys()
    
    def min_keys(self):
        return min(self.queue.keys())
    
    def max_keys(self):
        return max(self.queue.keys())

    def upper_keys(self, key):
        for i in self.queue.keys():
            if i > key:
                return i
        return 0