def words_sorting(*args):
    words = {}
    for word in args:
        words[word] = sum(ord(x) for x in word)

    sum_of_values = sum(x for x in words.values())

    if sum_of_values % 2 != 0:
        words = sorted(words.items(), key=lambda x: -x[1])
    else:
        words = (sorted(words.items(), key=lambda x: x[0]))

    result = []
    for word, value in words:
        result.append(f"{word} - {value}")

    return "\n".join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

