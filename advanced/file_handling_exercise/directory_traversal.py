import os

found = {}


def directory_traversal(dir, first_level=False):
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            root, extension = os.path.splitext(file)
            if extension not in found:
                found[extension] = []
            found[extension].append(root)
        else:
            if not first_level:
                directory_traversal(path, first_level=True)


directory_traversal(".")

sorted_by_extensions = dict(sorted(found.items(), key=lambda x: x[0]))

report = []
for k, v in sorted_by_extensions.items():
    report.append(k)
    for name in v:
        report.append(f"- - - {name}{k}")
with open("report.txt", "w") as file:
    file.write("\n".join(report))

# Another way with new line at the end
# with open("report.txt", "w") as file:
#     for k, v in sorted_by_extensions.items():
#         file.write(k + "\n")
#         for name in sorted(v):
#             file.write(f"- - - {name}{k}\n")
