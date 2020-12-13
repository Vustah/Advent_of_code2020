import Advent_of_code2020 as aoc 

class BUS:
    def __init__(self, ID):
        self.ID = int(ID)
    
    def calc_minutes_to_departure(self):
        timeStamp = self.timeStamp
        bus_depart = self.ID
        while(True):
            if bus_depart>=timeStamp:
                break
            else:
                bus_depart += self.ID

        self.minutes_to_departure =  bus_depart-timeStamp

    def set_timeStamp(self, timeStamp):
        self.timeStamp = timeStamp
        self.calc_minutes_to_departure()

    def get_minutes_to_departure(self):
        return self.minutes_to_departure

    def get_ID(self):
        return self.ID

def solve():
    buslines = aoc.importFile("13122020.txt")
    earlies_depart = int(buslines[0])
    bus_lines = buslines[1].split(",")
    Busses = []
    for line in bus_lines:
        if line != "x":
            Busses.append(BUS(int(line)))

    earlies_depart_bus = {
        "BusLine": 0,
        "Minutes_to_depart": 10e100
    }

    for Bus in Busses:
        Bus.set_timeStamp(earlies_depart)
        minutes_to_departure = Bus.get_minutes_to_departure()
        if minutes_to_departure < earlies_depart_bus["Minutes_to_depart"]:
            earlies_depart_bus["BusLine"] = Bus.get_ID()
            earlies_depart_bus["Minutes_to_depart"] = minutes_to_departure
        print(earlies_depart_bus)    


    print(earlies_depart_bus["BusLine"]*earlies_depart_bus["Minutes_to_depart"])
            


if __name__ == "__main__":
    solve()