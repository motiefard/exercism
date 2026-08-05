import math

def score(x, y):
    dist = math.sqrt(x**2 + y**2)
    return next((point for r, point in [(1, 10), (5, 5), (10, 1)] if dist <= r), 0)
    
    

