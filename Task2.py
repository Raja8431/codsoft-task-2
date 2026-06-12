from tkinter import *
from tkinter import messagebox
import math

# =========================================
# MAIN WINDOW
# =========================================

root = Tk()
root.title("Tic Tac Toe AI")
root.geometry("700x850")
root.config(bg="#0f172a")

# =========================================
# VARIABLES
# =========================================

board = [" " for _ in range(9)]

buttons = []

human = "X"
ai = "O"

# =========================================
# CHECK WINNER
# =========================================

def check_winner(player):

    win_positions = [

        [0,1,2],
        [3,4,5],
        [6,7,8],

        [0,3,6],
        [1,4,7],
        [2,5,8],

        [0,4,8],
        [2,4,6]
    ]

    for pos in win_positions:

        if (
            board[pos[0]] == player and
            board[pos[1]] == player and
            board[pos[2]] == player
        ):

            return True

    return False

# =========================================
# CHECK DRAW
# =========================================

def check_draw():

    return " " not in board

# =========================================
# MINIMAX ALGORITHM
# =========================================

def minimax(board_state, is_maximizing):

    if check_winner(ai):
        return 1

    if check_winner(human):
        return -1

    if check_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board_state[i] == " ":

                board_state[i] = ai

                score = minimax(
                    board_state,
                    False
                )

                board_state[i] = " "

                best_score = max(
                    score,
                    best_score
                )

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board_state[i] == " ":

                board_state[i] = human

                score = minimax(
                    board_state,
                    True
                )

                board_state[i] = " "

                best_score = min(
                    score,
                    best_score
                )

        return best_score

# =========================================
# AI MOVE
# =========================================

def ai_move():

    best_score = -math.inf
    best_move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = ai

            score = minimax(
                board,
                False
            )

            board[i] = " "

            if score > best_score:

                best_score = score
                best_move = i

    board[best_move] = ai

    buttons[best_move].config(
        text=ai,
        fg="#ef4444",
        bg="#1e293b"
    )

    if check_winner(ai):

        status_label.config(
            text="AI WINS 🤖",
            fg="#ef4444"
        )

        messagebox.showinfo(
            "Game Over",
            "AI Wins 🤖"
        )

        reset_game()

    elif check_draw():

        status_label.config(
            text="DRAW GAME 😅",
            fg="#facc15"
        )

        messagebox.showinfo(
            "Game Over",
            "It's a Draw 😅"
        )

        reset_game()

# =========================================
# PLAYER MOVE
# =========================================

def player_move(index):

    if board[index] == " ":

        board[index] = human

        buttons[index].config(
            text=human,
            fg="#22c55e",
            bg="#1e293b"
        )

        if check_winner(human):

            status_label.config(
                text="YOU WIN 🎉",
                fg="#22c55e"
            )

            messagebox.showinfo(
                "Game Over",
                "You Win 🎉"
            )

            reset_game()

            return

        elif check_draw():

            status_label.config(
                text="DRAW GAME 😅",
                fg="#facc15"
            )

            messagebox.showinfo(
                "Game Over",
                "It's a Draw 😅"
            )

            reset_game()

            return

        ai_move()

# =========================================
# RESET GAME
# =========================================

def reset_game():

    global board

    board = [" " for _ in range(9)]

    for button in buttons:

        button.config(
            text="",
            bg="#1e293b"
        )

    status_label.config(
        text="YOUR TURN ✨",
        fg="#38bdf8"
    )

# =========================================
# HEADER
# =========================================

top_frame = Frame(
    root,
    bg="#111827",
    height=120
)

top_frame.pack(fill="x")

Label(
    top_frame,
    text="TIC TAC TOE AI",
    font=("Arial", 34, "bold"),
    bg="#111827",
    fg="#38bdf8"
).pack(pady=15)

Label(
    top_frame,
    text="Human vs Unbeatable AI",
    font=("Arial", 14),
    bg="#111827",
    fg="#94a3b8"
).pack()

# =========================================
# STATUS LABEL
# =========================================

status_label = Label(
    root,
    text="YOUR TURN ✨",
    font=("Arial", 22, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

status_label.pack(pady=20)

# =========================================
# GAME FRAME
# =========================================

game_frame = Frame(
    root,
    bg="#0f172a"
)

game_frame.pack(pady=30)

# =========================================
# CREATE BUTTONS
# =========================================

for i in range(9):

    button = Button(

        game_frame,

        text="",

        font=("Arial", 38, "bold"),

        width=4,
        height=2,

        bg="#1e293b",

        fg="white",

        activebackground="#334155",

        bd=0,

        cursor="hand2",

        relief=FLAT,

        command=lambda i=i:
        player_move(i)
    )

    button.grid(
        row=i//3,
        column=i%3,
        padx=10,
        pady=10
    )

    buttons.append(button)

# =========================================
# BUTTON FRAME
# =========================================

button_frame = Frame(
    root,
    bg="#0f172a"
)

button_frame.pack(pady=30)

# =========================================
# NEW GAME BUTTON
# =========================================

Button(
    button_frame,
    text="NEW GAME",
    command=reset_game,
    font=("Arial", 15, "bold"),
    bg="#06b6d4",
    fg="black",
    padx=25,
    pady=10,
    bd=0,
    cursor="hand2"
).grid(
    row=0,
    column=0,
    padx=20
)

# =========================================
# EXIT BUTTON
# =========================================

Button(
    button_frame,
    text="EXIT",
    command=root.destroy,
    font=("Arial", 15, "bold"),
    bg="#ef4444",
    fg="white",
    padx=25,
    pady=10,
    bd=0,
    cursor="hand2"
).grid(
    row=0,
    column=1,
    padx=20
)

# =========================================
# FOOTER
# =========================================

Label(
    root,
    text="Developed Using Python, Tkinter & Minimax AI",
    font=("Arial", 12),
    bg="#0f172a",
    fg="#94a3b8"
).pack(side=BOTTOM, pady=20)

# =========================================
# RUN APP
# =========================================

root.mainloop()