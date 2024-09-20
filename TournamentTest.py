import unittest
from unittest import TestCase

from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)
        self.distance = 90

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(test_value)

    def test_tour_1(self):
        tour_1 = Tournament(self.distance, self.runner_1, self.runner_3)
        result = tour_1.start()
        self.all_results['test_tour_1'] = result

    def test_tour_2(self):
        tour_1 = Tournament(self.distance, self.runner_2, self.runner_3)
        result = tour_1.start()
        self.all_results['test_tour_2'] = result

    def test_tour_3(self):
        tour_1 = Tournament(self.distance, self.runner_1, self.runner_2, self.runner_3)
        result = tour_1.start()
        self.all_results['test_tour_3'] = result


if __name__ == '__main__':
    unittest.main()
