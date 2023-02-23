n, m = [int(x) for x in input().split()]
first = {input() for _ in range(n)}
second = {input() for _ in range(m)}
print(*first.intersection(second), sep="\n")
