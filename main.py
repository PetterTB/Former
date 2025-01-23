from FormerBoard import FormerBoard
import tkinter as tk


class NaiveBruteforceSolver:

    def __init__(self, board, tries=100):
        self.board = board
        self.result = []
        self.tries = tries

    def solve(self):
        best_solution = self.do_single_solve()
        for i in range(self.tries):
            solution = self.do_single_solve()
            if len(solution) < len(best_solution):
                best_solution = solution

        return best_solution

    def do_single_solve(self):
        solution = []
        work_board = self.board.get_deep_copy()
        while not work_board.is_empty():
            h, w = work_board.find_random_sector()
            solution.append((h, w))
            work_board.remove_sector(h, w)

        return solution


class GUI:

    def __init__(self, res, game):

        self.window = tk.Tk()
        self.window.title("Former Explorer")

        self.game = game
        self.set_result(res)

        self.step = 0

        self.update_board()
        label = tk.Label(self.window, text="Best is : " + str(len(res)))
        label.grid(row=0, column=10)

        next_step = tk.Button(self.window, text="Do next",
                              command=self.next_step)
        next_step.grid(row=1, column=10)

        label = tk.Label(self.window, text="Next step: " +
                         str(self.result[self.step]))
        label.grid(row=2, column=10)

    def set_result(self, res):
        self.result = res
        if (len(self.result) == 0):
            self.result = [(0, 0)]
        for r in self.result:
            if len(r) < 2:
                raise Exception(
                    "GUI: Result given has wrong format: " + str(r))

    def update_board(self):

        b = self.game.board
        for i in range(len(b)):
            for j in range(len(b[-1])):
                text = b[i][j]
                if text == 1:
                    text = "*"
                if text == 2:
                    text = "<"
                if text == 3:
                    text = "&"
                if text == 4:
                    text = "#"
                text = str(text)

                if i == self.result[self.step][0] and j == self.result[self.step][1]:
                    label = tk.Label(self.window, text=text, bg="#f00")
                else:
                    label = tk.Label(self.window, text=text)
                # Each label is placed in its corresponding grid position
                label.grid(row=i, column=j)

    def next_step(self):

        r = self.result[self.step]
        self.game.remove_sector(r[0], r[1])

        self.step += 1

        foo = ""
        if (self.step >= len(self.result)):
            foo = "Last Done!"
            self.step -= 1
        else:
            "Next step:"

        label = tk.Label(self.window, text=foo + str(self.result[self.step]))
        label.grid(row=2, column=10)

        self.update_board()


if __name__ == '__main__':
    to_print = FormerBoard()
    to_print.load_board_11_nov()

    solver = NaiveBruteforceSolver(to_print, tries=10000)
    result = solver.solve()

    gui = GUI(result, to_print)

    # Start the event loop.
    gui.window.mainloop()
