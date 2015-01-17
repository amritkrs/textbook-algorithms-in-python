import os
import sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))

import unittest
from ch06.stack import ArrayStack
from ch06.empty_exception import Empty



class TestArrayStack(unittest.TestCase):

    def test_is_empty(self):
        s = ArrayStack()
        self.assertTrue(s.is_empty())

    def test_push(self):
        s = ArrayStack()
        s.push(12)
        self.assertIs(s.top(),12)

    def test_pop(self):
        s = ArrayStack()
        s.push(10)
        self.assertIs(s.pop(),10)
        self.assertTrue(s.is_empty())

        # should raise exception if used top or pop on empty stack
        with self.assertRaises(Empty):
            s.pop()
        with self.assertRaises(Empty):
            s.top()

if __name__ == "__main__":
    unittest.main()