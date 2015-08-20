#! /usr/bin/env python

import unittest

#####
#         0  1  2  3  4
# str1 = [a, b, c, d, e]
#         0  1  2
# str2 = [b, d, e]
# len1 = 5
# len2 = 3
# mat = 5,3
# col = 0 to 3 i.e 
# row = 0 to 5
# col = 1 to 3
#   row = 1 to 5
def longestCommonSubSequenceLenDP(str1, str2):
    """
        get length of LCS(str1, str2) using Dynamic Programming algo
    """
    len1 = len(str1) # 5
    len2 = len(str2) # 3
    mat = [ [0 for col in xrange(0, len2+1)] 
            for row in xrange(0, len1+1)]
    for col in xrange(1, len2+1):
        for row in xrange(1, len1+1):
            if str1[row-1] == str2[col-1]:
                mat[row][col] = mat[row-1][col-1] + 1
            else:
                mat[row][col] = max([ mat[row-1][col], 
                                    mat[row][col-1] ])
            # end of if else
        # end of row for
    # end of col for
    return mat[len1][len2]


# Test cases
class LcsTest(unittest.TestCase):

    def setUp(self):
        self.func = longestCommonSubSequenceLenDP

    def test1(self):
        print "Test1: Simple positive test case"
        str1 = "abcde"
        str2 = "bde"
        self.assertEqual(self.func(str1, str2), 3)



if __name__ == '__main__':
    unittest.main()
