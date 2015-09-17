#! /usr/bin/env python

import Queue
import unittest


class ID_Manager:
    """
        Manages pool of integer ids
    """

    def __init__(self, start, end):
        self._free_list = Queue.Queue()
        for i in xrange(start, end+1, 1):
            self._free_list.put_nowait(i)
        # end of for

    def get_id(self):
        return self._free_list.get()

    def free_id(self, int_id):
        self._free_list.put(int_id)

# End of class ID_Manager

# --------- Test cases ------------


class Test_ID_Manager(unittest.TestCase):
    def setup(self):
        pass

    def test1(self):
        print "Test1: Test get_id full range"
        manager = ID_Manager(1, 3)
        self.assertEqual(manager.get_id(), 1)
        self.assertEqual(manager.get_id(), 2)
        self.assertEqual(manager.get_id(), 3)
        manager.get_id()
    # end of method

    def test2(self):
        print "Test2: Test free_id logic"
        manager = ID_Manager(1, 2)
        id1 = manager.get_id()
        id2 = manager.get_id()
        manager.free_id(id2)
        self.assertEqual(manager.get_id(), id2)
    # end of test2



# end of class


if __name__ == '__main__':
    unittest.main()
