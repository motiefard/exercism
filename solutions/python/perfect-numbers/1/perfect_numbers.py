
def find_factors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors


    
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = find_factors(number)
    aliquot = sum(factors)

    if number < aliquot:
        return "abundant"
    elif number == aliquot:
        return "perfect"
    else: return "deficient"

    
# print(classify(8))