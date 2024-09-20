import logging
import traceback
import unittest
from unittest import TestCase
from rt_with_exceptions import Runner
import tests_12_4


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            run = Runner('Vasya', speed=-6)
            for _ in range(10):
                run.walk()
            self.assertEqual(run.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner\n{e}")
            traceback.print_exc()

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner(2)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner\n{e}")
            traceback.print_exc()

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run = Runner('Vasya')
        run2 = Runner('Kopchik')

        for _ in range(10):
            run.run()
            run2.walk()

        self.assertNotEqual(run.distance, run2.distance)
