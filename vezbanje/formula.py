import copy
from itertools import combinations

def get_all_valuations(valuations):
    for r in range(len(valuations) + 1):
        for true_values in combinations(valuations, r):
            result = {x: False for x in valuations}
            result.update({x: True for x in true_values})
            yield result

class Formula:
    def __int__(self):
        self.components = []

    def iterpret(self, valuation):
        pass

    def copy(self):
        return copy.deepcopy(self)

    def __and__(self, right):
        return And(self.copy(), right.copy())

    def __or__(self, right):
        return Or(self.copy(), right.copy())

    def __rshift__(self, right):
        return Impl(self.copy(), right.copy())

    def __eq__(self, right):
        return Eq(self.copy(), right.copy())

    def __invert__(self):
        return Not(self.copy())

    def get_all_variables(self):
        pass

    """
    def get_all_varibales(self):
        result = set()
        for c in self.componets:
            result.update(c.get_all_variables())
            
            
        return result
    """

    """
    valjana/tautologija
    kada je tacna za sve ulaze
    """
    def is_valid(self):
        valuations = list(self.get_all_variables())
        for valuation in get_all_valuations(valuations):
            if self.iterpret(valuation) == False:
                return False, valuation

        return True, None

    """
    nezadovoljiva/kontradikcija
    kada je netacna za sve ulaze, tj ne postoji valuacija u kojoj je tacna
    """
    def is_contradictory(self):
        valuations = list(self.get_all_variables())
        for valuation in get_all_valuations(valuations):
            if self.iterpret(valuation) == True:
                return False, valuation

        return True, None

    """
    zadovoljiva
    kada postoji neka valuacija u kojoj je tacna
    """
    def is_satisfable(self):
        valuations = list(self.get_all_variables())
        for valuation in get_all_valuations(valuations):
            if self.iterpret(valuation) == True:
                return True, valuation

        return False, None

    """
    poreciva
    postoji neka valuacija u kojoj je netacna
    """
    def is_falsifiable(self):
        valuations = list(self.get_all_variables())
        for valuation in get_all_valuations(valuations):
            if self.iterpret(valuation) == False:
                return True, valuation

        return False, None

class Var(Formula):
    def __init__(self, name):
        super().__int__()
        self.name = name

    def iterpret(self, valuation):
        return valuation[self.name]

    def __str__(self):
        return self.name

    def get_all_variables(self):
        return set([self.name])
class Const(Formula):
    def __int__(self, value):
        super().__int__()
        self.value - value

    def interpret(self, valuation):
        return self.value

    def __str__(self):
        return "{}".format(1 if self.value else 0)

class And(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def interpret(self, valuation):
        return self.components[0].iterpret(valuation) and self.components[1].iterpret(valuation)

    def __str__(self):
        return "({}) & ({})".format(self.components[0], self.components[1])

    def get_all_variables(self):
        left_valuation = self.components[0].get_all_variables()
        right_valuation = self.components[1].get_all_variables()
        return left_valuation.union(right_valuation)

class Or(Formula):
    def __init__(self, left, right):
        super().__init__()
        self.components = [left, right]

    def interpret(self, valuation):
        return self.components[0].iterpret(valuation) or self.components[1].iterpret(valuation)

    def __str__(self):
        return "({}) | ({})".format(self.components[0], self.components[1])

    def get_all_variables(self):
        left_valuation = self.components[0].get_all_variables()
        right_valuation = self.components[1].get_all_variables()
        return left_valuation.union(right_valuation)


class Impl(Formula):
    def __init__(self, left, right):
        super().__int__()
        self.components = [left, right]

    def interpret(self, valuation):
        return not self.components[0].iterpret(valuation) or self.components[1].iterpret(valuation)

    def __str__(self):
        return "({}) >> ({})".format(self.components[0], self.components[1])

    def get_all_variables(self):
        left_valuation = self.components[0].get_all_variables()
        right_valuation = self.components[1].get_all_variables()
        return left_valuation.union(right_valuation)

class Eq(Formula):
    def __int__(self, left, right):
        super().__int__()
        self.components = [left, right]

    def interpret(self, valuation):
        return self.components[0].iterpret(valuation) == self.components[1].iterpret(valuation)

    def __str__(self):
        return "({}) == ({})".format(self.components[0], self.components[1])

    def get_all_variables(self):
        left_valuation = self.components[0].get_all_variables()
        right_valuation = self.components[1].get_all_variables()
        return left_valuation.union(right_valuation)


class Not(Formula):
    def __init__(self, operand):
        super().__init__()
        self.components = [operand]

    def interpret(self, valuation):
        return not self.components[0].iterpret(valuation)

    def __str__(self):
        return "~({})".format(self.components[0])

    def get_all_variables(self):
        return self.components[0].get_all_variables()



def vars(names):
    return [Var(name.strip()) for name in names.split(',')]

def evaluate_formula(formula: Formula):
    print(formula)
    print("is valid: ", formula.is_valid())
    print("is contradictory:", formula.is_contradictory())
    print("is satisfable: ", formula.is_satisfable())
    print("is falsifiable: ", formula.is_falsifiable())

if __name__ == '__main__':
    x, y, z = vars("x,y,z")
    # formula = Or(
    #     And(x, y),
    #     Impl(y, z)
    # )

    formula = (x & y) | (y >> z)

    valuation = {
        "x" : True,
        "y" : False,
        "z" : True
    }

    evaluate_formula(formula)

    print(formula.iterpret(valuation))