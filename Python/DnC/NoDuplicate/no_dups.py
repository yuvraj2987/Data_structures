#! /usr/bin/env python

import unittest

def findNonDupRecur(arr, start, end):
    if start > end:
        return None
    if start == end:
        return arr[start]
    mid = start + (end - start)/2
    if (mid%2 == 0):
        # mid is even
        if arr[mid] == arr[mid+1]:
            return findNonDupRecur(arr, mid+2, end)
        else:
            return findNonDupRecur(arr, start, mid+1)
    else:
        # mid is odd
        if arr[mid] == arr[mid-1]:
            return findNonDupRecur(arr, mid+1, end)
        else:
            return findNonDupRecur(arr, start, mid-1)
#end of method

def findNonDup(arr):
    return findNonDupRecur(arr, 0, len(arr)-1)



class TestFindNonDup(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        print "Test1: single element"
        arr = [1]
        self.assertEqual(findNonDup(arr), 1)

    def test2(self):
        print "Test2: 3 elements"
        arr = [1, 1, 2]
        self.assertEqual(findNonDup(arr), 2)

    def test3(self):
        print "Test3: 3 elements"
        arr = [1, 2, 2]
        self.assertEqual(findNonDup(arr), 1)

    def test4(self):
        print "Test4: Geek For Geeks example 1"
        arr = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
        self.assertEqual(findNonDup(arr), 4)


if __name__ == '__main__':
    unittest.main()
