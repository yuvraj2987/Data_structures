#! /usr/bin/env python

import unittest


class StackTest(unittest.TestCase):
    def setUp(self):
        from Stack import Stack
        self.stack = Stack(5)

    def testPush(self):
        self.stack.push(1)
