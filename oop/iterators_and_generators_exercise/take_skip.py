class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0 - step

    def __iter__(self):
        return self

    def __next__(self):
        if not self.count:
            raise StopIteration

        self.number += self.step
        self.count -= 1

        return self.number


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
