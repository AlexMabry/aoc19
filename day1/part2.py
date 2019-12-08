import math

# Open the file
input_file = open('input.txt', 'r')

# Read every line of the file into a list of strings
lines_in_file = input_file.readlines()

# Turn that list of strings into a list of modules
modules = [int(line) for line in lines_in_file]


def calculate_fuel(mass):
    return math.floor(mass/3)-2


def total_fuel(module):
    fuel_required = calculate_fuel(module)

    if fuel_required > 0:
        return fuel_required + total_fuel(fuel_required)
    else:
        return 0


# Calculate the mass for each module
mass = [total_fuel(module) for module in modules]

# Add of the masses together
answer = sum(mass)

print('Answer is', answer)
