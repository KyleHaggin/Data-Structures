import sys
sys.path.append('../Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, value):
        self.add_to_tail(value)

    def dequeue(self):
        if self.length == 0:
            return None
        return self.remove_from_head()

    def len(self):
        return self.length
