class Node():
    def __init__(self, init_value):
        self.value = init_value
        self.next = None

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value
