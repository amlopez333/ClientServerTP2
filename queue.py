class Queue:

    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def getLength(self):
        return len(self.queue)
    def isEmpty(self):
        if(len(self.queue) > 0):
            return False
        return True
