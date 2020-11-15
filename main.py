from node import Node
from linkedlist import Linked

print("Welcome to the linked list program!")

first_node = Node(5)
second_node = Node(42)

first_node.set_next(second_node)

myList = Linked()
myList.insert(first_node)
myList.insert(second_node)

myList.print_all_nodes()
