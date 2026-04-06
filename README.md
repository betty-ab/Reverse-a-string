##structure
This repository contains my solutions for three Python programming challenges, ranging from basic string manipulation to building a functional CLI game.

Level 1: Reverse a String
Description: A simple utility that takes a string input from the user and flips it backward.

Logic: Uses Python's "slicing" method [::-1] which is the most efficient way to reverse a sequence in Python.

Level 2: Fibonacci SequenceDescription: A program that generates the Fibonacci sequence up to a user-defined number of terms.Logic: Uses a while loop to iteratively add the two preceding numbers ($n_1 + n_2$) to create the next number in the series. It includes error handling to ensure the user enters a positive integer.

Level 3: Tic-Tac-Toe (CLI-based)
Description: A Command Line Interface (CLI) version of the classic Tic-Tac-Toe game for two players (X and O).

Logic: * The board is stored as a list of 9 elements.

A check_winner function scans all rows, columns, and diagonals after every turn.

It prevents players from picking a spot that is already occupied.
