# sudoku game made with tkinter


import random
import tkinter as tk


class generate_sudoku():
    def __init__(self):
        self.solution = [[0] * 9 for _ in range(9)]
        self.board = [[0] * 9 for _ in range(9)]
        self.generate(self.solution)
        self.board = self.remove_values(self.solution, 50)


    def __repr__(self):
        return str(self.solution)

    def is_valid(self, board, row, col, num):
        # check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # check 3x3 block
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    # recursive function
    def generate(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.generate(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    # hide some values from solution
    def remove_values(self, solution, n):
        board = [row[:] for row in solution]
        n = min(n, 50)
        zeros_indices = random.sample(range(81), n)
        for index in zeros_indices:
            row = index // 9
            col = index % 9
            board[row][col] = 0
        return board

    def print_board(self):
        for row in self.board:
            print(row)

    def print_solution(self):
        for row in self.solution:
            print(row)

    def return_board(self):
        return self.board

    def return_solution(self):
        return self.solution


class SudokuGame():
    def __init__(self, board, solution):
        self.board = board
        self.solution = solution
        self.window = tk.Tk()
        self.window.title("Sudoku")
        self.entries = []

        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(self.window, width=4, font=("Arial", 14))
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            self.entries.append(row_entries)

        for i in range(9):
            for j in range(9):
                value = self.board[i][j]
                if value != 0:
                    self.entries[i][j].insert(tk.END, str(value))
                    self.entries[i][j].config(state="disabled")

    def show_solution(self):
        for i in range(9):
            for j in range(9):
                value = self.solution[i][j]
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(tk.END, str(value))
                self.entries[i][j].config(state="disabled")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    generator = generate_sudoku()
    solution = generator.return_solution()
    board = generator.return_board()
    game = SudokuGame(board, solution)
    game.run()