import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
buttons = []

def check_winner():
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            return True
    return False

def button_click(i):
    global current_player

    if buttons[i]["text"] == "":
        buttons[i]["text"] = current_player

        if check_winner():
            messagebox.showinfo("Winner", current_player + " Wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player
    current_player = "X"
    for b in buttons:
        b["text"] = ""

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
