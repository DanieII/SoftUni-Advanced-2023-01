class vowels:

    def __init__(self, text):
        self.vowels = [x for x in text if x.lower() in 'auoyei']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.vowels):
            raise StopIteration

        self.index += 1
        return self.vowels[self.index - 1]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
