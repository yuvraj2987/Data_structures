#! /usr/bin/env python

import unittest


def mergeSort(arr):
    if arr == None:
        return
    tmp = [0, ] * len(arr)
    mergeSortRecur(arr, tmp, 0, len(arr)-1)


def mergeSortRecur(arr, tmp, start, end):
    if start >= end:
        return
    mid = start + (end - start)/2
    mergeSortRecur(arr, tmp, start, mid)
    mergeSortRecur(arr, tmp, mid+1, end)
    merge(arr, tmp, start, mid, end)

def merge(arr, tmp, start, mid, end):
    index1 = start
    index2 = mid+1
    tmp_index = start
    while index1 <= mid and index2 <= end:
        if arr[index1] <= arr[index2]:
            tmp[tmp_index] = arr[index1]
            index1 += 1
        else:
            tmp[tmp_index] = arr[index2]
            index2 += 1
        # end of if else
        tmp_index += 1
    # end of while
    while index1 <= mid:
        tmp[tmp_index] = arr[index1]
        index1 += 1
        tmp_index += 1
    # end of while
    while index2 <= end:
        tmp[tmp_index] = arr[index2]
        index2 += 1
        tmp_index += 1
    # end of while
    for index in xrange(start, end+1):
        arr[index] = tmp[index]
    # end of for
#end of merge method

## Test cases
class SortTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test1(self):
        print "Test1: basic sorted test"
        arr = [5, 4, 1, 2]
        mergeSort(arr)
        self.assertEqual(arr, [1, 2, 4, 5])

    def test2(self):
        print "Test2: Reverese sorted arr"
        arr = [5, 4, 3, 1]
        mergeSort(arr)
        self.assertEqual(arr, [1, 3, 4, 5])

    def test3(self):
        print "Test3: Sorted array"
        arr = [1, 2, 3, 4]
        mergeSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test4(self):
        print "Test4: Odd reverse  array sort"
        arr = [3, 2, 1]
        mergeSort(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test5(self):
        print "Test5: Odd mix array"
        arr = [2, 3, 7, 6, 1]
        mergeSort(arr)
        self.assertEqual(arr, [1, 2, 3, 6, 7])


if __name__ == '__main__':
    unittest.main()
