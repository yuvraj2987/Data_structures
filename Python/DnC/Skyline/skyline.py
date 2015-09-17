#! /usr/bin/env python

# class - {1, 11, 5} {2, 6, 7} - {left, height, right}
# f(arr, 0, 1)
# f (0, 0) - {1, 11}, {5, 0}
# f (1, 1) - {2, 6}, {7, 0}
# solution - {1, 11}, {5, 7} {7, 0}
# 
# Divide and Conquer

class Building:
    def __init__(self, left, height, right):
        self.left = left
        self.right = right
        self.height = height


class Skyline:
    def __init__(self, x, h):
        self.x = x
        self.h = h



def getSkyline(build_arr, start, end):
    if start > end:
        return None
    if start == end:
        sk1 = Skyline(build_arr[start].left, build_arr[start].height)
        sk2 = Skyline(build_arr[start].right, 0)
        return [sk1, sk2]
    mid = start + (end - start)/2
    left_skylines = getSkyline(build_arr, start, mid)
    right_skylines = getSkylines(build_arr, mid+1, end)
    merged_skylines = mergeSkylines(left_skylines, right)
    return merged_skylines

# f (0, 0) - {1, 11}, {5, 0}
# f (1, 1) - {2, 6}, {7, 0}

def mergeSkylines(left_sks, right_sks):
    combo_sks = []
    l_idx = 0
    r_idx = 0
    while l_idx < len(left_sks) and r_idx < len(right_sks):
        l_x = left_sks[l_idx].x
        l_h = left_sks[l_idx].h
        r_x = right_sks[r_idx].x
        r_h = right_sks[r_idx].h
        if l_x < r_x:
            if l_h > r_h:
                combo_sks.append(Skyline(l_x, l_h))
            # else nothing
            l_idx += 1
        else:
            if r_h > l_h:
                right_ht = r_h
                combo_sks.append(Skyline(r_x, r_h))
            #
            r_idx += 1
        # end of if/else
    # end of while
    return combo_sks

