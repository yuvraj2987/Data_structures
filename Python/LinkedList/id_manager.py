#! /usr/bin/env python

import Queue
import unittest
from sets import Set


class InvalidIntegerId(Exception):
    pass

class DuplicateIntegerId(Exception):
    pass


class ID_Manager:
    """
        Manages pool of integer ids
    """

    def __init__(self, start, end):
        """
            contructor for ID_Manager
            start - starting range of ids
            end - end range
        """
        self._start = start
        self._end = end
        self._cur = start - 1  # For Lazy Initialization
        self._free_list = Queue.Queue()
        # self._free_set = Set()
        # end of for

    def get_id(self):
        """
            Get Next id in the range
        """
        if self._cur < self._end:
            self._cur += 1
            return self._cur
        if self._free_list.empty():
            return None
        ret_id = self._free_list.get()
        # self._free_set.remove(ret_id)
        return ret_id

    def free_id(self, int_id):
        """
            Add int_id in the available pool
        """
        if int_id < self._start or int_id > self._end:
            raise InvalidIntegerId()
        # if int_id in self._free_set:
        #     raise DuplicateIntegerId()
        # else:
        #     self._free_set.add(int_id)
        self._free_list.put(int_id)

# End of class ID_Manager

# --------- Test cases ------------


class Test_ID_Manager(unittest.TestCase):
    def setup(self):
        pass

    def test1(self):
        """
            Check you get full range of ids from start to end both inclusive
        """
        print "Test1: Test get_id full range"
        manager = ID_Manager(1, 3)
        self.assertEqual(manager.get_id(), 1)
        self.assertEqual(manager.get_id(), 2)
        self.assertEqual(manager.get_id(), 3)
        self.assertIsNone(manager.get_id())
    # end of method

    def test2(self):
        """
            Check get_id only returns ids those are freed.
            id2 is freed before id1
        """
        print "Test2: Test free_id logic"
        manager = ID_Manager(1, 2)
        id1 = manager.get_id()
        id2 = manager.get_id()
        manager.free_id(id2)
        self.assertEqual(manager.get_id(), id2)
        manager.free_id(id1)
        self.assertEqual(manager.get_id(), id1)
    # end of test2

    def test3(self):
        """
            Test empty list case. There are no ids in the free pool.
            We get None. We can use queue.wait() for multi-threaded env
        """
        print "Test3: Check empty list get_id"
        manager = ID_Manager(1, 0)
        self.assertIsNone(manager.get_id())

    def test4(self):
        """
        """
        print "Test4: Test free_id exception"
        manager = ID_Manager(1, 3)
        self.assertRaises(InvalidIntegerId, manager.free_id, 5)
    # end of test4

    def test5(self):
        print "Test5: Test Lazy Initailization"
        manager = ID_Manager(1, 4)
        self.assertTrue(manager._free_list.empty() is True)
        self.assertEqual(manager.get_id(), 1)
        self.assertEqual(manager.get_id(), 2)
        self.assertTrue(manager._free_list.empty() is True)
        # Free some ids
        manager.free_id(2)
        manager.free_id(1)
        # still
        self.assertEqual(manager.get_id(), 3)
        self.assertEqual(manager.get_id(), 4)
        self.assertEqual(manager.get_id(), 2)
        self.assertEqual(manager.get_id(), 1)
        self.assertIsNone(manager.get_id())

    def test6(self):
        print "Test6: Exception while duplicate free_id()"
        manager = ID_Manager(2, 5)
        id1 = manager.get_id()
        id2 = manager.get_id()
        manager.free_id(id2)
        manager.free_id(id1)
        self.assertRaises(DuplicateIntegerId, manager.free_id, id2)


# end of class


if __name__ == '__main__':
    unittest.main()
