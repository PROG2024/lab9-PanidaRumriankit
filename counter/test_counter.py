"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
import logging
from counter import Counter
logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s %(funcName)8s: %(message)s"
                    )


class CounterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.count1 = Counter()
        self.count2 = Counter()

    def test_same_instance(self):
        self.assertEqual(self.count1, self.count2)

    def test_same_count(self):
        self.count1.increment()
        self.assertEqual(self.count1.count, self.count2.count)

    def test_invoke_count(self):
        c1 = self.count1.count
        c2 = self.count1.count
        self.assertEqual(c1, c2)

    def test_invoke_new(self):
        self.count1.increment()
        self.count3 = Counter()
        self.assertEqual(self.count1, self.count3)
        self.assertEqual(self.count1.count, self.count3.count)
        self.assertEqual(1, self.count1.count)
