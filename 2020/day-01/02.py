with open('input.txt') as input_file:
    expenses = [int(line) for line in input_file]

# x = 2020 - y - z
def find_year_numbers_multiplied(year):
    keys = []
    result = 1

    for i in expenses:
        for j in expenses:
            key = year - i - j
            
            for k in expenses:
                if key == k and k not in keys:
                    keys.append(k)

            if len(keys) == 3:
                for key in keys: result = result * key
                return result

print(find_year_numbers_multiplied(2020))