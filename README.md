# TIC-TAC-TOE-AI
Implemented an AI agent that plays the classic game of Tic-Tac-Toe against a human player, using Minimax algorithm.

# Implementation 

**Define the Game Board:**
Represent the Tic-Tac-Toe board as a 3x3 list or array.
Use 'X' for the human player, 'O' for the AI, and empty spaces for available moves.

**Create a Function to Check for a Win:**
Write a function that checks if either player has won by forming a horizontal, vertical, or diagonal line.

**Implement the Minimax Algorithm:**

 -  **Minimax Overview:**

    - Objective: Minimize the opponent's maximum possible win (for the AI, it's minimizing the human's chance to win).
    
    - Recursion: The algorithm simulates all possible moves, scoring them based on potential outcomes (win, lose, draw).
    
    - Base Case: If a win, loss, or draw is detected, return a corresponding score (e.g., +1 for AI win, -1 for human win, 0 for a draw).

- **Pseudocode for Minimax:**

    If the current board state is a win for either player or a draw, return the score.
    For each possible move:
  
       - Simulate the move.
  
       - Call the Minimax function recursively to evaluate the resulting board state.
  
       - Undo the move.
  
    Choose the move with the best score (maximizing for AI's turn, minimizing for human's turn).

**Handle the AI's Move:**

Use the Minimax function to determine the best move for the AI and update the board accordingly.

**Create the Game Loop:**

Alternate turns between the human player and the AI.

Display the board after each move.

Check for a win, loss, or draw after each turn.
