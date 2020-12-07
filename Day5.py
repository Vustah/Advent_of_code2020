from Advent_of_code2020 import importFile

def solveDay5():
    contents = importFile("05122020.txt")
    num_rows = 127
    num_seats = 7
    seat_ID_max = 0
    seat_ID_list = []
    for seat_code in contents:
        seat_loc = [0,num_rows,0,num_seats]
        for letter in seat_code[0:7]:
            front_pos = seat_loc[0]
            back_pos = seat_loc[1]
            if letter == "F":
                next_back_pos = (back_pos-front_pos)/2+front_pos
                next_front_pos = front_pos

            elif letter == "B":
                next_back_pos = back_pos
                next_front_pos = (back_pos-front_pos+1)/2+front_pos
                
            seat_loc[0] = int(next_front_pos)
            seat_loc[1] = int(next_back_pos)        
        for letter in seat_code[7:]:
            upper_pos = seat_loc[2]
            lower_pos = seat_loc[3]
            if letter == "L":
                next_lower_pos = (lower_pos-upper_pos)/2+upper_pos
                next_upper_pos = upper_pos
            elif letter == "R":
                next_lower_pos = lower_pos
                next_upper_pos = (lower_pos-upper_pos+1)/2+upper_pos
            seat_loc[2] = int(next_upper_pos)
            seat_loc[3] = int(next_lower_pos)
        
        row = seat_loc[0]
        collumn = seat_loc[2]
        seat_ID = row*8+collumn
        seat_ID_list.append(seat_ID)
        if seat_ID>seat_ID_max:
            seat_ID_max = seat_ID
    print(seat_ID_max)
    seat_ID_list.sort()
    for i in range(1,len(seat_ID_list)-1):
        if seat_ID_list[i] != seat_ID_list[i-1]+1:
            print(seat_ID_list[i-1]+1)


if __name__ == "__main__":
    solveDay5()