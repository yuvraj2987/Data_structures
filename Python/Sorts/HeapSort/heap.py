#! /usr/bin/env python

import unittest


def left(index):
    return (index << 2) + 1

def right(index):
    return (index << 2) + 2


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.heap_size = 0 # 0 to len-1
        self.size = len(self.arr)

    def setHeapSize(self, heap_size):
        self.heap_size = heap_size

    def maxHeapify(self, index):
        left_index = left(index)
        right_index = right(index)
        arr = self.arr
        largest_index = index
        if left_index <= self.heap_size and arr[left_index] > arr[index]:
            largest_index = left_index
        if right_index <= self.heap_size and arr[right_index] > arr[largest_index]:
            largest_index = right_index

        if largest_index != index:
            swap(arr, index, largest_index)
            self.maxHeapify(largest_index)
    # end of maxHeapify method

    def buildMaxHeap(self):
        self.heap_size = self.size - 1
        mid_index = self.size/2
        for index in xrange(mid_index, -1, -1):
            self.maxHeapify(index)
        # end of for
    # end of method

    def heapSort(self):
        self.buildMaxHeap()
        for index in xrange(self.size-1, 0, -1):
            swap(self.arr, 0, index)
            self.heap_size -= 1
            self.maxHeapify(0)
        # end of for loop
    # end of method

# end of classes

######### Test Cases #############
class HeapSortTests(unittest.TestCase):

    def setup(self):
        pass

    def test1(self):
        print "Test1: unsorted array"
        arr = [5, 4, 3, 1, 2]
        heap = Heap(arr)
        heap.heapSort()
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test2(self):
        print "Test2: reverse sorted"
        arr = [5, 3, 2, 1]
        heap = Heap(arr)
        heap.heapSort()
        self.assertEqual(arr, [1, 2, 3, 5])

    def test3(self):
        print "Test3: already sorted"
        arr = [1, 2, 3]
        heap = Heap(arr)
        heap.heapSort()
        self.assertEqual(arr, [1, 2, 3])

    def test4(self):
        print "Test4: duplicates"
        arr = [5, 3, 4, 3, 1, 1, 2]
        heap = Heap(arr)
        heap.heapSort()
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5])





if __name__ == '__main__':
    unittest.main()
