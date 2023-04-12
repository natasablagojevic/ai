import os
from iertools import product

class KNF:
    def __init__(self):
        self.clauses = []
        self.number_to_var_name = {}
        self.var_name_to_number = {}

    def add_clauses(self, clause):
        self.clauses.append(clause)
        for literal in clause:
            var_name = literal.strip("-")
            if var_name not in self.number_to_var_name:
                var_number = len(self.var_name_to_number) + 1
                self.var_name_to_number[var_name] = var_number
                self.number_to_var_name[var_number] = var_name

    # def get_var_name(self, number: int):
        # return self.var
    def dimacs(self):
        result = f"p cnf {len(self.var_name_to_number)} {len(self.clauses)}\n"
        for clause in self.clauses:
            for literal in clause:
                var_name = literal.strip("-")
                if literal[0] == "-":
                    result += "-"
                result += f"{self.var_name_to_number[var_name]} "

            result += "0\n"

        return result

def minisat_slove(problem_name, problem_dimacs, number_to_var):
    try:
        with open(f"{problem_name}.cnf", "w") as handle:
            handle.write(problem_dimacs)

        os.system(f"minisat {problem_name}.cnf {problem_name}_result.cnf")

        with open(f"{problem_name}_result.cnf", "r") as result_file:
            lines = result_file.readlines()

        if lines[0].startwith("SAT"):
            print("SAT")
            var_values = {}

            for var in lines[1].split(" ")[:-1]:
                var_num = int(var.strip("-"))
                var_name = number_to_var[var_number] 
                var_values[var_name] = 0 if var.startwith("-") else 1

            true_vars = list(filter(lambda v: v[1] == 1, var_values.items()))
            true_vars.sort()

            for var in true_vars:
                print(vars)
        else:
            print("UNSAT")
        
    except:
        sys.exit("greska")

"""
Svakom slovu dodelim promenljivu.
p_{i,j}     p_{0,0} -> T 

(p_{0,0} or p_{0,1} or p_{0,2} or p_{0,3}) 

-----------------
|   |   |   |   |
-----------------
|   |   |   |   |
-----------------
|   |   |   |   |
-----------------
|   |   |   |   |
-----------------

dijagonala: p_{i,j} p_{k,l} -> abs(k-i) == abs(l-j)

"""
def n_dama_cnf(n):
    cnf = KNF()

    # p00
    # f"p{i}{j}"

    # makar jedna dama
    # kolona
    for j in range(n):
        clause = [f"p{i}{j}" for i in range(n)] 
        cnf.add_clauses(clause)

    # da nemamo dve u isto vreme
    # k fiksirana vrsta
    for k in range(n):
        for i in range(n-1):
            for j in range(i+1, n):
                cnf.add_clauses([f"-p{k}{i}", f"-p{k}{j}"])

    for k in range(n):
        for i in range(n-1):
            for j in range(i+1, n):
                cnf.add_clauses([f"-p{i}{k}", f"-p{j}{k}"])

    for i, j, k, l in product(range(n), repeat=4):
        if k > i and abs(k - i) == abs(l - j):
            cnf.add_clauses([f"-p{i}{j}", f"-p{k}{l}"])


"""
S_{i, j, k} i-vrsta, j-kolona, k-broj
not S_{0,0,1}
not S_{0,0,2}
"""

"""
    promenljiva - nema veliku izrazajnost => ime promenljive
    S_{i', j', k'} : ako je k = k' ne moze
"""

def same_subsquare(r1, c1, r2, c2, n):
    block_size = int(n**0.5)

    block1 = (r1 // block_size, c1 // block_size)
    block2 = (r2 // block_size, c2 // block_size)

    return block1 == block2

def sudoku_cnf(initial_board):
    n = len(initial_board)
    print(n)

    cnf = CNF()

                    # dekartov proizvod
    for row, col in product(range(n), repeat=2):
        number = initial_board[row][col]
        if number != 0:
            cnd.add_clauses([f"S_{row}_{col}_{number}"])

    # na jednom polju je neki broj od 1 do 9
    for row, col in product(range(n), repeat=2):
        clause = [f"S_{row}_{col}_{number}" for number in range(1, n+1)]
        cnf.add_clauses(clause)

    # na istom polju ne mogu biti dva broja
    for row, col in product(range(n), repeat=2):
        for num1, num2 in product(range(1, n+1), repeat=2):
            if num1 != num2:
                clause = [f"-S_{row}_{col}_{num1}", f"-S_{row}_{col}_{num2}"]
                cnf.add_clauses(clause)

    # ako su u istom redu ili koloni ili kvadratu ne mogu imati isti broj
    for row1, col1, row2, col2, number in product(range(n), repeat=5):
        number += 1
                                                                            # poredi redom po koordinatama
        if (row1 == row2 and col1 < col2) or (col1 == col2 and row1 < row2) or ((row1, col1) != (row2, col2) and same_subsquare(row1, col1, row2, col2, n)):
            cnf.add_clauses([f"-S_{row1}_{col1}_{number}", f"-S_{row2}_{col2}_{number}"])

    
# def main():
    # formula = KNF()
    # formula.add_clauses(["p", "q"])
    # formula.add_clauses(["-p","-r"])
# 
    # # print(formula.dimacs())
# 
    # minisat_slove("test", formula.dimacs(), formula.number_to_var_name)

if __name__ == '__main__':
    # main()
    # formula = KNF()
    # formula.add_clauses(["p", "q"])
    # formula.add_clauses(["-p","-r"])
    # print(formula.dimacs())
    # minisat_slove("test", formula.dimacs(), formula.number_to_var_name)
    # -------------------
    # minisat("n_dama", cnf.dimacs(), cnf.number_to_var_name)

    true_vars = minisat_slove("sudoku", cnf.dimacs(), cnf.number_to_var_name)

    if true_vars is None:
        sys.exit("greska")

    for true_vars, _ in true_vars:
        """
            S_{}_{}_{}
        """
        tokens = true_var.split('_')
        i = int(tokens[1][0])
        j = int(tokens[2][0])
        number = int(tokens[3][0])
        initial_board[i][j] = number 

    print(initial_board)
    
