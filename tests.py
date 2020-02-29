import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        expected = 3.14159
        self.assertEqual(expected, task.areacircle(1))

    def test4(self):
        expected = [1, 5]
        self.assertEqual(expected, task.liststartend([1, 2, 3, 4, 5]))

    def test5(self):
        expected = 10
        self.assertEqual(expected, task.daycounter((2020, 1, 1), (2020, 1, 11)))


if __name__ == '__main__':
    unittest.main()
