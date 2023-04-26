import os
import sys

import cnf as f
from itertools import product

def minisat_solve(problem_name, problem_dimacs, number_to_var_name):
    try:
        with open(f'{problem_name}.cnf', 'w') as f:
            f.write(problem_dimacs)
    except:
        sys.exit('Greska!')

    os.system(f'minisat {problem_name}.cnf {problem_name}_result')

    try:
        with open(f'{problem_name}_result', 'r') as f:
            lines = f.readlines()

        if lines[0].startswith('SAT'):
            print('SAT')
            var_values = {}

            for var in lines[1].split(' ')[:-1]:
                var_number = int(var.strip('-'))
                var_name = number_to_var_name[var_number]
                var_values[var_name] = 0 if var.startswith('-') else 1

            true_vars = list(filter(lambda v: v[1], var_values.items()))
            true_vars.sort()

            for var in true_vars:
                print(var)
        else:
            print("UNSAT")
    except:
        sys.exit('Greska 2')

def n_queens(n):
    cnf = f.CNF()

    # u svakoj koloni se nalazi tacno jedna dama
    # p_ij -> tacno ukoliko je na polju (i, j) nalazi jedna dama
    for i in range(n):
        clause = [f'p_{i}_{j}' for j in range(n)] # p0i | p1i | .. | p(n-1)i
        cnf.add_claues(clause)

    # u svakoj vrsti moze da se nadje jedna dama
    # ~(pki & pkj) <=> ~pki | ~pkj (i != j)
    for k in range(n):
        for i in range(n-1):
            for j in range(i+1, n):
                cnf.add_claues([f'-p_{k}_{i}', f'-p_{k}_{j}'])

    # u svakoj koloni moze da se nadje najvise jedna dama
    # ~(pik & pjk) <=> ~pik | ~pjk (i != j)
    for k in range(n):
        for i in range(n-1):
            for j in range(i+1, n):
                cnf.add_claues([f'-p_{i}_{k}', f'-p_{j}_{k}'])

    # nema dama koje se napadaju dijagonalno
    # ~(pij & pkl) = ~pij | ~pkl
    for i, j, k, l in product(range(n), repeat=4):
        if k > i and abs(k-i) == abs(l - j):
            cnf.add_claues([f'-p_{i}_{j}', f'-p_{k}_{l}'])

    minisat_solve(f'{n}_qunns', cnf.dimacs(), cnf.number_to_var_name)

if __name__ == '__main__':
    n_queens(100)

