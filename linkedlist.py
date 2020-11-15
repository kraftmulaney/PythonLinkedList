from node import Node

class Linked():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, new_node):
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            new_node.set_next(None)
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            new_node.set_next(None)

    def print_all_nodes(self):
        iter = self.head
        while (iter != None):
            print(iter.get_value())
            iter = iter.get_next()

    def delete_head(self):
        # NOT IMPLEMENTED
