"""
    Z3 - sluzi za predikatsku logiku
        ako dodje na ispitu docice iz predikatske loguike, a ne iz iskazne
    
    **Iskazna logika**
    svodjenje na SAT - dobije se pajton kod i CNF()
        treba dodavati uslove, kodiranje
"""

from z3 import *

# --------------

A, B, C, D = Bools("A B C D")

s = Solver()
# s.add(A == D, B == C, Not(And(A == B, B == C, C == D)))

s.add(A == D, B == C, Not(A == B))

# if s.check() == sat:
    # # mapiranje koja promenljiva se slika u koju vrednost
    # print(s.model())

while s.check() == sat:
    print(s.model())
    model = s.model()
    
    s.add(Not(And(A == model[A], B == model[B], C == model[C], D == model[D])))

# ------------------------------------

A, B = Bools("A B")
s = Solver()
s.add(A == B)

while s.check() == sat:
    m = s.model()

    for x in m:
        print(x)
        print(m[x])
        s.add(Not(n == m[x]))

    # print()
    
# ----------------------------------------

# resavanje sistema jednacina
x, y, z = Reals("x y z")

s = Slover()

s.add(
    x + 5*y - 3*z == 4,
    -x + y + z == 3,
    2*x + y - z == 1
)

if s.check() == sat:
    print(s.model())


#--------------------------------

"""
    N dama
    promenljive su dosta izrazajnije

    Q1 prvi red
    promen kolona
    Q0 = [0, 3]
    Q0 = 2  -> u nultoj koloni na poziciji 2 se nalazi dama
"""

n = 8
Q = [Int(f"Q_{i}") for i in range(n)]
val_c = [And(0 <= q, q < n) for q in Q] # u svakoj vrsi makar jedna dama
col_c = [Distinct(Q)]   # za sve promenljive da imaju razlicitu vrednost
diag = [
    And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i)
    for i in range(n) for j in range(i) if i != j
]

n_quens = val_c + col_c + diag

solve(n_queens)
