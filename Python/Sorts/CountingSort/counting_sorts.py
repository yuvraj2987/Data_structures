#! /usr/bin/env python
import unittest

def countingSort(a, k):
    c = [0,] * (k+1) # O(k)
    arr_len = len(a) # O(n)
    # Count the number of elements
    # O(n)
    for i in xrange(0, arr_len):
        c[a[i]] += 1
    # end of for
    # sum the elements
    # O(K)
    for j in xrange(1, k+1):
        c[j] += c[j-1]
    # end of for 
    b = [0,] * arr_len # O(K)
    # O(n)
    for i in xrange(arr_len-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
    # end of transformation
    return b


# Test cases
class TestCountingSort(unittest.TestCase):

    def setup(self):
        pass

    def test1(self):
        print "Test1: 6 elments range 3"
        arr = [3, 1, 1, 2, 1, 3]
        self.assertTrue(countingSort(arr, 3), [1, 1, 1, 2, 3, 3])

# End of class


if __name__ == '__main__':
    unittest.main()
