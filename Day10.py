import Advent_of_code2020 as aoc 

def solve():
    jolts = aoc.importFile("10122020.txt")
    jolts = [int(j) for j in jolts]
    jolts.sort()
    one_diff = []
    two_diff = []
    three_diff = []
    jolt = 0
    i = 0
    while(i < len(jolts)):
        check = False
        test_jolt = jolts[i]
        
        if test_jolt == jolt+1:
            jolt += 1                
            one_diff.append(test_jolt)
            check = True
        elif test_jolt == jolt+2:
            jolt += 2
            two_diff.append(test_jolt)
            check = True
        elif test_jolt == jolt+3:
            jolt += 3
            three_diff.append(test_jolt)
            check = True

        if check:
            i = 0
        else:
            i += 1

    print(one_diff)
    print(two_diff)
    print(three_diff)    
    print(len(one_diff),len(two_diff),len(three_diff)+1)    
    print(len(one_diff)*(len(three_diff)+1))

if __name__ == "__main__":
    solve()