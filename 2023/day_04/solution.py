from pathlib import Path

USE_SAMPLE_INPUT = False

in_path = Path.cwd() / 'input.txt'

sample_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()

if USE_SAMPLE_INPUT:
    input = sample_input
else:
    with in_path.open("r") as inf:
        input = inf.read().strip()

lines = input.split('\n')

point_sum = 0

for line in lines:
    idx = line.index(':')
    trimmed = line[idx+1:]

    win_part, have_part = trimmed.split('|')

    win_nums = set(int(n) for n in win_part.split())
    have_nums = set(int(n) for n in have_part.split())

    intersect = win_nums.intersection(have_nums)

    if len(intersect) == 0:
        score = 0
    else:
        score = 2 ** (len(intersect) - 1)

    print(line[:idx+1], score)

    point_sum += score

print(f'Part 1: {point_sum}')

card_counts = [1] * len(lines)
for i, line in enumerate(lines):
    splidx = line.index(':')
    trimmed = line[splidx+1:]

    win_part, have_part = trimmed.split('|')

    win_nums = set(int(n) for n in win_part.split())
    have_nums = set(int(n) for n in have_part.split())

    intersect = win_nums.intersection(have_nums)

    for j in range(i+1, min(i + 1 + len(intersect), len(lines))):
        card_counts[j] += card_counts[i]

    print(card_counts)

print(f'Part 2:', sum(card_counts))
