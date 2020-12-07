import Advent_of_code2020 as aoc

def solveDay1():
    contents = aoc.importFile("01122020.txt")
    for number in contents:
        number = int(number)
        for second_number in contents:
            second_number = int(second_number)
            for third_number in contents:
                third_number = int(third_number)
                if number+second_number+third_number == 2020:
                    answer = number*second_number*third_number
    print(answer)

if __name__ == "__main__":
    solveDay1()