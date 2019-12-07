from functools import reduce

def fuel_requirements(mass):
    return (mass // 3) - 2
    
    
input = open('input').read().splitlines()    
fuel_counter = reduce(lambda x,y:x + fuel_requirements(y), input)
