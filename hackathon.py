# My solution to the HackSussex hackathon question: create a function that
# takes a 2D matrix and returns True if all the row values and column values
# are unique
# Sample: matrix = [[1,2,3],[2,3,1], [3,1,2]]

def is_unique(matrix: list):
    trans_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
    match_row = {i for i in range(1, len(matrix)+1)}

    row_count = col_count = 0
    for row in matrix:
        if set(row) == match_row:
            row_count += 1
    for row in trans_matrix:
        if set(row) == match_row:
            col_count += 1

    if row_count == col_count and row_count == len(matrix): return True
