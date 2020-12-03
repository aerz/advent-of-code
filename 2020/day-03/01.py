with open('input.txt') as input_file:
    lines = [line.strip() for line in input_file]

def count_trees(slope_right, slope_down):
    j = 0
    i = 0
    width = len(lines[0])
    total = 0

    while i < len(lines):
        i += slope_down
        j = (j + slope_right) % width

        total += 1 if i < len(lines) and lines[i][j] == '#' else 0

    return total

# Part One
print(count_trees(3, 1))

# Part Two
print(
    count_trees(1, 1) *
    count_trees(3, 1) *
    count_trees(5, 1) *
    count_trees(7, 1) *
    count_trees(1, 2)
)
