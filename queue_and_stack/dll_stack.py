import sys
sys.path.append('../Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def push(self, value):
        self.add_to_head(value)

    def pop(self):
        if self.length == 0:
            return None
        return self.remove_from_head()

    def len(self):
        return self.length
