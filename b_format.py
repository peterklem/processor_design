from decimaltobinary import *

def b_format(command, binary_flag, goto_dict, current_line):

    line = 0
    command = command.split('//', 1)
    command_spl = command[0].split()
    command_stripped = []
    for i in command_spl:
        command_stripped.append(i.strip(',X#'))
    #print(command_stripped)

    for i in goto_dict:
        if i == command_stripped[1]:
            line = goto_dict[i]

            address = current_line - line

    opcode = 5
    if binary_flag == False:
        return_str = str(opcode) + ' ' + str(address)

    else:
        opcode = decimaltobinary(opcode,6)
        address = decimaltobinary(address,26)
        return_str = str(opcode) + ' ' + str(address)

    return return_str