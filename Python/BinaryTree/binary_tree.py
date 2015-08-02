#! /usr/bin/env python

# -------------------
# Binary Tree as single Node implementation
# -----------

import unittest

class BinaryTreeNode:
    """
        Data Storage Class
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


Node = BinaryTreeNode

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BinaryTree.insertNode(self.root, data)

    @staticmethod
    def insertNode(node, data):
        if node == None:
            return Node(data)
        if node.data >= data:
            node.left = BinaryTree.insertNode(node.left, data)
        else:
            node.right = BinaryTree.insertNode(node.right, data)
        return node

    def printInOrder(self):
        self.printInOrderNode(self.root)

    def printInOrderNode(self, node):
        if node == None:
            return
        self.printInOrderNode(node.left)
        print "%s" % str(node)
        self.printInOrderNode(node.right)

    def size(self):
        return BinaryTree.sizeNode(self.root)

    @staticmethod
    def sizeNode(node):
        if node == None:
            return 0
        return BinaryTree.sizeNode(node.left) + 1 + BinaryTree.sizeNode(node.right)


# -------- Test Methods -------
class BinaryTreeTestSize(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def test1(self):
        print "Test1: Empty Tree size"
        self.assertEqual(0, self.tree.size())

    def test2(self):
        print "Test2: 3 node Balanced tree"
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(7)
        self.assertEqual(3, self.tree.size())

    def test3(self):
        print "Test3: 6 nodes unbalanced tree"
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(3)
        self.tree.insert(4)
        self.tree.insert(5)
        self.assertEqual(5, self.tree.size())



def normalTest():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(4)
    tree.insert(7)
    print tree.printInOrder()



if __name__ == "__main__":
    unittest.main()
    # normalTest()
