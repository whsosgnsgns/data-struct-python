# stack.py
# Stack implementation using Python list

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, items):
        # Insert item on top of stack
        self.items.append(items)
    
    def pop(self):
        # Remove and return top item of stack
        if self.is_empty():
            return self.items.pop()
        
    def peek(self):
        # Return top item without removing it
        if self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)

if __name__=="__manin__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())