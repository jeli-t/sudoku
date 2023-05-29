# sudoku game made with tkinter


import random
import tkinter as tk


class generate_sudoku():
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.generate(self.board)

    def __repr__(self):
        return str(self.board)

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

    def print_board(self):
        for row in self.board:
            print(row)

    def return_board(self):
        return self.board


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
        #####################
        self.show_solution()

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
    solution = generator.return_board()
    game = SudokuGame(solution, solution)
    game.run()