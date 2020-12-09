import Advent_of_code2020 as aoc 

def solveDay8():
    program = aoc.importFile("08122020.txt")
    program_counter = 0
    program_length = len(program)
    program_finished = program_run(program_counter,program_length,program)
    
    for idx, line in enumerate(program):
        new_program = program.copy()
        operation, operation_cmd = line.split(" ")[:2]
        operation_cmd = int(operation_cmd)
        if operation == "jmp":
            print("jmp changed to nop")
            new_program[idx] = "nop "+ str(operation_cmd) + " #Changed from " + line
        if operation == "nop":
            print("nop changed to jmp")
            new_program[idx] = "jmp "+ str(operation_cmd) + " #Changed from " + line

        program_finished = program_run(program_counter,program_length,new_program)
        if program_finished:
            print_file(new_program)
            print("Program successpully ended")
            break
        
def print_file(contents):
    f = open("08122020_new_program.txt","w")
    for line in contents:
        f.write(line)
    f.close()

def program_run(program_counter,program_length,program):
    accumulator = 0
    program_counter_history = []
    while(program_counter < program_length):
        operation, operation_cmd = program[program_counter].split(" ")[:2]
        operation_cmd = int(operation_cmd)
        if program_counter in program_counter_history:
            print(accumulator)
            break

        program_counter_history.append(program_counter)

        if operation == "nop":
            program_counter += 1
        elif operation == "acc":
            accumulator += operation_cmd
            program_counter += 1
        elif operation == "jmp":
            program_counter += operation_cmd

    #print(program_counter_history)

    if program_counter >=program_length:
        print(accumulator)
        return True
    else:
        return False

    




if __name__ == "__main__":
    solveDay8()
