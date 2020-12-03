with open('input.txt') as input_file:
    expenses = [int(line) for line in input_file]

# x = 2020 - y
def find_year_numbers_multiplied(year):
    for i in expenses:
        key = year - i
        for j in expenses:
            if key == j:
                return i * j

print(find_year_numbers_multiplied(2020))