#! /usr/bin/env python

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
