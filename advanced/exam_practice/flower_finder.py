from collections import deque

vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]

flowers = {
    "rose": [],
    "tulip": [],
    "lotus": [],
    "daffodil": []
}


def check_for_a_match():
    for word, found in flowers.items():
        if len(found) == len(word):
            return word


while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for flower in flowers.keys():
        if current_vowel in flower and current_vowel not in flowers[flower]:
            flowers[flower].extend(current_vowel * (flower.count(current_vowel)))
        if current_consonant in flower and current_consonant not in flowers[flower]:
            flowers[flower].extend(current_consonant * (flower.count(current_consonant)))

    result = check_for_a_match()
    if result:
        print(f"Word found: {result}")
        break

else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
