import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
"""
Data Structure where You add data in and remoe data out 
FIFO first in first out 
think of a line
first piece of data in the queque is the first piece out 
"""

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

#push 
    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1
#pop
    def dequeue(self):
        if self == 0:
            value = self.storage.remove_from_head()
            return value
        else: 
            return None

    def len(self):
        return self.size
