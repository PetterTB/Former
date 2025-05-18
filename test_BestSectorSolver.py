from unittest.case import TestCase

from BestSectorSolver import BestSectorSolver
from FormerBoard import FormerBoard


class TestBestSectorSolver(TestCase):
    def test_simple(self):
        test_board = FormerBoard()
        test_board.load_board(FormerBoard.TEST1)

        solver = BestSectorSolver(test_board)
        result = solver.solve()
        self.assertEqual([(0, 1), (0, 2)], result)
