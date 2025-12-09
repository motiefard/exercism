def leap_year(year):
    div_4 = year % 4 == 0
    div_100 = year % 100 == 0
    div_400 = year % 400 == 0

    div_100_400 = not(div_100 ^ div_400)

    return div_4 and div_100_400
    
