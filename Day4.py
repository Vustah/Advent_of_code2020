import Advent_of_code2020 as aoc

def createDict(item):
    dict_created = {}
    for thing in item:
        dict_created[thing[0:3]] = thing[4:]
    return dict_created

def solveDay4():
    input = aoc.importFile("04122020.txt")
    new_input = [[]]
    
    for item in input:
        if item == "\n":
            new_input.append([])
        else:   
            nextInputLine = item.replace("\n", "")
            nextInputLine = nextInputLine.split(" ")
            for thing in nextInputLine:
                new_input[-1].append(thing)

    count = 0
    for item in new_input:
        byr = False
        ecl = False
        eyr = False
        iyr = False
        hcl = False
        hgt = False
        pid = False
        
        passport = createDict(item)
        if "byr" in passport:
            birth_year = int(passport["byr"])
            if birth_year>=1920 and birth_year<=2002:
                byr = True
        if "iyr" in passport:            
            issue_year = int(passport["iyr"])
            if issue_year>=2010 and issue_year<=2020:
                iyr = True
        if "eyr" in passport:
            exp_year = int(passport["eyr"])
            if exp_year>=2020 and exp_year<=2030:
                eyr = True
        if "hgt" in passport:
            try:
                height = int(passport["hgt"][:-2])
                subfix = passport["hgt"][-2:]
                if subfix == "in":
                    if height >= 59 and height <= 76:
                        hgt = True
                elif subfix == "cm":
                    if height >= 150 and height <= 193:
                        hgt = True
                
            except ValueError:
                hgt = False
        if "hcl" in passport:
            if passport["hcl"][0] == "#":
                hexCode = passport["hcl"][1:]
                if len(hexCode) == 6:
                    if int(hexCode,16) <= 16777215:
                        hcl = True
        if "ecl" in passport:
            eye_color = passport["ecl"]
            valid_colors = ["amb","blu","brn","gry","grn","hzl", "oth"]
            for color in valid_colors:
                if eye_color == color:
                    if not ecl:
                        ecl = True
                    else:
                        ecl = False
                        break

        if "pid" in passport:
            country_of_origin = passport["pid"]
            if len(country_of_origin) == 9:
                pid = True
            try:
                country_of_origin = int(country_of_origin)
            except:
                pid = False

        if byr and ecl and eyr and iyr and hcl and hgt and pid:
            count += 1
    
        for item in passport:
            printString = ""
            for key in passport:
                plusString = "%s %10s\n" %(key, passport[key])
                printString = printString + plusString
            #print(printString)
            #print(" ")
                

    print(count)

if __name__ == "__main__":
    solveDay4()