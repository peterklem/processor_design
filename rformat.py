from decimaltobinary import *


def rformat(command,boolflag):
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

        if boolflag == False:
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 0 '  + str(Rn) +  ' ' +  str(Rd)

        else:
            opcode = decimaltobinary(opcode,11)
            Rd = decimaltobinary(Rd,5)
            Rn = decimaltobinary(Rn,5)
            Rm = decimaltobinary(Rm,5)
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 000000 '  + str(Rn) +  ' ' +  str(Rd)



    elif command_stripped[0] == 'SUB':
        opcode = 1624
        if boolflag == False:
            return_str = str(opcode) + ' ' + str(Rm) + ' 0 ' + str(Rn) + ' ' + str(Rd)

        else:
            opcode = decimaltobinary(opcode, 11)
            Rd = decimaltobinary(Rd, 5)
            Rn = decimaltobinary(Rn, 5)
            Rm = decimaltobinary(Rm, 5)
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 000000 '  + str(Rn) +  ' ' +  str(Rd)

    elif command_stripped[0] == 'AND':
        opcode = 1104
        if boolflag == False:
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 0 '  + str(Rn) +  ' ' +  str(Rd)

        else:
            opcode = decimaltobinary(opcode, 11)
            Rd = decimaltobinary(Rd, 5)
            Rn = decimaltobinary(Rn, 5)
            Rm = decimaltobinary(Rm, 5)
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 000000 '  + str(Rn) +  ' ' +  str(Rd)

    elif command_stripped[0] == 'ORR':
        opcode = 1360
        if boolflag == False:
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 0 '  + str(Rn) +  ' ' +  str(Rd)

        else:
            opcode = decimaltobinary(opcode, 11)
            Rd = decimaltobinary(Rd, 5)
            Rn = decimaltobinary(Rn, 5)
            Rm = decimaltobinary(Rm, 5)
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 000000 '  + str(Rn) +  ' ' +  str(Rd)

    elif command_stripped[0] == 'EOR':
        opcode = 1616
        if boolflag == False:
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 0 '  + str(Rn) +  ' ' +  str(Rd)

        else:
            opcode = decimaltobinary(opcode, 11)
            Rd = decimaltobinary(Rd, 5)
            Rn = decimaltobinary(Rn, 5)
            Rm = decimaltobinary(Rm, 5)
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 000000 '  + str(Rn) +  ' ' +  str(Rd)

    elif command_stripped[0] == 'LSL':
        opcode = 1691

        if boolflag == False:
            return_str = str(opcode) + ' X ' + str(shamt) + " " + str(Rn) + " " + str(Rd)
        else:
            opcode = decimaltobinary(opcode,11)
            Rd = decimaltobinary(Rd,5)
            Rn = decimaltobinary(Rn,5)
            shamt = decimaltobinary(shamt,6)
            return_str = str(opcode) + ' 00000 ' + str(shamt) + " " + str(Rn) + " " + str(Rd)


    elif command_stripped[0] == 'LSR':
        opcode = 1690
        if boolflag == False:
            return_str = str(opcode) + ' X ' +  str(shamt) + " " + str(Rn) + " " + str(Rd)

        else:
            opcode = decimaltobinary(opcode, 11)
            Rd = decimaltobinary(Rd, 5)
            Rn = decimaltobinary(Rn, 5)
            shamt = decimaltobinary(shamt, 6)
            return_str = str(opcode) + ' 00000 ' +  str(shamt) + " " + str(Rn) + " " + str(Rd)

    elif command_stripped[0] == 'SUBS':
        opcode = 1880
        if boolflag == False:
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 0 '  + str(Rn) +  ' ' +  str(Rd)

        else:
            opcode = decimaltobinary(opcode, 11)
            Rd = decimaltobinary(Rd, 5)
            Rn = decimaltobinary(Rn, 5)
            Rm = decimaltobinary(Rm, 5)
            return_str = str(opcode) + ' ' +  str(Rm) +  ' 000000 '  + str(Rn) +  ' ' +  str(Rd)

    return return_str


