class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, roman):
        romans = {"I": 1, "V": 5, "X": 10}

        result = 0
        for index in range(len(roman)):
            if index < len(roman) - 1 and romans[roman[index]] < romans[roman[index + 1]]:
                result -= romans[roman[index]]
            else:
                result += romans[roman[index]]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))
