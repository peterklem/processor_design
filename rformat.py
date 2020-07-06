from decimaltobinary import *


def rformatdecimal(command):
    command_spl = command.split()
    command_stripped = []
    for i in command_spl:
        command_stripped.append(i.strip(',X#'))
    print(command_stripped)

    if command_stripped[0] in ['ADD','SUB','AND','ORR','EOR','SUBS']:
        Rd = int(command_stripped[1])
        if command_stripped[2] == 'ZR':
            Rn = 0
        else:
            Rn = int(command_stripped[2])

        if command_stripped[3] == 'ZR':
            Rm = 0
        else:
            Rm = int(command_stripped[3])

    elif command_stripped[0] in ['LSL','LSR']:
        Rd = int(command_stripped[1])
        Rn = int(command_stripped[2])
        shamt = int(command_stripped[3])

    if command_stripped[0] == 'ADD':
        opcode = 1112
        print(opcode, " ", Rm, " 0 ", Rn, " ", Rd)



    elif command_stripped[0] == 'SUB':
        opcode = 1624
        print(opcode, " ", Rm, " 0 ", Rn, " ", Rd)

    elif command_stripped[0] == 'AND':
        opcode = 1104
        print(opcode, " ", Rm, " 0 ", Rn, " ", Rd)

    elif command_stripped[0] == 'ORR':
        opcode = 1360
        print(opcode, " ", Rm, " 0 ", Rn, " ", Rd)

    elif command_stripped[0] == 'EOR':
        opcode = 1616
        print(opcode, " ", Rm, " 0 ", Rn, " ", Rd)

    elif command_stripped[0] == 'LSL':
        opcode = 1691
        print(opcode, " X ", shamt , " ", Rn, " ", Rd)

    elif command_stripped[0] == 'LSR':
        opcode = 1690
        print(opcode, " X ", shamt, " ", Rn, " ", Rd)

    elif command_stripped[0] == 'SUBS':
        opcode = 1880
        print(opcode, " ", Rm, " 0 ", Rn, " ", Rd)




