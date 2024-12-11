from unittest import TestCase
from FormerBoard import FormerBoard


class TestFormerBoard(TestCase):

    def test_smoke_test(self):
        a = FormerBoard()

    def test_remove_sector(self):
        b = FormerBoard()
        b.load_board(FormerBoard.TEST1)
        size = b.remove_sector(1, 1, 2)
        self.assertEqual(size, 4)
        self.assertFalse(b.is_empty())
        b.perform_fall()
        self.assertEqual([1, 1, 1], b.board[-1])

    def test_get_sectors(self):
        b = FormerBoard()
        b.load_board(FormerBoard.TEST1)
        sectors = b.find_sectors()
        self.assertEqual(len(sectors), 3)

