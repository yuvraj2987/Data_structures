#! /usr/bin/env python

## Implementation for the quick sort ####
import unittest



def swap(arr, i, j):
    """
        swap array elements at index i and j
    """
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, start, end):
    """
        description - partition the array on pivote = arr[start]
        input
        arr - array
        start - first index + pivote element
        end - last index
        output
        pivote index in partitioned array
    """
    pivote = arr[start]
    i = start
    j = start + 1
    while j <= end:
        if arr[j] <= pivote:
            i += 1
            swap(arr, i, j)
        # end if
        j += 1
    # end of while
    swap(arr, start, i)
    return i


def quickSort(arr, start, end):
    """
        input:
            arr - array to be sorted
            start
            end
    """
    if start < end:
        q = partition(arr, start, end)
        quickSort(arr, start, q-1)
        quickSort(arr, q+1, end)
    # end of if

##### Test cases ###

class SortTest(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        print "Sort 2 element array"
        arr = [2, 1]
        quickSort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2])

    def test2(self):
        print "Sort 3 element array"
        arr = [3, 1, 2]
        quickSort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2, 3])

    def test3(self):
        print "Already sorted array"
        arr = [1, 2, 3, 4, 5]
        quickSort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test4(self):
        print "Same element array"
        arr = [3, 3, 3]
        quickSort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [3, 3, 3])


if __name__ == '__main__':
    unittest.main()
