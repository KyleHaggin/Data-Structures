import sys
sys.path.append('../Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache(DoublyLinkedList):
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        super().__init__()
        self.limit = limit
        self.size = 0
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.move_to_end(node)
            return node.value[key]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        # If key is already in storage, overwrite the value
        if key in self.storage:
            # Find and open the node
            node = self.storage[key]
            # Store the key/value pair
            node.value = {key: value}
            self.move_to_end(node)
            return

        # Check to see if the chache is full
        if self.size == self.limit:
            # Remove oldest from dictionary
            head_key = list(self.head.value.keys())
            del self.storage[head_key[0]]
            # Remove oldest from LL
            self.remove_from_head()
            # Reduce the size
            self.size -= 1

        # Base case
        # Add to linked list
        self.add_to_tail({key: value})
        # Add the key and value to the dictonary
        self.storage[key] = self.tail
        # Increase size
        self.size += 1
