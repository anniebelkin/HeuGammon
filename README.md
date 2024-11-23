# HeuGammon: A Heuristic-Based Backgammon Simulator

**HeuGammon** is a research and development project designed to explore advanced decision-making algorithms in the game of backgammon. The project focuses on implementing, testing, and improving strategies using heuristic functions, reinforcement learning (RL), and search-based techniques.

## Core Features

### Game Enhancements
- **Time-Limited Moves:** Implement constraints to simulate real-time decision-making.
- **Import/Export Board States:** Save and load game states for analysis or testing.
- **Automatic Legal Move Generation:** Generate all valid moves based on dice rolls and board state.
- **Game-End Detection:** Identify when a game has concluded and calculate results.

### Heuristic-Based Play
- **Heuristic Functions:** Define and integrate two heuristic functions for evaluating board states.
- **Greedy Algorithm:** Support automated gameplay using greedy strategies based on heuristic evaluations.

### Advanced Search Algorithms
- **Minimax Algorithm:** Implement decision-making with heuristic evaluation under time constraints.
- **Monte Carlo Tree Search (MCTS):** Explore strategic decision-making using MCTS variations.

### Reinforcement Learning
- **Policy Learning:** Use neural networks and RL algorithms to learn and refine gameplay strategies.
- **Training AI:** Develop competitive agents capable of advanced decision-making.

### Project Requirements

The simulation environment must support the following features:

- **Generate All Legal Moves:** Ability to generate all legal moves given a dice roll.
- **Dice Roll Generation:** Ability to generate dice rolls with appropriate probability.
- **External Move Input:** Provide a function to receive the next move from an external player.
- **Move Legality Check:** Check if a move is legal.
- **Game-End Detection:** Identify if the game has ended and determine the result.
- **Move Time Limitation:** Ability to limit the time allowed for each move.
- **Random Move Selection:** Option to select a random valid move.
- **Board State Import/Export:** Import and export board states in a compact data format (e.g., array).
- **Tournament Management:** Ability to organize tournaments by inputting a set of players and specifying the number of rounds per match.

### Board Format:
- **Board State:** A list of length 28 representing the board.
  - Positions 1-24 represent the board’s points: 
    - Positive values represent white checkers.
    - Negative values represent black checkers.
  - Position 25: Number of white checkers that have been hit.
  - Position 26: Number of black checkers that have been hit.
  - Position 27: Number of white checkers that have been borne off.
  - Position 28: Number of black checkers that have been borne off.

## Project Goals
1. Develop a flexible and modular backgammon simulator for AI experimentation.
2. Compare the performance of heuristic-based and learning-based strategies.
3. Participate in competitive tournaments to rank and evaluate strategies.

---

**HeuGammon** combines theoretical exploration with practical implementation, offering a platform for experimenting with AI techniques in the challenging domain of backgammon.
