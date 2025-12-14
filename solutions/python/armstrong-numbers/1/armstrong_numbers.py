def is_armstrong_number(number):
    number_digits = len(str(number))
    sum_digits = sum(int(i) ** number_digits for i in str(number))
    return sum_digits == number
