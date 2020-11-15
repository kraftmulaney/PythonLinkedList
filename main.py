from node import Node

print("Welcome to the linked list program!")

first_node = Node(5)
second_node = Node(42)

first_node.set_next(second_node)

iter = first_node
while (iter != None):
    print(iter.get_value())

    iter = iter.get_next()
