def negative_vs_positive(*args):
    numbers = args[0]
    positive = sum([x for x in numbers if x > 0])
    negative = sum([x for x in numbers if x < 0])
    return f"""{negative}
{positive}
The {"negatives" if abs(negative) > positive else "positives"} are stronger than the {"positives" if abs(negative) > positive else "negatives"}"""


# Test
print(negative_vs_positive([int(x) for x in input().split()]))
