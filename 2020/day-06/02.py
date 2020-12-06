def collect_group_answers():
    with open('input.txt') as file:
        lines = file.read().splitlines()
        answers = []
        answer = []

        for index, line in enumerate(lines):
            if len(line) == 0 or index + 1 == len(lines):
                answers.append(set.intersection(*map(set, answer)))
                answer = []
            else:
                answer.append(line)

    return answers

print(
    sum(len(answer) for answer in collect_group_answers())
)