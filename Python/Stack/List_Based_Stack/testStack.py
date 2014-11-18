#! /usr/bin/env python

import unittest
from Stack import Stack, StackFullError, StackEmptyError


class StackTest(unittest.TestCase):

    def testPush(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.isEmpty())

    def testStackFullError(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertRaises(StackFullError, stack.push(5))

if __name__ == "__main__":
    unittest.main()
