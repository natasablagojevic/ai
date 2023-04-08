# -*- coding: utf-8 -*-
"""Formula.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wZ_Me5hD0cqZpp34J_A3z3iZbhO2R4W5

# ISKAZNA LOGIKA

- valuacija kombinacija True ili False za iskazne promenljive
- Formula:
  1. T, F
  2. a = T
  3. a and T
  4. a and (T or F)

  
      and
     /   \
    a     or 
         /  \
        T    F 

- f = And(Var('a'), Or(Const(True), Const(False)))
- f = interpret(valuation)

class Formula:
  def __init__(self):
    self.components = []

  # apstraktna funkcija
  def interpret(self, valuation):
    pass 

class Var(Formula):
  def __init__(self, name):
    super().__init__()
    self.name = name 

  def interpret(self, valuation):
    return valuation[self.name]

  def __str__(self):
    return self.name 

class Const(Formula):
  def __init__(self, value):
    super().__init__()
    self.value = value

  def interpret(self, valuation):
    return self.value 

  def __str__(self):
    return f'{"T" if self.value else "F"}'

class And(Formula):
  def __init__(self, lhs, rhs):
    super().__init__()
    self.components = [lhs, rhs]

  def interpret(self, valuation):
    return self.components[0].interpret(valuation) and self.components[1].interpret(valuation)

  def __str__(self):
    return f'({self.components[0]} & {self.components[1]})'

class Or(Formula):
  def __init__(self, lhs, rhs):
    super().__init__()
    self.components = [lhs, rhs]

  def interpret(self, valuation):
    return self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

  def __str__(self):
    return f'({self.components[0]} | {self.components[1]})' 

class Impl(Formula):
  def __init__(self, lhs, rhs):
    super().__init__()
    self.components = [lhs, rhs]

  def interpret(self, valuation):
    return not self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

  def __str__(self):
    return f'({self.components[0]} => {self.components[1]})'

class Eq(Formula):
  def __init__(self, lhs, rhs):
    super().__init__()
    self.components = [lhs, rhs]

  def interpret(self, valuation):
    return self.components[0].interpret(valuation) == self.components[1].interpret(valuation)

  def __str__(self):
    return f'({self.components[0]} == {self.components[1]})'

class Not(Formula):
  def __init__(self, op):
    super().__init__()
    self.components = [op]

  def interpret(self, valuation):
    return not self.components[0].interpret(valuation)

  def __str__(self):
    return f'~({self.components[0]})'
"""

import copy

class Formula:
  def __init__(self):
    self.components = []

  # apstraktna funkcija
  def interpret(self, valuation):
    pass 

  def __eq__(self, rhs):
    # da izbegnemo reference saljemo kopiju
    return Eq(self.copy(), rhs.copy())

  def __and__(self, rhs):
    # da izbegnemo reference saljemo kopiju
    return And(self.copy(), rhs.copy())

  def __or__(self, rhs):
    # da izbegnemo reference saljemo kopiju
    return Or(self.copy(), rhs.copy())

  def __rshift__(self, rhs):
    # da izbegnemo reference saljemo kopiju
    return Impl(self.copy(), rhs.copy())

  def __invert__(self):
    # da izbegnemo reference saljemo kopiju
    return Not(self.copy())

  def copy(self):
    return copy.deepcopy(self)

  def is_valid(self):
    variables = list(self.get_all_variables())

    for valuation in all_valuation(variables):
      if self.interpret(valuation) == False:
        return False, valuation 

    return True, None 

  # Resenje SAT problema
  # Problem zadovoljivosti
  # NP-kompletan problem
  def is_satisfable(self):
    variables = list(self.get_all_variables())
                    
                    # eksponencijalan broj resenja
    for valuation in all_valuation(variables):
      if self.interpret(valuation) == True:
        return True, valuation 

    return False, None 

  def is_contradictory(self):
    variables = list(self.get_all_variables())

    for valuation in all_valuation(variables):
      if self.interpret(valuation) == True:
        return False, valuation 

    return True, None 

  # poreciva
  def is_falsifable(self):
    variables = list(self.get_all_variables())

    for valuation in all_valuation(variables):
      if self.interpret(valuation) == False:
        return True, valuation 

    return False, None 


  def get_all_variables(self):
    result = set()

    for c in self.components:
      result.update(c.get_all_variables())

    return result

  def all_true_valuations(self):
    result = []
    variables = list(self.get_all_variables())

    for valuation in all_valuation(variables):
      if self.interpret(valuation) == True:
        result.append(valuation)

    return result



