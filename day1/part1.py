import math

# Open the file
input_file = open('input.txt', 'r')

# Read every line of the file into a list of strings
lines_in_file = input_file.readlines()

# Turn that list of strings into a list of modules
modules = [int(line) for line in lines_in_file]


def calculate_fuel(module):
    return math.floor(module/3)-2


# Calculate the fuel required for each module
fuel = [calculate_fuel(module) for module in modules]

# Add of the fuel requirements together
answer = sum(fuel)

print('Answer is', answer)
