from __future__ import division

import math

from sympy import *

#z = sympify("x**2")

def SolveForX(Equation, Answer):
    """
    :param Equation: The equation to be solved
    :param Answer: The answer
    :return: return the value of x
    """
    x = symbols('x') #sets the symbol
    Equation = Eq(Equation, Answer)
    y = solveset(Equation)
    return y



def SinD(Value):
    """
    :param Value: the value, in degrees
    :return: return the sin of the value
    """
    Value = math.radians(Value)
    Return = math.sin(Value)
    return Return


def SinR(Value):
    """
    :param Value: the value, in radians
    :return: return the sin of the value
    """
    Return = math.sin(Value)
    return Return


def CosD(Value):
    """
    :param Value: the value, in degrees
    :return: return the cosine of the value
    """
    Value = math.radians(Value)
    Return = math.cos(Value)
    return Return


def CosR(Value):
    """
    :param Value: the value, in radians
    :return: return the cosine of the value
    """
    Return = math.cos(Value)
    return Return


def TanD(Value):
    """
    :param Value: the value, in degrees
    :return: return the tangent of the value
    """
    Value = math.radians(Value)
    Return = math.tan(Value)
    return Return


def TanR(Value):
    """
    :param Value: the value, in radians
    :return: return the tangent of the value
    """
    Return = math.tan(Value)
    return Return


def ArcSinD(Value):
    """
    :param Value: the value, in degrees
    :return:
    """
    Value = math.radians(Value)
    Return = math.asin(Value)
    return Return


def ArcSinR(Value):
    """
    :param Value: the value, in radians
    :return:
    """
    Return = math.asin(Value)
    return Return


def ArcCosD(Value):
    """
    :param Value: the value, in degrees
    :return:
    """
    Value = math.radians(Value)
    Return = math.acos(Value)
    return Return


def ArcCosR(Value):
    """
    :param Value: the value, in degrees
    :return:
    """
    Return = math.acos(Value)
    return Return


def ArcTanD(Value):
    """
    :param Value: the value, in degrees
    :return:
    """
    Value = math.radians(Value)
    Return = math.atan(Value)
    return Return


def ArcTanR(Value):
    """
    :param Value: the value, in degrees
    :return:
    """
    Return = math.atan(Value)
    return Return


def ToRadians(Value):
    """
    :param Value: The value to turn into radians
    :return: the radians value of the given
    """
    Return = math.radians(Value)
    return Return


def ToDegrees(Value):
    """
    :param Value: The value to turn into degrees
    :return: the radians value of the given
    """
    Return = math.degrees(Value)
    return Return


def Remainder(Number, division):
    """
    :param Number: Value that will be divided to find remainder
    :param division: value that will be used to divide
    :return: The remainder
    """
    Return = math.remainder(Number, division)
    return Return


def EucDistance(P1, P2):
    """
    :param P1: the first point that has a definite value
    :param P2: the second point that has a definite value
    :return: the euclidean distance between the points
    """
    Return = math.dist(P1, P2)
    return Return


def Pi():
    """
    :return: Value of Pi
    """
    Return = math.pi
    return Return


def e():
    """
    :return: Value of e
    """
    Return = math.e
    return Return


def tau():
    """
    :return: Value of tau
    """
    Return = math.tau
    return Return


def ln(Value):
    """
    :param value: the value that the user wants to use in the natural log
    :return: returns the natural log of Value
    """
    Return = math.log(Value)
    return Return


def log(Value, Base):
    """
    :param Value: the value that the user wants to use in the log with a base of his choice
    :param Base: the base the user wants to use in the log function
    :return: returns the log of value divided by log of base
    """
    Return = math.log(Value, Base)
    return Return


def Sqrt(Value):
    """
    :param Value: The value that the user wants teh square root of
    :return: square root of the value
    """
    Return = math.sqrt(Value)
    return Return


def pow(V1, V2):
    """
    :param V1: the base of the exponent
    :param V2: raised to the power of v2
    :return: the value of the power
    """
    Return = math.pow(V1, V2)
    return Return


def differentiation(Value, Respect):
    """
    :param Value:
    :param Respect:
    :return:
    """
    x, y, z, t = symbols('x y z t')
    Return = diff(Value, Respect)
    return Return


def Limit(Expression, Letter, FinalValue):
    """
    :param Expression: The equation used in the limit
    :param Letter: The letter meaning x -> 0, the letter here is x
    :param FinalValue: The final value achieved from computing the limit
    :return: returns the limit value found
    """
    x, y, z, t = symbols('x y z t')
    Return = limit(Expression, Letter, FinalValue)
    return Return

