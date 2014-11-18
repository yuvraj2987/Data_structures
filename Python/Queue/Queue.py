

# -------------------- Description --------------------------------------------
# Queue implementation
# queue = Queue()
# queue -> ["abc", True]
# queue.enqueue(10)
# data -> 10
# queue.enqueue("abc")
# data -> "abc"
# queue.enqueue("True")
# data -> True
# queue.dequeu()
# 10

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        """ This O(n) """
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
