import unittest
from unittest import TestCase
import runner


class RunnerTest(TestCase):
    def test_walk(self):
        run = runner.Runner('Vasya')

        for _ in range(10):
            run.walk()

        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = runner.Runner('Vasya')

        for _ in range(10):
            run.run()

        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run = runner.Runner('Vasya')
        run2 = runner.Runner('Kopchik')

        for _ in range(10):
            run.run()
            run2.walk()

        self.assertNotEqual(run.distance, run2.distance)


if __name__ == '__main__':
    unittest.main()
