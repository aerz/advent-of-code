import math

def binary_space_partition(even, odd, half):
    assert (half == 'even' or half == 'odd'),"half must be 'odd' (left) or 'even' (right)"

    if even == 0 and half == 'odd':
        odd = math.trunc(odd - (odd - even) / 2)
        return [even, odd]
    
    if half == 'even':
        even = round(odd - (odd - even) / 2)
        return [even, odd]
    
    if half == 'odd':
        odd = math.trunc(even + (odd - even) / 2)
        return [even, odd]

def calculate_seat_row(letters):
    left  = 0
    right = 127
    position = letters[-1]
    halfs = { 'F': 'odd', 'B': 'even' }

    for letter in letters:
        left, right = binary_space_partition(left, right, halfs[letter])

    return left if position == 'F' else right

def calculate_seat_column(letters):
    top = 0
    bottom = 7
    position = letters[-1]
    halfs = { 'L': 'odd', 'R': 'even' }

    for letter in letters:
        top, bottom = binary_space_partition(top, bottom, halfs[letter])
    
    return top if position == 'L' else bottom

def calculate_seat_id(boarding_pass):
    row = calculate_seat_row(boarding_pass[:7])
    column = calculate_seat_column(boarding_pass[7:])
    return row * 8 + column

with open('input.txt') as file:
    boarding_passes = [line.strip() for line in file]

# Part one

ids = [calculate_seat_id(boarding_pass) for boarding_pass in boarding_passes]
print(max(ids))

# Part two

ids = sorted([calculate_seat_id(boarding_pass) for boarding_pass in boarding_passes])

for id, next_id in zip(ids, ids[1:]):
    if id + 1 != next_id:
        print(id + 1)
        break