import math

# Open the file
input_file = open('input.txt', 'r')

# Read every line of the file into a list of strings
lines_in_file = input_file.readlines()

# Turn that list of strings into a list of modules
modules = [int(line) for line in lines_in_file]


def calculate_fuel(module):
    return math.floor(module/3)-2


# Calculate the mass for each module
mass = [calculate_fuel(module) for module in modules]

# Add of the masses together
answer = sum(mass)

print('Answer is', answer)
