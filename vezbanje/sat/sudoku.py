from itertools import product

import cnf as f

def same_subsquare(row1, col1, row2, col2, n):
    block_size = n**0.5
    block1 = (row1 // block_size, col1 // block_size)
    block2 = (row2 // block_size, col2 // block_size)

    return block1 == block2

def sudoku(board):
    cnf = f.CNF()

    n = len(board)

    # S_i_j_k polje (i, j) sadrzi broj k

    for row, col in product(range(n), repeat=2):
        number = board[row][col]
        if number != 0:
            cnf.add_claues([f'S_{row}_{col}_{number}'])

    # svako polje mora da ima vrednost od 1 do 9
    for row, col in product(range(n), repeat=2):
        clause = [f'S_{row}_{col}_{number}' for number in range(1, n+1)]
        cnf.add_claues(clause)

    # jedno polje ne sme da sadrzi dva broja
    # ~(S_r_c_k & S_r_c_k')  (k != k')
    for row, col in product(range(n), repeat=2):
        for num1, num2 in product(range(1, n+1), repeat=2):
            if num1 < num2:
                clause = [f'-S_{row}_{col}_{num1}', f'-S_{row}_{col}_{num2}']
                cnf.add_claues(clause)

    # ne smeju u istom redu da stoji isti broj
    # ~(S_r_c_k & S_r'_c_k)     r != r'
    # ~(S_r_c_k & S_r_c'_k)     c != c'
    # ~(S_r_c_k & S_r'_c'1_k)   (r,c) != (r', c')   u istom podkvadrantu da je isti broj

    for row1, col1, row2, col2, num in product(range(n), repeat=5):
        num += 1

        if (col1 == col2 and row1 < row2) or (row1 == row2 and col1 < col2) or ((row1, col1) != (row2, col2) and same_subsquare(row1, col1, row2, col2, n)):
            cnf.add_claues([f'-S_{row1}_{col1}_{num}', f'-S_{row2}_{col2}_{num}'])

    cnf.minisat_solve('sudoku', cnf.dimacs(), cnf.number_to_var_name)

if __name__ == '__main__':
    board = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]

    sudoku(board)