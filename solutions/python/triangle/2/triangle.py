def equilateral(sides):
    return validation(sides) and len(set(sides)) == 1


def isosceles(sides):
    return validation(sides) and len(set(sides)) <= 2


def scalene(sides):
    return validation(sides) and len(set(sides)) == 3


def validation(sides):
    a, b, c = sides
    return all(side > 0 for side in sides) and a + b >= c and b + c >= a and c + a >= b