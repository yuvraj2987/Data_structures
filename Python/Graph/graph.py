#! /usr/bin/env python
from enum import Enum
import Queue
import unittest


class NodeColor(Enum):
    """
        Enumeration of Node visited color
        white - 0 # not seen yet
        grey - 1 # seen and in the queue
        black - 2 # completed
    """
    white = 0
    grey = 1
    black = 2
#end of class NodeColor

class GraphNode:

    def __init__(self, data):
        self.data = data
        self.visit = False
        self.color = NodeColor.white
        self.adjList = []

    def addEdge(self, node):
        if node not in self.adjList:
            self.adjList.append(node)

    def getAdjList(self):
        return self.adjList
# class ends

class Graph:

    def __init__(self):
        self.node_list = []

    def addEdge(self, node_1, node_2):
        if node_1 not in self.node_list:
            self.node_list.append(node_1)
        if node_2 not in self.node_list:
            self.node_list.append(node_2)
        node_1.addEdge(node_2)

    def printGraph(self):
        for node in self.node_list:
            node_str = str(node.data) + "->"
            for nb in node.getAdjList():
                node_str += str(nb.data) + "->"
            print node_str
        # end of for

    def checkRoute(self, node_a, node_b):
        """
            returns True/False
            checks if route exists between node_a and node_b
            using BFS
        """
        if node_a == None or node_b == None:
            return False
        if not isinstance(node_a, GraphNode) or not isinstance(node_b, GraphNode):
            return False
        if node_a == node_b:
            return True
        queue = Queue.Queue()
        node_a.color = NodeColor.grey
        queue.put(node_a)
        while not queue.empty():
            node_u = queue.get()
            for node in node_u.getAdjList():
                if node == node_b:
                    return True
                # end of node_b if
                if node.color == NodeColor.white:
                    node.color = NodeColor.grey
                    queue.put(node)
                # end of color.white if
            #end of node for
            node_u.color = NodeColor.black
        # while ends
        return False


### Graph Test


class checkRouteTest(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.node_a = GraphNode("a")
        self.node_b = GraphNode("b")
        self.node_c = GraphNode("c")
        self.node_d = GraphNode("d")
        self.graph.addEdge(self.node_a, self.node_b)
        self.graph.addEdge(self.node_a, self.node_c)
        self.graph.addEdge(self.node_d, self.node_c)
        self.graph.addEdge(self.node_b, self.node_d)
        self.graph.printGraph() 

    def test1(self):
        print "Test1: route exists"
        self.assertTrue(self.graph.checkRoute(self.node_a, self.node_d))
        self.assertTrue(self.graph.checkRoute(self.node_b, self.node_c))
        
    def test2(self):
        print "Test2: self route exist"
        self.assertTrue(self.graph.checkRoute(self.node_c, self.node_c))

    def test3(self):
        print "Test3: route does not exist"
        self.assertFalse(self.graph.checkRoute(self.node_c, self.node_d))


def buildGraph():
    g = Graph()
    node_a = GraphNode("a")
    node_b = GraphNode("b")
    node_c = GraphNode("c")
    node_d = GraphNode("d")
    g.addEdge(node_a, node_b)
    g.addEdge(node_a, node_c)
    g.addEdge(node_d, node_c)
    g.addEdge(node_b, node_d)
    g.printGraph()
    return g


if __name__ == "__main__":
    unittest.main()
