#linked_list.py
# Singly Linked List basic implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_front(self, data):
        """ Insert new node at front of list """
        new_node = Node(data)
        new_node.Next = self.head
        self.head = new_node
        
    def print_list(self):
        """ Print all elements in the list """
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.Next
        print("None")

if __name__=="__main__":
    ll = LinkedList()
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_front(30)
    ll.print_list()