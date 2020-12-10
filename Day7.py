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

def findBagsInside(bag_string):
    open_bag = bag_string.index("contain")
    bags_inside = open_bag.split(", ")
    bags_inside_list = []
    for bags in bags_inside:
        number, character, color = bags.split(" ")[:-1]
        bags_inside_list.append([number, character + " "+ color])
    return bags_inside_list

def look_into_bags_reqursive(baglist,bags_inside):
    

    return 0

def solveDay7():
    bagSpecs = aoc.importFile("07122020_test.txt")

    bagList = ["shiny gold"]

    bags_inside = [] 

    for i in range(10):
        next_bag_list = lookIntoBags(bagList,bagSpecs)
        for bag in next_bag_list:
            if not bag in bagList:
                bagList.append(bag)
    
    bagList.pop(bagList.index("shiny gold"))
    print(len(bagList))

    

if __name__ == "__main__":
    solveDay7()