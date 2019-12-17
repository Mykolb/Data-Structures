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
        #add value to tail (end of stack)
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        #if stack is bigger than zero than you can take one subtract one from the tail 
        if self.size> 0:
            self.size -= 1
            return self.storage.remove_from_tail()
            
        else:
            return None #if nothing in stack, return none

    def len(self):
        return self.size


