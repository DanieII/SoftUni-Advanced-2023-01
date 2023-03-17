class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.number = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.end:
            raise StopIteration

        self.number += 1
        return self.number - 1


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
