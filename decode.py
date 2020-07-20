from format_sorter import *
def decode(goto_dict, command):
    return_list = []
    format = format_sorter(command)
    command_split = command.split()
    if format == 'r':
        command_split[3] = int(command_split[3])
        return_list.append(goto_dict[command_split[3]])
        if command_split[0] in ['LSL', 'LSR']:
            command_split[2] = int(command_split[2])
            return_list.append(goto_dict[command_split[2]])
        else:
            command_split[1] = int(command_split[1])
            return_list.append(goto_dict[command_split[1]])

    elif format == 'i':
        command_split[2] = int(command_split[2])
        return_list.append(goto_dict[command_split[2]])

    elif format == 'd':
        command_split[3] = int(command_split[3])
        return_list.append(goto_dict[command_split[3]])

    elif format == 'cb':
        return_list.append(goto_dict[command_split[2]])

    return return_list

