SIZE = 6
# Create matrix
matrix = [input().split() for i in range(SIZE)]

prizes = {
    "Lego Construction Set": lambda x: 300 <= x,
    "Teddy Bear": lambda x: 200 <= x <= 299,
    "Football": lambda x: 100 <= x <= 199
}


def collect_sum(column):
    numbers = [int(matrix[row][column]) for row in range(SIZE) if matrix[row][column].isdigit()]
    return sum(numbers)


score = 0
hit_buckets = []
for _ in range(3):
    strike = input()
    r, c = [int(x) for x in strike[1:-1].split(", ")]
    if r not in range(SIZE) or c not in range(SIZE):
        continue
    hit = matrix[r][c]
    if hit.isalpha() and [r, c] not in hit_buckets:
        points = collect_sum(c)
        score += points
        hit_buckets.append([r, c])

for prize in prizes:
    if prizes[prize](score):
        print(f"Good job! You scored {score} points, and you've won {prize}.")
        break
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
