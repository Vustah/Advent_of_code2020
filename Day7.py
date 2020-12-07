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

    bagList = ["shiny gold"]


    for i in range(10):
        next_bag_list = lookIntoBags(bagList,bagSpecs)
        for bag in next_bag_list:
            if not bag in bagList:
                bagList.append(bag)
    
    bagList.pop(bagList.index("shiny gold"))
    print(len(bagList))


if __name__ == "__main__":
    solveDay7()