def convert(number):
    divisible = False
    result = ""
    env = {3:"Pling", 5:"Plang", 7:"Plong"}
    
    for q, sound in env.items():
        if (number % q) == 0:
            result += sound
            divisible = True

    if not divisible:
        result = str(number)
    
    return result
