def equilateral(sides):
    if validation(sides):
        a, b, c = sides
        if a==b and b==c and c==a : return True
    return False


def isosceles(sides):
    if validation(sides):
        a, b, c = sides
        if a==b or b==c or c==a : return True
    return False


def scalene(sides):
    if validation(sides):
        a, b, c = sides
        if a!=b and b!=c and c!=a : return True
    return False


def validation(sides):
    for side in sides:
        if side <= 0:
            return False
    a, b, c = sides
    if not a + b >= c : return False
    if not b + c >= a : return False
    if not a + c >= b : return False
    return True