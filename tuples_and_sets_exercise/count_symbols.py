text = input()
occurrences = dict()
for i in text:
    if i not in occurrences:
        occurrences[i] = 1
        continue
    occurrences[i] += 1
for k, v in sorted(occurrences.items()):
    print(f"{k}: {v} time/s")
