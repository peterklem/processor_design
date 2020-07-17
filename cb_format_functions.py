from decimaltobinary import *

def cb_format(command, binary_flag, goto_dict, current_line):
    # Format line
    line = 0
    return_str = ' '
    command = command.upper()
    split_comments = command.split('/')
    command_spl = split_comments[0].split()
    command_stripped = []
    for i in command_spl:
        command_stripped.append(i.strip(',X#'))
    print(command_stripped)


    ##### Go Through the dictionary and match the conditional word and then find the address
    if command_stripped[0] in ['B.EQ', 'B.NE', 'B.GT', 'B.LT', 'B.LE', 'B.GE']:
        for i in goto_dict:
            if i == command_stripped[1]:
                line = goto_dict[i]
        address = line - current_line

    if command_stripped[0] in ['B.EQ', 'B.NE', 'B.GT', 'B.LT', 'B.LE', 'B.GE']:
        for i in goto_dict:
            if i == command_stripped[1]:
                line = goto_dict[i]
        address = line - current_line



    if command_stripped[0] in ['B.EQ', 'B.NE', 'B.GT', 'B.LT', 'B.LE', 'B.GE']:
        if command_stripped[0] in ['B.GE']:
            opcode = 84
            if binary_flag == False:
                return_str = str(opcode) + ' ' + str(address) + ' 10'
            else:
                opcode = decimaltobinary(opcode,8)
                address = decimaltobinary(address,19)
                return_str = str(opcode) + ' ' + str(address) + ' 01010'


        elif command_stripped[0] in ['B.EQ']:
            opcode = 84
            if binary_flag == False:
                return_str = str(opcode) + ' ' + str(address) + ' 0'
            else:
                opcode = decimaltobinary(opcode,8)
                address = decimaltobinary(address,19)
                return_str = str(opcode) + ' ' + str(address) + ' 00000'

        elif command_stripped[0] in ['B.NE']:
            opcode = 84
            if binary_flag == False:
                return_str = str(opcode) + ' ' + str(address) + ' 1'
            else:
                opcode = decimaltobinary(opcode, 8)
                address = decimaltobinary(address, 19)
                return_str = str(opcode) + ' ' + str(address) + ' 00001'

        elif command_stripped[0] in ['B.GT']:
            opcode = 84
            if binary_flag == False:
                return_str = str(opcode) + ' ' + str(address) + ' 12'
            else:
                opcode = decimaltobinary(opcode, 8)
                address = decimaltobinary(address, 19)
                return_str = str(opcode) + ' ' + str(address) + ' 01100'

        elif command_stripped[0] in ['B.LE']:
            opcode = 84
            if binary_flag == False:
                return_str = str(opcode) + ' ' + str(address) + ' 13'
            else:
                opcode = decimaltobinary(opcode, 8)
                address = decimaltobinary(address, 19)
                return_str = str(opcode) + ' ' + str(address) + ' 01101'

        elif command_stripped[0] in ['B.LT']:
            opcode = 84
            if binary_flag == False:
                return_str = str(opcode) + ' ' + str(address) + ' 11'
            else:
                opcode = decimaltobinary(opcode, 8)
                address = decimaltobinary(address, 19)
                return_str = str(opcode) + ' ' + str(address) + ' 01011'

    elif command_stripped[0] in ['CBZ', 'CBNZ']:
        if command_stripped[0] in ['CBZ']:
            opcode = 180
            Rt = int(command_stripped[1])
            if binary_flag == False:
                return_str = str(opcode) + ' ' + str(address) + ' ' + str(Rt)
            else:
                opcode = decimaltobinary(opcode, 8)
                address = decimaltobinary(address, 19)
                Rt = decimaltobinary(Rt,5)
                return_str = str(opcode) + ' ' + str(address) + ' ' + str(Rt)

        elif command_stripped[0] in ['CBNZ']:
            opcode = 181
            Rt = int(command_stripped[1])
            if binary_flag == False:
                return_str = str(opcode) + ' ' + str(address) + ' ' + str(Rt)
            else:
                opcode = decimaltobinary(opcode, 8)
                address = decimaltobinary(address, 19)
                Rt = decimaltobinary(Rt, 5)
                return_str = str(opcode) + ' ' + str(address) + ' ' + str(Rt)

    return return_str


