from FormerBoard import FormerBoard
from unittest import TestCase


class BestSectorSolver:
    def __init__(self, board: FormerBoard):
        self.board = board
        self.solutions = {}

    def solve(self):
        board = self.board.get_deep_copy()

        solution = []
        b = board.get_deep_copy()

        while not b.is_empty():
            sectors = b.find_sectors()
            best_sector = max(sectors, key=sectors.get)
            solution.append(best_sector)
            b.remove_sector(best_sector[0], best_sector[1])


class TestBestSectorSolver(TestCase):
    def test_smoketest(self):
        test_board = FormerBoard()
        test_board.load_board(FormerBoard.TEST1)

        solver = BestSectorSolver(test_board)
        result = solver.solve()


if __name__ == '__main__':
    import unittest
    unittest.main()
