# queue.py
# Queue implementation using Python list

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        # Return front item without removing it
        if self.is_empty():
            return None
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
if __name__=="__main__":
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q.dequeue())
    print(q.peek())