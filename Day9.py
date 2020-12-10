import Advent_of_code2020 as aoc 

def solveDay9():
    numbers = aoc.importFile("09122020.txt")
    preamble_scale = 5

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
            print(number_range)
            maximum = max(number_range)
            minimum = min(number_range)
            print(minimum, maximum, minimum+maximum)
            break
            
                


if __name__ == "__main__":
    solveDay9()