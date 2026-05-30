"""Convert number to sounds."""
SOUNDS = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

def convert(number):
    results = ''.join(sound for divisor, sound in SOUNDS.items() 
                     if number % divisor == 0)
    return results or str(number)

        
