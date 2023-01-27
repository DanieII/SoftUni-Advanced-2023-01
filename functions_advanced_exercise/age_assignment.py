def age_assignment(*args, **kwargs):
    people = dict()
    for k, v in kwargs.items():
        for name in args:
            if name[0] == k:
                people[name] = v
    return "\n".join([f"{name} is {age} years old." for name, age in sorted(people.items(), key=lambda x: x[0])])


# Test
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
