import os
import sys


class CNF:
    def __init__(self):
        # [['p2', '-p3'], ['-p1', 'p2', '-p3']]
        self.clauses = []
        self.number_to_var_name = {}
        self.var_name_to_number = {}

    def add_claues(self, clause):
        for literal in clause:
            var_name = literal.strip('-')
            if var_name not in self.var_name_to_number:
                var_number = len(self.var_name_to_number) + 1
                self.var_name_to_number[var_name] = var_number
                self.number_to_var_name[var_number] = var_name

        self.clauses.append(clause)

    def dimacs(self):
        result = f'p cnf {len(self.var_name_to_number)} {len(self.clauses)}\n'
        for clause in self.clauses:
            for literal in clause:
                var_name = literal.strip('-')
                if literal[0] == '-':
                    result += '-'
                result += f'{self.var_name_to_number[var_name]} '
            result += '0\n'

        return result

    def minisat_solve(self, problem_name, problem_dimacs, number_to_var_name):
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
