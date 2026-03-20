import streamlit as st
import numpy as np

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3,3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1


def check_winner(board):
    if 3 in np.sum(board,axis=1) or 3 in np.sum(board,axis=0):
        return "X"

    if -3 in np.sum(board,axis=1) or -3 in np.sum(board,axis=0):
        return "O"

    if np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return "X"

    if np.trace(board) == -3 or np.trace(np.fliplr(board)) == -3:
        return "O"

    if 0 not in board:
        return "Draw"

    return None


def make_move(row, col):
    if st.session_state.board[row][col] == 0:
        st.session_state.board[row][col] = st.session_state.current
        st.session_state.current *= -1


st.title("Tic Tac Toe 🎮")

board = st.session_state.board

symbols = {0:" ", 1:"X", -1:"O"}

# Create 3x3 grid
for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        if cols[c].button(symbols[board[r][c]], key=f"{r}{c}"):
            make_move(r,c)

result = check_winner(board)

if result:
    if result == "Draw":
        st.subheader("Match Draw 🤝")
    else:
        st.subheader(f"{result} Wins 🎉")

    if st.button("Restart Game"):
        st.session_state.board = np.zeros((3,3), dtype=int)
        st.session_state.current = 1


 