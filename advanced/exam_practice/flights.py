def flights(*args):
    flights_dict = {}
    for index in range(0, len(args), 2):
        element = args[index]
        try:
            next_value = args[index + 1]
        except IndexError:
            next_value = None
        if element == "Finish":
            break
        else:
            if element not in flights_dict:
                flights_dict[element] = 0
            flights_dict[element] += int(next_value)

    return flights_dict


print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
