def collect_group_answers():
    with open('input.txt') as file:
        lines = file.read().splitlines()
        answers = []
        start = end = 0

        for index, line in enumerate(lines):
            if len(line) == 0 or index + 1 == len(lines):
                answers.append(''.join(lines[start:end + 1]))
                start = end + 1
            end += 1

    return answers

print(
    sum([len(set(answer)) for answer in collect_group_answers()])
)