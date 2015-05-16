# -------------------- Description --------------------------------------------
# Stack Implementation


class StackNode:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
# Class ends


class StackFull(Exception):
    pass


class StackEmpty(Exception):
    pass


class Stack:

    def __init__(self, size):
        self.top = None
        self.fullSize = size
        self.curSize = 0

    def Push(self, data):
        if self.curSize >= self.fullSize:
            raise StackFull()
        next_nd = StackNode(data)
        next_nd.nextNode = self.top
        self.top = next_nd
        self.curSize += 1
        return

    def Pop(self):
        if self.curSize <= 0:
            raise StackEmpty()
        ret_nd = self.top
        self.top = ret_nd.nextNode
        self.curSize -= 1
        return ret_nd.data

    def Peek(self):
        if self.curSize <= 0:
            raise StackEmpty()
        peek_nd = self.top
        return peek_nd.data
