import Advent_of_code2020 as aoc 

def lookIntoBags(bagList, bagSpecs):
    next_level_baglist = []
    for second_level_bag in bagList:
        for bag in bagSpecs:
            if second_level_bag in bag:
                current_bag = bag.split(" ")
                current_bag_str = current_bag[0] + " " + current_bag[1]
                next_level_baglist.append(current_bag_str)

    return next_level_baglist

def solveDay7():
    bagSpecs = aoc.importFile("07122020.txt")

    bagList = [["shiny gold"]]

    count = 0
    for i in range(10):
        next_bag_list = lookIntoBags(bagList[-1],bagSpecs)
        
        bagList.append(next_bag_list)
        count += len(next_bag_list)

    print(count)

if __name__ == "__main__":
    solveDay7()