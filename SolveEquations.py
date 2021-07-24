from __future__ import division
from sympy import symbols, solveset, Eq
x = symbols('x')

y = solveset(x)

def SolveForX(Equation, Answer):
    "This function will solve for x using sympy tools"
    print(Equation)
    print(type(Equation))
    x = symbols('x') #sets the symbol
    Equation = Eq(Equation, Answer)
    y = solveset(Equation)
    return y

a = SolveForX(2*x+10, 20)
