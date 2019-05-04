import unittest
from run import complement 


def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
  def test(self):
    self.assertEqual(fun(3), 4)
  def test_complement(self):
    self.assertEqual(complement(0, 5), 4)
    self.assertEqual(complement(1, 5), 3)
    self.assertEqual(complement(2, 5), 2)
    self.assertEqual(complement(3, 5), 1)
    self.assertEqual(complement(4, 5), 0)
    


if __name__ == '__main__':
  unittest.main()