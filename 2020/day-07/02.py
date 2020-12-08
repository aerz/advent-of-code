import re

def find_inside_bag_colors(rules, color):
    for rule in rules:
        main = ' '.join(rule.split()[0:2])

        if color in main:
            colors = []
            combinations = re.findall("[0-9]+ \w+ \w+", rule)

            for combination in combinations:
                colors += int(combination[0]) * [combination[2:]]

            return colors

    return []

def count_combination_colors(rules, colors):
    uniques = set(colors)
    total = sum(map(colors.count, uniques))

    for unique in uniques:
        combinations = find_inside_bag_colors(rules, unique)

        if len(combinations) > 0:
            total = total + colors.count(unique) * count_combination_colors(rules, combinations)

    return total

with open('input.txt') as file:
    rules = file.read().splitlines()

print(
    count_combination_colors(rules, find_inside_bag_colors(rules, 'shiny gold'))
)