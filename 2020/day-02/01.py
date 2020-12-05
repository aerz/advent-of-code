import re

with open('input.txt') as file:
    policies = [line for line in file]

valid = 0

for policy in policies:
    min = int(policy[:policy.find('-')])
    max = int(policy[policy.find('-')+1:policy.find(' ')])
    key = policy[policy.find(' ')+1:policy.find(':')]
    
    found = len(re.findall(key, policy)) - 1
    valid += 1 if found >= min and found <= max else 0

print(valid)
