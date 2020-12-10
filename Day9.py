import Advent_of_code2020 as aoc 

def solve1(preamble_scale = 25):
    numbers = aoc.importFile("09122020.txt")

    number_length = len(numbers)
    for i in range(preamble_scale, number_length):
        numbers_OK = False
        current_number = int(numbers[i])
        number_range = [int(j) for j in numbers[i-preamble_scale:i]]
        for j in number_range:
            j = int(j)
            for k in number_range:
                k = int(k)
                if k == j:
                    break
                
                if (current_number-j) == k:
                    numbers_OK = True
                    #print(current_number,j,k)
                    break
            
            if numbers_OK:
                break
        
        if not numbers_OK:
            print(current_number)
            break
    return current_number, numbers

def checkNumber(current_number,sub_numbers):
    count = 0
    for jdx, num in enumerate(sub_numbers):
        count += int(num)
        if count == current_number:
            return jdx
        elif count > current_number:
            return 0

def solve2(preamble_scale = 25):
    current_number, numbers = solve1(preamble_scale)
    number_length = len(numbers)
    for idx in range(number_length):
        jdx = int(checkNumber(current_number,numbers[idx:]))
        if jdx > 0:
            break
    start = idx
    stop = jdx+idx
    subset_numbers = numbers[start:stop]
    maximum = int(max(subset_numbers))
    minimum = int(min(subset_numbers))
    return minimum, maximum, minimum+maximum


if __name__ == "__main__":
    solve1()
    solve2()