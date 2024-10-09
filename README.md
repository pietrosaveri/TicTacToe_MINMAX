# Tic Tac Toe AI using MinMax Algorithm
---
### Overview

This Python project is a Tic Tac Toe game with an AI opponent, designed using the MinMax algorithm. There are two versions of the AI included: a strong AI that plays optimally, and a weaker AI that provides more of a challenge for beginners.

The strong AI uses the full potential of the MinMax algorithm, making it virtually unbeatable, while the weaker AI limits its depth or makes suboptimal moves, giving the player a better chance of winning. This project demonstrates the use of AI algorithms to solve simple games and provides an introduction to game theory concepts like minimax.

### Features

- **Strong AI:** A virtually unbeatable opponent that plays optimally using the MinMax algorithm.
- **Weaker AI:** A toned-down version of the AI that is easier to beat, making the game more enjoyable for casual players.
- **Tic Tac Toe gameplay:** Classic 3x3 grid, where players alternate between placing "X" or "O".
- **Simple and clean interface:** The game runs in the terminal, with easy-to-read grid positions.

### MinMax Algorithm

The MinMax algorithm is a decision-making algorithm used in game theory. In this Tic Tac Toe game, the AI evaluates every possible move using a recursive function that simulates both the AI's and player's turns. The algorithm aims to:

- Maximize the AI's chance of winning.
- Minimize the player's chance of winning.
The strong AI evaluates all possible moves and chooses the optimal one, while the weaker AI might either skip certain future states or make random moves to simulate imperfect play.
