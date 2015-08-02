
import unittest

# 8 2 4 9 3 6
# 2 8 4 9 3 6
# 2 4 8 9 3 6
# j = 1 to 5
# i = 0 to 4
# j = 2, i = 1 key = 4

def insertion_sort(arr):
    if arr == None:
        return
    end_idx = len(arr) - 1
    for j in xrange(1, end_idx+1):
        i = j-1
        key = arr[j]
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        # end of while
        arr[i+1] = key
    # end of for




# Test cases
class SortTest(unittest.TestCase):

    def setup(self):
        pass

    def test1(self):
        print "Test1: simple non-sorted array"
        arr = [8, 2, 4, 9, 3, 6]
        insertion_sort(arr)
        self.assertEqual(arr, [2, 3, 4, 6, 8, 9])

    def test2(self):
        print "Test2: sorted array"
        arr = [ 1, 2, 3, 4]
        insertion_sort(arr)
        self.assertEqual(arr, [ 1, 2, 3, 4])

    def test3(self):
        print "Test3: same element array"
        arr = [2, 2, 2]
        insertion_sort(arr)
        self.assertEqual(arr, [2, 2, 2])

    def test4(self):
        print "Test4: reverse sorted array"
        arr = [9, 8, 7, 6, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [5, 6, 7, 8, 9])



if __name__ == '__main__':
    unittest.main()
