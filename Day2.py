import Advent_of_code2020 as aoc

def solveDay2():
    passwords = aoc.importFile("02122020.txt")
    count = 0
    for line in passwords:
        line_contents = line.replace(":", "")
        line_contents = line_contents.split(" ")
        pos_1, pos_2 = line_contents[0].split("-")
        control_letter = line_contents[1]
        input_password = line_contents[2].replace("\n","")
        pos_1 = int(pos_1)-1
        pos_2 = int(pos_2)-1
        if input_password[pos_1]== control_letter:
            if input_password[pos_2] != control_letter:
                count+=1
        if input_password[pos_2]== control_letter:
            if input_password[pos_1] != control_letter:
                count+=1
    print(count)

if __name__ == "__main__":
    solveDay2()