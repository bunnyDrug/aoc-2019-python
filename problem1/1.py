from functools import reduce

def fuel_requirements(mass):
    fuel = (int(mass) // 3) - 2
    result = 0
    while fuel > 0:
        result += fuel
        fuel = (int(fuel) // 3) - 2
    return result


input = open('input').read().splitlines()


fuel_counter = [fuel_requirements(mass) for mass in input]

total_fuel_required = reduce(lambda x, y: x + y ,fuel_counter)

print("Total Fuel required is: " + str(total_fuel_required))


