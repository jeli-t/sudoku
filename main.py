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


class SudokuGUI():
    def __init__(self, board, solution):
        self.board = board
        self.solution = solution
        self.window = tk.Tk()
        self.window.title("Sudoku")
        self.window.resizable(0,0)
        self.window.config(background='#454545', padx=20, pady=20)
        self.entries = []

        # create entry fields
        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(self.window, width=2, font=("Arial", 30), fg='#000000', disabledforeground='#000000', disabledbackground='#c4c4c4', justify='center')
                if i == 2 or i == 5:
                    if j == 2 or j == 5:
                        entry.grid(row=i, column=j, padx=(2,6), pady=(2,6))
                    else:
                        entry.grid(row=i, column=j, padx=2, pady=(2,6))
                elif j == 2 or j == 5:
                        entry.grid(row=i, column=j, padx=(2,6), pady=2)
                else:
                    entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # create buttons
        self.check_button = tk.Button(self.window, text="Check solution", font=("Arial", 16), command=self.check_solution)
        self.check_button.grid(row=9, column=0, columnspan=4, pady=20)
        self.solve_button = tk.Button(self.window, text="Show solution", font=("Arial", 16), command=self.show_solution)
        self.solve_button.grid(row=9, column=5, columnspan=4, pady=20)

        # fill the entry fields
        for i in range(9):
            for j in range(9):
                value = self.board[i][j]
                if value != 0:
                    self.entries[i][j].insert(tk.END, str(value))
                    self.entries[i][j].config(state="disabled")

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                solution_value = self.solution[i][j]
                try:
                    if int(value) == solution_value:
                        self.entries[i][j].config(bg='#1dcf4c')
                    else:
                        self.entries[i][j].config(bg='#d10d20')
                except ValueError:
                    self.entries[i][j].config(bg='#d10d20')

    def show_solution(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                solution_value = self.solution[i][j]
                try:
                    if int(value) == solution_value:
                        self.entries[i][j].config(state="disabled")
                    else:
                        self.entries[i][j].delete(0, tk.END)
                        self.entries[i][j].insert(tk.END, str(solution_value))
                        self.entries[i][j].config(state="disabled", disabledbackground='#ffff00')
                except ValueError:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(tk.END, str(solution_value))
                    self.entries[i][j].config(state="disabled", disabledbackground='#ffff00')

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    generator = generate_sudoku()
    solution = generator.return_solution()
    board = generator.return_board()
    gui = SudokuGUI(board, solution)
    gui.run()