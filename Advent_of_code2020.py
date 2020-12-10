import Day9
import Day10


def importFile(filename):
    infile = open(filename, 'r')
    contents = []
    for line in infile.readlines():
        contents.append(line)
    return contents



    

if __name__ == "__main__":
    Day9.solve1()
    print(Day9.solve2())