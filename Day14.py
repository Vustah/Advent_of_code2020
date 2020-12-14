import Advent_of_code2020 as aoc 
import numpy as np
import re

class Memory:
    def __init__(self):
        self.mask = 0
        self.memory = {}
        self.memCheck = 0

    def setBitMask(self, mask):
        self.mask = mask
    
    def getBitMask(self):
        return self.mask
    
    def __insertValue_to_string(self, string, address, value):
            string_list = list(string)
            string_list[address] = value
            return ''.join(string_list)

    def writeMemory(self, address, value):
        mask_length = len(self.mask)
        printed_value = "0"*mask_length
        value = str(bin(value)[2:])
        value = value.zfill(mask_length)
        #print(value)
        for idx,char in enumerate(self.mask):
            #print(idx)
            if char == "X":
                printed_value = self.__insertValue_to_string(printed_value, idx, value[idx])
            elif char == "1":
                printed_value = self.__insertValue_to_string(printed_value, idx, "1")
            elif char == "0":
                printed_value = self.__insertValue_to_string(printed_value, idx, "0")
        
        self.memory[str(address)] = int(printed_value,2)

    def writeMemory_2(self, address, value):
        mask_length = len(self.mask)
        printed_address = "0"*mask_length
        address = str(bin(address)[2:])
        address = address.zfill(mask_length)
        Xes_pos = []
        for idx,char in enumerate(self.mask):
            if char == "X":
                printed_address = self.__insertValue_to_string(printed_address, idx, "X")
                Xes_pos.append(idx)
            elif char == "1":
                printed_address = self.__insertValue_to_string(printed_address, idx, "1")
            elif char == "0":
                printed_address = self.__insertValue_to_string(printed_address, idx, address[idx])

        Xes = printed_address.count("X")
        number_of_values = 2**Xes
        for i in range(number_of_values):
            str_i = bin(i)[2:].zfill(Xes)
            for idx, bit in enumerate(str_i):
                printed_address = self.__insertValue_to_string(printed_address,Xes_pos[idx],bit )
            #print(int(printed_address,2))
            #print(printed_address)
            self.memory[str(int(printed_address,2))] = int(value)


    def readMemory(self, address):
        try:
            return self.memory[str(address)]
        except KeyError:
            return None
    def readAllMemory(self):
        return self.memory

    def calcMemCheckSum(self):
        checkSum = 0
        for key,value in self.memory.items():
            checkSum += value
        self.memCheck = checkSum

    def getMemCheckSum(self):
        return self.memCheck

def findAddress(string):
    first_klemme = string.find("[")+1
    second_klemme = string.find("]")
    address = string[first_klemme:second_klemme]
    return address

def solve1():
    program = aoc.importFile("14122020.txt")
    MEM = Memory()

    for line in program:
        splitted_line = line.replace("\n","").split(" = ")
        cmd = splitted_line[0]
        value = splitted_line[1]
        if cmd == "mask":
            MEM.setBitMask(value)
        elif cmd[0:3] == "mem":

            address = findAddress(cmd)
            MEM.writeMemory(address,int(value))
        else:
            print("Faulty program")
            break
    
    #print(MEM.readAllMemory())
    MEM.calcMemCheckSum()
    print(MEM.getMemCheckSum())

def solve2():
    program = aoc.importFile("14122020.txt")
    MEM = Memory()

    for line in program:
        splitted_line = line.replace("\n","").split(" = ")
        cmd = splitted_line[0]
        value = splitted_line[1]
        if cmd == "mask":
            MEM.setBitMask(value)
        elif cmd[0:3] == "mem":

            address = findAddress(cmd)
            MEM.writeMemory_2(int(address),int(value))
        else:
            print("Faulty program")
            break
    
    #print(MEM.readAllMemory())
    MEM.calcMemCheckSum()
    print(MEM.getMemCheckSum())





if __name__ == "__main__":
    solve1()
    solve2()