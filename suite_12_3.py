import unittest
import runner_test
import tournament_test

ts = unittest.TestSuite()
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tournament_test.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts)
