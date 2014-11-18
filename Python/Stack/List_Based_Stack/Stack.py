class StackFullError(Exception):
    pass


class StackEmptyError(Exception):
    pass


class Stack:

    def __init__(self, size):
        self.items = []
        self.size = size

    def isEmpty(self):
        return self.items == []

    def push(self, element):
        if len(self.items) == self.size:
            raise StackFullError
        self.items.append(element)

    def pop(self):
        if self.isEmpty():
            raise StackEmptyError()
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise StackEmptyError()
        return self.items[len(self.items) - 1]
