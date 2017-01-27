import re

input_seat = "EEOEE"


def get_seat(input_seat):
    #seats = list(input_seat)
    seats = input_seat
    print(type(seats))
    #check for the last seat
    if seats[-1] == 'E':
        print(len(seats) - 1)
    elif seats[0] == 'E':
        print(0)
    else:
        print(re.compile("(E+E)").findall(seats))
        print(min(re.compile("(E+E)").findall(seats)))
        print(seats.find(min(re.compile("(E+E)").findall(seats))) + 1)

def get_best_seat(seats):
    print(seats)
    seats[4] = 'J'
    print(seats)

get_seat(input_seat)


