with open('input.txt') as file:
    policies = [line for line in file]

valid = 0

for policy in policies:
    first = int(policy[:policy.find('-')]) - 1
    second = int(policy[policy.find('-')+1:policy.find(' ')]) - 1
    key = policy[policy.find(' ')+1:policy.find(':')]
    passw = policy[policy.find(': ')+2:]
    
    if passw[first] == key and passw[second] != key:
        valid += 1
    
    if passw[first] != key and passw[second] == key:
        valid += 1

print(valid)
