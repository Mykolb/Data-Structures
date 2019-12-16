import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

"""
LIFO data structure 
-> last element added to the stack, will be the first element removed from stack 
-> used when you want undo an action that was at the top of the stack like history object when using React 
"""
#should have head, tail, length
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
       self.storage.add_to_tail(value)
       self.size += 1

    def pop(self):
        if self.size > 0:
            value = self.storage.remove_from_tail()
            self.size -= 1
            return value 
        else:
            return None

    def len(self):
        return self.size
