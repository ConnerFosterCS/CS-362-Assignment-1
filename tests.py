import unittest
import main

class TestCase(unittest.Testcase):
  def test1(self):
    self.assertEqual(main.fizzbuzz(), 0)

if __name__ == '__main__':
  unittest.main()