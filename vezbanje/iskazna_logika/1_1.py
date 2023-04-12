import copy
from itertools import combinations


def get_all_valuations(variables):
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

    def __invert__(self):
        return Not(self.copy())

    def all_true_valuations(self):
        result = []
        variables = list(self.get_all_variables())

        for valuation in get_all_valuations(variables):
            if self.interpret(valuation) == True:
                result.append(valuation)

        return result

    def get_all_components(self):
        pass

    """
        zadovoljiva
        da li postoji valuacija u kojoj je tacna
    """
    def is_satisfiable(self):
        valuations = list(self.get_all_components())
        for valuation in get_all_valuations(valuations):
            if self.interpret(valuation) == True:
                return True, valuation
        return False, None

    """
        tautologija
        da je tacna za sve valuacije
    """
    def is_valid(self):
        valuations = list(self.get_all_components())
        for valuation in get_all_valuations(valuations):
            if self.interpret(valuation) == False:
                return False, valuation
        return True, None

    """
        kontradikcija
        za sve valuacije je netacna
    """
    def is_contradictory(self):
        valuations = list(self.get_all_components())
        for valuation in get_all_valuations(valuations):
            if self.interpret(valuation) == True:
                return False, valuation
        return True, None

    """
        poreciva
        postoji valucija u kojoj je netacna
    """
    def is_falsifiable(self):
        valuations = list(self.get_all_components())
        for valuation in get_all_valuations(valuations):
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

    def get_all_components(self):
        return set([self.name])

class Const(Formula):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return "{}".format(1 if self.value else 0)

    def interpret(self, valuation):
        return self.value

    def get_all_components(self):
        return set([])

class And(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def __str__(self):
        return "({}) & ({})".format(self.components[0], self.components[1])

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) and self.components[1].interpret(valuation)

    def get_all_components(self):
        left_components = self.components[0].get_all_components()
        right_components = self.components[1].get_all_components()
        return left_components.union(right_components)

class Or(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def __str__(self):
        return "({}) | ({})".format(self.components[0], self.components[1])

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

    def get_all_components(self):
        left_components = self.components[0].get_all_components()
        right_components = self.components[1].get_all_components()
        return left_components.union(right_components)


class Impl(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def __str__(self):
        return "({}) >> ({})".format(self.components[0], self.components[1])

    def interpret(self, valuation):
        return not self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

    def get_all_components(self):
        left_components = self.components[0].get_all_components()
        right_components = self.components[1].get_all_components()
        return left_components.union(right_components)


class Eq(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def __str__(self):
        return "({}) == ({})".format(self.components[0], self.components[1])

    def interpret(self, valuation):
        return self.components[0].interpret(valuation) == self.components[1].interpret(valuation)

    def get_all_components(self):
        left_components = self.components[0].get_all_components()
        right_components = self.components[1].get_all_components()
        return left_components.union(right_components)


class Not(Formula):
    def __init__(self, operand):
        super().__init__()
        self.components = [operand]

    def __str__(self):
        return "~({})".format(self.components[0])

    def interpret(self, valuation):
        return not self.components[0].interpret(valuation)

    def get_all_components(self):
        return self.components[0].get_all_components()

def vars(names):
    return [Var(name.strip()) for name in names.split(',')]

def evaluate_formula(formula: Formula):
    print(formula)
    print("satisfiable: ", formula.is_satisfiable())
    print("valid: ", formula.is_valid())
    print("contradictory: ", formula.is_contradictory())
    print("falsifiable: ", formula.is_falsifiable())

if __name__ == '__main__':

    x, y, z = vars("x,y,z")

    # formula = Or(
    #     And(x, y),
    #     Impl(z, y)
    # )

    formula = (x & y) | (z >> y)

    valuation = {
        "x" : False,
        "y" : True,
        "z" : False
    }

    print(formula)
    print(formula.interpret(valuation))

    evaluate_formula(formula)