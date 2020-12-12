import Advent_of_code2020 as aoc 

class Ship:
    def __init__(self, x_coor=0, y_coor=0, facing = 90):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.facing = facing

    def GoNorth(self, value):
        self.y_coor = self.y_coor+value
    def GoSouth(self, value):
        self.y_coor = self.y_coor-value

    def GoEast(self, value):
        self.x_coor = self.x_coor+value
    def GoWest(self, value):
        self.x_coor = self.x_coor-value

    def RotateShip(self,value):
        new_facing = self.facing + value
        while(True):
            if new_facing < 0:
                new_facing = (360 + new_facing)%360
            elif new_facing >= 360:
                new_facing = (new_facing)%360
            else:
                break
        self.facing = new_facing

    def receiveCommand(self, cmd, value):
        if cmd == "N":
            self.GoNorth(value)    
        elif cmd == "S":
            self.GoSouth(value)
        
        elif cmd == "E":
            self.GoEast(value)
        elif cmd == "W":
            self.GoWest(value)

        elif cmd == "L":
            self.RotateShip(-1*value)
        elif cmd == "R":
            self.RotateShip(value)

        elif cmd == "F":
            if self.facing == 0:
                self.GoNorth(value)
            elif self.facing == 90:
                self.GoEast(value)
            elif self.facing == 180:
                self.GoSouth(value)
            elif self.facing == 270:
                self.GoWest(value)

    def getLocation(self):
        return self.x_coor, self.y_coor
    
    def getFacing(self):
        return self.facing

    def getManhattenTraveled(self):
        return abs(self.x_coor) + abs(self.y_coor)

def solve():
    navigation = aoc.importFile("12122020.txt")
    CruiseShip = Ship()
    print("%s->%3s | F: %3d (%5d,%5d)" %(" "," ", CruiseShip.getFacing(),CruiseShip.getLocation()[0],CruiseShip.getLocation()[1]))
    for instruction in navigation:
        cmd = instruction[0]
        value = int(instruction[1:])
        CruiseShip.receiveCommand(cmd, value)
        print("%s->%3.d | F: %3d (%5d,%5d)" %(cmd,value, CruiseShip.getFacing(),CruiseShip.getLocation()[0],CruiseShip.getLocation()[1]), CruiseShip.getManhattenTraveled())

    print(CruiseShip.getLocation())
    print(CruiseShip.getManhattenTraveled())

if __name__ == "__main__":
    solve()