class Var(Formula):
  def __init__(self, name):
    super().__init__()
    self.name = name 

  def interpret(self, valuation):
    return valuation[self.name]

  def __str__(self):
    return self.name 

  # secenje rekurzije
  def get_all_variables(self):
    return set([self.name])

class Const(Formula):
  def __init__(self, value):
    super().__init__()
    self.value = value

  def interpret(self, valuation):
    return self.value 

  def __str__(self):
    return f'{"T" if self.value else "F"}'

class And(Formula):
  def __init__(self, lhs, rhs):
    super().__init__()
    self.components = [lhs, rhs]

  def interpret(self, valuation):
    return self.components[0].interpret(valuation) and self.components[1].interpret(valuation)

  def __str__(self):
    return f'({self.components[0]} & {self.components[1]})'

class Or(Formula):
  def __init__(self, lhs, rhs):
    super().__init__()
    self.components = [lhs, rhs]

  def interpret(self, valuation):
    return self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

  def __str__(self):
    return f'({self.components[0]} | {self.components[1]})' 

class Impl(Formula):
  def __init__(self, lhs, rhs):
    super().__init__()
    self.components = [lhs, rhs]

  def interpret(self, valuation):
    return not self.components[0].interpret(valuation) or self.components[1].interpret(valuation)

  def __str__(self):
    return f'({self.components[0]} => {self.components[1]})'

class Eq(Formula):
  def __init__(self, lhs, rhs):
    super().__init__()
    self.components = [lhs, rhs]

  def interpret(self, valuation):
    return self.components[0].interpret(valuation) == self.components[1].interpret(valuation)

  def __str__(self):
    return f'({self.components[0]} == {self.components[1]})'

class Not(Formula):
  def __init__(self, op):
    super().__init__()
    self.components = [op]

  def interpret(self, valuation):
    return not self.components[0].interpret(valuation)

  def __str__(self):
    return f'~({self.components[0]})'

f = And(Var("a"), Or(Const(True), Const(False)))

f.interpret({"a": True})

a = Var("a")
f1 = a & (True | False)

# b = Var("b")
# c = Var("c")

b, c = vars("b, c")

# f = c | b 
f = c >> b
f.interpret({"b": False, "c": False})

f.get_all_variables()

def vars(names):
  return [Var(name.strip()) for name in names.split(',')]

def evaluate_formula(formula: Formula):
  print(formula)
  print("is valid: ", formula.is_valid())
  print("is satisfable: ", formula.is_satisfable())
  print("is falsifable: ", formula.is_falsifable())
  print("is contradictory: ", formula.is_contradictory())
  print("all true variables:", formula.all_true_valuations())

from itertools import combinations
def all_valuation(variables):
  
  # all_valuation = []
  
  for r in range(0, len(variables) + 1):
    for true_variables in combinations(variables, r):
      result = {x : False for x in variables}
      result.update({x : True for x in true_variables})
      # all_valuation.append(result)
      yield result    # return res, pa kada se pozove opet funkcija krece od sledece iteracije petlje

evaluate_formula(f)

print(f)

ana_je_zubar = Var("ana_je_zubar")
formula = ana_je_zubar | ~ana_je_zubar
evaluate_formula(formula)

"""
Date su dve kutije, A i B. Robot mora da stavi objekat u tacno jednu od njih
 """

A, B = vars("A,B")
formula = (A & ~B) | (~A & B)
evaluate_formula(formula)

"""NOTE: na ispitu ce biti sigurno da se resi mini SAT problem
- oni se resavaju preko AND, OR, NOT

"""

"""
|A|B|
|C|D|

2x2 tacno jedan zeton u svakom redu
"""

A, B, C, D = vars("A,B,C,D")

# dobar oblik za SAT probleme
# odekuju KNF format 
# (A or B) and not(A and B) and (C or D) and not(C and D)
formula = (A | B) & (~A | ~B) & (C | D) & (~C | ~D)
evaluate_formula(formula)