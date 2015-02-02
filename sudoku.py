#!/usr/bin/env python


def solve(puzzle):
    i = puzzle.find('0')
    if i == -1:
        return puzzle
    
    excluded_num_set = set()
    for j in range(81):
        if i / 9 == j / 9:                  # same row
            excluded_num_set.add(puzzle[j])
        elif (i - j) % 9 == 0:              # same col
            excluded_num_set.add(puzzle[j])
        elif i / 27 == j / 27 and (i % 9) / 3 == (j % 9) / 3: # same square
            excluded_num_set.add(puzzle[j])

    for k in range(1,10):
        if str(k) not in excluded_num_set:
            solved = solve(puzzle[:i] + str(k) + puzzle[i+1:])
            if solved: 
                return solved

def sudoku(puzzle):
    working_copy = ""
    for row in puzzle:
        for cell in row:
            working_copy += str(cell)        # Converts 2-dim array to string

    solved_puzzle_str = solve(working_copy)
    
    solved_puzzle = []                       # Converts string to 2-dim array
    for i in range(9):
        row = []
        for j in range(9):
            row.append(int(solved_puzzle_str[9*i+j]))
        solved_puzzle.append(row)
        
    return solved_puzzle
