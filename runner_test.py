import unittest
from unittest import TestCase
from runner_and_tournament import Runner


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run = Runner('Vasya')

        for _ in range(10):
            run.walk()

        self.assertEqual(run.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = Runner('Vasya')

        for _ in range(10):
            run.run()

        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run = Runner('Vasya')
        run2 = Runner('Kopchik')

        for _ in range(10):
            run.run()
            run2.walk()

        self.assertNotEqual(run.distance, run2.distance)

