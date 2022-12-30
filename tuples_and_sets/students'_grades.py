def average(lst):
    return sum(lst) / len(lst)


number_of_students = int(input())
students = (input().split() for _ in range(number_of_students))
my_dict = {}
for name, mark_as_string in students:
    mark = float(mark_as_string)
    if name not in my_dict:
        my_dict[name] = [mark]
    else:
        my_dict[name].append(mark)
for student, grades in my_dict.items():
    formatted_grades = " ".join(f"{grade:.2f}" for grade in grades)
    print(f"{student} -> {formatted_grades} (avg: {average(grades):.2f})")
