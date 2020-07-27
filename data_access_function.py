#goto_dict will be the data memory dictionary
#goto_dict2 will be the register dictionary

def data_access(goto_dict,  goto_dict2, command):
    command_split = command.split()
    command_split[1] = int(command_split[1])
    command_split[4] = int(command_split[4])

    if command_split[0] == 'LDUR':
        goto_dict2[command_split[4]] = goto_dict[command_split[1]]

    elif command_split[0] == 'STUR':
        goto_dict[command_split[1]] = goto_dict2[command_split[4]]


