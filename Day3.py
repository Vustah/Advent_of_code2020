import Advent_of_code2020 as aoc

def solveDay3(down_dir=1, right_dir=3):
    slope = aoc.importFile("03122020.txt")
    for idx in range(len(slope)):
        slope[idx] = slope[idx].replace("\n","")
    slope_length = len(slope)
    slope_width = len(slope[0])
    i = 0
    j = 0
    number_of_trees = 0
    while(1):

        thing = slope[i][j]
        if thing == "#":
            number_of_trees += 1

        i += down_dir
        if i>=slope_length:
            break
        j += right_dir
        if j>=slope_width:
            j = j-slope_width

    print("Number of obsticals of Down %d, Right %d: %d" %(down_dir,right_dir,number_of_trees))
    return number_of_trees

if __name__ == "__main__":
    solveDay3()