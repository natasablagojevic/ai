# -*- coding: utf-8 -*-
"""predikatska_logika.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/natasablagojevic/ai/blob/main/09.Z3/predikatska_logika.ipynb
"""

# Svaki covek je smrtan  - aksioma
# Sokrat je covek        - aksioma
# Sokrat je smrtan       - konjaktura

# Predikati:
# Smrtan(X)
# Covek(X)

# Domen: sta god zelimo da bude (neki skup)
# Kodomen: T/F

from z3 import *

# BoolSort, IntSort, RealSort
Objekat = DeclareSort('Objekat')
Human = Function('Human', Objekat, BoolSort())
Mortal = Function('Mortal', Objekat, BoolSort())

socrates = Const('socrates', Objekat)

# zapis aksioma
x = Const('x', Objekat)
# niz promenljivih uhvacene kvantifikatorom
A1 = ForAll([x], Implies(Human(x), Mortal(x)))
A2 = Human(socrates)
conjucture = Mortal(socrates)

s = Solver()
s.add(A1)
s.add(A2)

# uvek pre provere
if s.check() == sat:
    print('axioms coherent')
    
    # pps: konjaktura sledi iz suprotnog
    s.add(Not(conjucture))
    print(s.check())
else:
    print('axioms incoherent')

# Dve nemimopilazne prave se seku ili su paralelne
# Prave koje se seku, leze u istoj ravni
# Prave koje su paralelne leze u istoj ravni
# Dve nemimoilazne prave leze u istoj ravni

                 # implikacija na konjukciju
# m(X,Y) - X i Y su neminoilazne
# p(X,Y) - X i Y su paralelne
# s(X,Y) - X i Y se seku
# r(X,Y) - X i Y u istoj ravni

B = BoolSort()

P = DeclareSort('Prave')

m = Function('m', P, P, B)
s = Function('s', P, P, B)
p = Function('p', P, P, B)
r = Function('r', P, P, B) 


x, y = Consts('x y', P)

A1 = ForAll([x, y], Implies(m(x, y), Xor(s(x,y), p(x,y))))
A2 = ForAll([x, y], Implies(s(x,y), r(x,y)))
A3 = ForAll([x,y], Implies(p(x,y), r(x,y)))

conjucture = ForAll([x,y], Implies(m(x,y), r(x,y)))

s = Solver()
s.add(A1, A2, A3)
print(s.check())
# s.add(conjucture)
s.add(Not(conjucture))
print(s.check())

# UPROSCAVANJE IZRAZA

x = Int('x')
y = Int('y')
# x,y = Ints('x y')
expr = simplify(x+y+2*x+3)
s = Solver()
s.add(expr > 0)
s.check()

simplify(x < y + x + 2)

# korisno kod: optimizacije, dokazivanje
simplify(And(x+1 >= 3, x**2 + + x**2 + y**2 + 2 >= 5))

# Dokazivanje

p, q = Bools('p q')
# jedna valuacija koja daje zadato ogranicenje
solve(Implies(And(p, q), p))

# dokazivanje
prove(Implies(And(p, q), p))

de_morgan = Not(And(p, q)) == Or(Not(p), Not(q))
prove(de_morgan)

prove(And(p, Not(p)))

# Sta Z3 NE MOZE da uradi - kriptografija

x, y = Ints('x y')
# pubkey = 3*7
pubkey = 1000000993 * 1000001011
solve(x*y == pubkey, x > 1, y > 1)

# Na ispitu iz ovoga da se uradi par stvari
# 1. uradi jednacina
# 2. nesto da se uprosti
# 3. nesto da se dokaze
# 4. da su date predikatske recenice koje treba da se rese

# Masinsko ucenje
# podsetiti se numpy, pandas, matplotlib