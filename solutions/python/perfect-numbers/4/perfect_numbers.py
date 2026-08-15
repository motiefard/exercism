def find_factors(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
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
    if number == aliquot:
        return "perfect"
    return "deficient"
