import tkinter as tk

from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.buttonsGrid = []
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.window, text="", width=15, height=8, command= lambda i=i,j=j: self.make_move(i,j))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttonsGrid.append(row)
    
    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttonsGrid[row][col].configure(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", "The Winner is " + self.current_player)
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "No one wins")
                self.window.quit()
            self.current_player = "O" if self.current_player == "X" else "X"


    def check_winner(self, player):
        for i in range(4):
            if player == self.board[i][0] and player == self.board[i][1] and player == self.board[i][2] and player == self.board[i][3]:
                return True
            if player == self.board[0][i] and player == self.board[1][i] and player == self.board[2][i] and player == self.board[3][i]:
                return True
        if player == self.board[0][0] and player == self.board[1][1] and player == self.board[2][2] and player == self.board[3][3]:
            return True
        if player == self.board[0][3] and player == self.board[1][2] and player == self.board[2][1] and player == self.board[3][0] :
            return True
        
        return False

    def is_draw(self): 
        for row in self.board:
            if "" in row:
                return False 
            else:
                return True 
    
    def run(self):
       self.window.mainloop()

game = TicTacToe()
game.run()        