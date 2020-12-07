import Advent_of_code2020 as aoc 

def solveDay6():
    contents = aoc.importFile("06122020.txt")
    new_input = [[]]
    for item in contents:
        if item == "\n":
            new_input.append([])
        else:   
            nextInputLine = item.replace("\n", "")
            nextInputLine = nextInputLine.split(" ")
            for thing in nextInputLine:
                new_input[-1].append(thing)

    count = 0    
    for answers in new_input:
        yes_answers = []
        for answer in answers:
            for yes in answer:
                if not yes in yes_answers:
                    yes_answers.append(yes)
        count += len(check_for_common_letters(answers))
        #count += len(yes_answers)

    print(count)

def check_for_common_letters(list_of_letter_strings):
    common_letters = []
    first_string = list_of_letter_strings[0]
    for letter in first_string:
        letterIsCommon = recursive_letter_check(letter,list_of_letter_strings)
        if letterIsCommon:
            common_letters.append(letter)
        
    return common_letters

def recursive_letter_check(letterToCheck,listOfLetters):
    try:
        if letterToCheck in listOfLetters[0]:        
            return recursive_letter_check(letterToCheck,listOfLetters[1:]) 
        else:
            return False
    except IndexError:
        return True

if __name__ == "__main__":
    solveDay6()