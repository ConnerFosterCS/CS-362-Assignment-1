import unittest
import main

class TestCase(unittest.TestCase):
  def testNums(self):
    self.assertEqual(main.fizzbuzz(7), 7)
    self.assertEqual(main.fizzbuzz(52), 52)
    self.assertEqual(main.fizzbuzz(31), 31)

  def testFizzBuzz(self):
    self.assertEqual(main.fizzbuzz(30), "FizzBuzz")
    self.assertEqual(main.fizzbuzz(60), "FizzBuzz")
    self.assertEqual(main.fizzbuzz(90), "FizzBuzz")

if __name__ == '__main__':
  unittest.main()