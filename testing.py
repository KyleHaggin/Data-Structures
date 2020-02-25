class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


def middle(node):
    while node:
        current_value = node.value
        node = node.next
        double_pointer = node.next.next
        if double_pointer is None:
            return current_value


def reverse(node):
    previous_node = None
    current_node = node.next
    while node:
        current_node.next, previous_node, current = previous_node, current_node, current_node.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(middle(node1))
