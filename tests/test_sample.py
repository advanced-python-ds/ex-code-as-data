from unittest import TestCase


class FirstTest(TestCase):

    def test_something(self):
        pass


class Evaluate(TestCase):
    def test_exercise(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 1, 0)
