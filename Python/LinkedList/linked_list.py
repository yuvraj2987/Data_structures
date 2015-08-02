#! /usr/bin/env python

# ------
# Linked List implementation
# -----

class Node:
    """
        Node class of LinkedList
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    


class LinkedList:
    """
        LinkedList class
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
            Put data at the end of the list
        """
        end_node = Node(data)
        if self.head is None:
            self.head = end_node
            return
        # else
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        # end of while
        cur_node.next = end_node

    def push(self, data):
        """
            Put data at the start of the list
        """
        first_node = Node(data)
        if self.head == None:
            self.head = first_node
            return None
        first_node.next = self.head
        self.head = first_node


    def length(self):
        cur_len = 0
        cur_node = self.head
        while cur_node != None:
            cur_len += 1
            cur_node = cur_node.next
        # while ends
        return cur_len

    def __str__(self):
        cur_node = self.head
        linked_list = []
        while cur_node != None:
            linked_list.append(str(cur_node))
            cur_node = cur_node.next
        # end of while
        return "LinkedList: [ " + '->'.join(linked_list) + "]"


# ------ Test Modules --------
def manual_linked_list_test():
    print "Testing Insert and Print"
    print "Test1: Empty Linked List"
    linked_list_1 = LinkedList()
    print str(linked_list_1)
    print "Test2: Full Linked List"
    linked_list_1.append(1)
    linked_list_1.append(2)
    linked_list_1.append(3)
    print str(linked_list_1)


def manual_test_length():
    print "Testing length"
    print "Test1: Empty list"
    linked_list1 = LinkedList()
    if linked_list1.length() != 0:
        print "Failed"
    else:
        print "Pass"
    print "Test2: Single node list"
    linked_list1.append(1)
    if linked_list1.length() != 1:
        print "Failed"
    else:
        print "Pass"
    print "Test3: Long list"
    linked_list1.append(2)
    linked_list1.append(3)
    if linked_list1.length() != 3:
        print "Failed"
    else:
        print "Pass"


if __name__ == '__main__':
    manual_linked_list_test()
    manual_test_length()
