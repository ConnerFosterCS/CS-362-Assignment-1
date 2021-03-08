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

  def testFizz(self):
    self.assertEqual(main.fizzbuzz(3), "Fizz")
    self.assertEqual(main.fizzbuzz(9), "Fizz")
    self.assertEqual(main.fizzbuzz(99), "Fizz")

  def testBuzz(self):
    self.assertEqual(main.fizzbuzz(5), "Buzz")
    self.assertEqual(main.fizzbuzz(25), "Buzz")
    self.assertEqual(main.fizzbuzz(50), "Buzz")

if __name__ == '__main__':
  unittest.main()