from collections import defaultdict
class Node:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

class PriorityQueue(object):
    def __init__(self):
        self.queue = {}
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def put(self, key,value):
        self.queue[key]=value
 
    # for popping an element based on Priority
    def get(self):
        a=min(self.queue.keys())
        item={}
        item=[a,self.queue[a]]
        return item
