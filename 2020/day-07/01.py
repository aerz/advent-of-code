import re

def find_bag_colors(rules, color):
    colors = []

    for rule in rules:
        if color in re.findall("(?:[0-9])+(?: )+(\w+ \w+)", rule):
            colors.append(' '.join(rule.split()[0:2]))

    return colors

def find_combination_colors(rules, colors):
    result = []

    for color in colors:
        bags = find_bag_colors(rules, color)
        result += bags

        if len(bags) > 0:
            result += find_combination_colors(rules, bags)

    return result + colors

with open('input.txt') as file:
    rules = file.read().splitlines()

print(len(set(
    find_combination_colors(rules, find_bag_colors(rules, 'shiny gold'))
)))