import Advent_of_code2020 as aoc 

def format_seats(seats):
    seat_grid = []
    for idx, seat_line in enumerate(seats):
        seat_line = seat_line.replace("\n", "")
        seat_grid.append([])
        for seat in seat_line:
            seat_grid[idx].append(seat)
    return seat_grid

def get_range(min, maks, pos):
    offset = 1
    if pos <= min :
        start = pos
    else:
        start = pos - offset
    if pos >= maks :
        stop = pos
    else:
        stop = pos + offset
    return start, stop

def getSeats_Dim(seats):
    rows = len(seats)
    cols = len(seats[0])
    
    return rows, cols

def copy_seats(seats):
    seats_rows, seats_cols = getSeats_Dim(seats)
    new_seats = [["." for i in range(seats_cols)] for j in range(seats_rows)]
    return new_seats

def check_adjecent_seats(seats, pos_x, pos_y):
    number_of_ocupied_seats = 0
    seats_rows, seats_cols = getSeats_Dim(seats)
    x_start, x_stop = get_range(0,seats_cols, pos_x)
    y_start, y_stop = get_range(0,seats_rows, pos_y)
    
    for x in range(seats_rows):
        for y in range(seats_cols):
            if x >= x_start and x <= x_stop:
                if y >= y_start and y <= y_stop:
                    if x == pos_x and y == pos_y:
                        #print("S", end="")
                        pass
                    else:
                        if seats[x][y] == "#":
                            number_of_ocupied_seats += 1
                        #print(seats[x][y], end= "")
        #print()
    

    return number_of_ocupied_seats

def new_seatLayout(seats):
    new_seats = copy_seats(seats)
    seats_changed = False
    for pos_x,seat_row in enumerate(seats):
        for pos_y, seat in enumerate(seat_row):
            number_of_ocupied_seats = check_adjecent_seats(seats,pos_x,pos_y)
            if seat == "L" and number_of_ocupied_seats == 0:
                new_seats[pos_x][pos_y] = "#"
                seats_changed = True
            elif seat == "#" and number_of_ocupied_seats >= 4:
                new_seats[pos_x][pos_y] = "L"#str(number_of_ocupied_seats)#
                seats_changed = True
            else:
                new_seats[pos_x][pos_y] = seat
            
            #print("=", pos_x,pos_y, seat, new_seats[pos_x][pos_y], number_of_ocupied_seats)
            

    return new_seats, seats_changed

def print_seats(seats):
    str = ""
    for seat_row in seats:
        print(str.join(seat_row))
    print()

def count_seats(seats):
    count = 0
    for seat_row in seats:
        for seat in seat_row:
            if seat == "#":
                count+=1
    return count

def solve():
    seats = aoc.importFile("11122020.txt")  
    seat_grid = format_seats(seats)
    
    iteration = 0
    while(True):
        iteration += 1
        #print_seats(seat_grid)
        new_seat_grid,seat_changed = new_seatLayout(seat_grid)
        if seat_changed:
            seat_grid = new_seat_grid
        else:
            break
        print(iteration)

    print(count_seats(new_seat_grid))    

if __name__ == "__main__":
    solve()