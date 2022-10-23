class PriorityQueue(object):
    def __init__(self):
        # Tạo một priority Queue là một dictionary
        self.queue = {}
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # Kiểm tra xem queue có rỗng hay không
    def isEmpty(self):
        return len(self.queue) == 0
 
    # Chèn 1 phần tử vào queue, với key ~ priority
    def put(self, key, value):
        self.queue[key] = value
    
    # Xét độ ưu tiên, priority là nhỏ nhất thì pop phần tử ra ngoài 
    def pop(self):
        key = min(self.queue.keys())
        item = {}
        item = [key, self.queue[key]]
        self.queue.pop(key)
        return item

    # Trả về là các keys của queue ~ priotiry
    def keys(self):
        return self.queue.keys()
    
    # Trả về keys nhỏ nhất
    def min_keys(self):
        return min(self.queue.keys())
    
    # Trả về keys lớn nhất
    def max_keys(self):
        return max(self.queue.keys())

    # Trả về giá trị của phần tử lớn hơn key trong queue
    def upper_keys(self, key):
        for i in self.queue.keys():
            if i > key:
                return i
        # Trường hợp không có hoặc key rỗng sẽ trả về key
        return key