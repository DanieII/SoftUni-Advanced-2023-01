def forecast(*args):
    output = []
    for elements in args:
        location = elements[0]
        weather = elements[1]
        output.append(f"{location} - {weather}")
    sorted_by_names = sorted(output, key=lambda x: x.split(" - ")[0])
    sunny = ""
    cloudy = ""
    rainy = ""
    for i in sorted_by_names:
        values = i.split(" - ")
        if values[1] == "Sunny":
            sunny += f"{i}\n"
        elif values[1] == "Cloudy":
            cloudy += f"{i}\n"
        else:
            rainy += f"{i}\n"
    return sunny + cloudy + rainy


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
