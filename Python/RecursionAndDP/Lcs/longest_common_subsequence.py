#! /usr/bin/env python

#####
# str1 = [a, b, c, d, e]
# str2 = [b, d, e]

def longestCommonSubSequenceLenDP(str1, str2):
    """
        get length of LCS(str1, str2) using Dynamic Programming algo
    """
    len1 = len(str1)
    len2 = len(str2)
    mat = [ [0 for col in xrange(0:len2+1)] 
            for row in xrange(0: len1+1)]
    for col in xrange(1: len2+1):
        for row in xrange(1: len1+1):
            if str1[row-1] == str2[col-1]:
                mat[row][col] = mat[row-1][col-1] + 1
            else:
                mat[row][col] = max([ mat[row-1][col], 
                                    mat[row][col-1] ])
            # end of if else
        # end of row for
    # end of col for
    return mat[len1][len2]
