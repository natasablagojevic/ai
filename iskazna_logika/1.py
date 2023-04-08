import copy
from itertools import combinations
def all_valuations(variables):
    for r in range(len(variables) + 1):
        for true_values in combinations(variables, r):
            result = {x: False for x in variables}
            result.update({x: True for x in true_values})
            yield result
class Formula:
    def __init__(self):
        self.components = []

    def interpret(self, valuation):
        pass

    def copy(self):
        return copy.deepcopy(self)
    def __and__(self, other):
        return And(self.copy(), other.copy())

    def __or__(self, other):
        return Or(self.copy(), other.copy())

    def __rshift__(self, other):
        return Impl(self.copy(), other.copy())

    def __eq__(self, other):
        return Eq(self.copy(), other.copy())

    def get_all_variables(self):
        result = set()
        for c in self.components:
            result.update(c.get_all_variables())

        return result

    """validna/tautologija"""
    def is_valid(self):
        variables = list(self.get_all_variables())
        for valuation in all_valuations(variables):
            if self.interpret(valuation) == False:
                return False, valuation

        return True, None

    """kontradikcija"""
    def is_contradictory(self):
        variables = list(self.get_all_variables())
        for valuation in all_valuations(variables):
            if self.interpret(valuation) == True:
                return False, valuation

        return True, None

    """zadovoljiva"""
    def is_satisdable(self):
        variables = list(self.get_all_variables())
        for valuation in all_valuations(variables):
            if self.interpret(valuation) == True:
                return True, valuation

        return False, None

    """poreciva"""
    def is_fasifiable(self):
        valuations = list(self.get_all_variables())
        for valuation in all_valuations(valuations):
            if self.interpret(valuation) == False:
                return True, valuation

        return False, None

class Var(Formula):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def interpret(self, valuation):
        return valuation[self.name]

    def get_all_variables(self):
        return set([self.name])

class Value(Formula):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return "{}".format(1 if self.value else 0)

    def interpret(self, valuation):
        return self.value

    # def get_all_variables(self):
    #     return set()

class And(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def __str__(self):
        return "({}) & ({})".format(self.components[0], self.components[1])

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) and self.components[1].interpret(valuation)

    # def get_all_variables(self):
    #     left_valuations = self.components[0].get_all_variables()
    #     right_valuations = self.components[1].get_all_variables()
    #     return left_valuations.union(right_valuations)

class Or(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def __str__(self):
        return "({}) | ({})".format(self.components[0], self.components[1])

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

    # def get_all_variables(self):
    #     left_valuations = self.components[0].get_all_variables()
    #     right_valuations = self.components[1].get_all_variables()
    #     return left_valuations.union(right_valuations)
class Impl(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def __str__(self):
        return "({}) >> ({})".format(self.components[0], self.components[1])

    def interpret(self, valuation):
        return not self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

    # def get_all_variables(self):
    #     left_valuations = self.components[0].get_all_variables()
    #     right_valuations = self.components[1].get_all_variables()
    #     return left_valuations.union(right_valuations)
class Eq(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def __str__(self):
        return "({}) == ({})".format(self.components[0], self.components[1])

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) == self.components[1].interpret(valuation)

    # def get_all_variables(self):
    #     left_valuations = self.components[0].get_all_variables()
    #     right_valuations = self.components[1].get_all_variables()
    #     return left_valuations.union(right_valuations)
class Not(Formula):
    def __init__(self, operand):
        super().__init__()
        self.components = [operand]

    def __str__(self):
        return "~({})".format(self.components[0])

    def interpret(self, valuation):
        return not self.components[0].interpret(valuation)

def vars(names):
    return [Var(name.strip()) for name in names.split(',')]

def evaluate_formula(formula : Formula):
    print(formula)

if __name__ == '__main__':
    x, y, z = vars("x,y,z")

    formula = (x & y) | (y >> z)

    # formula = Or(
    #     And(x, y),
    #     Impl(y, z)
    # )

    print(formula)
    print("valid:", formula.is_valid())
    print("contradictory:", formula.is_contradictory())
    print("falsifable:", formula.is_fasifiable())
    print("satisfable:", formula.is_satisdable())