def cb_format(command, binary_flag, goto_dict, current_line):
    # Format line
    command = command.upper()
    command_split = command.split()
    for item in command_split:
        item.strip()
    
    # Assign variables
    opcode = command_split[0]
    address = ''
    Rt = ''
    current_line

    # Check if it is a CBZ/CBNZ or a B.cond
    if opcode[0] == 'B':
        print('B')
    elif opcode[0] == 'C':
        opcode_dec = 84
        print('C')

    # 
    if opcode == 'CBZ':
        opcode_dec = 180
    elif opcode == 'CBNZ':
        opcode_dec = 181
    elif opcode == 'B.EQ':
        pass
        # Rt_dec =
    elif opcode == 'B.NE':
        pass
        # Rt_dec =
    elif opcode == 'B.GT':
        pass
        # Rt_dec =
    elif opcode == 'B.GE':
        pass
        # Rt_dec =
    elif opcode == 'B.LT':
        pass
        # Rt_dec =
    elif opcode == 'B.LE':
        pass
        # Rt_dec =
    else:
        # Not a cb-format command
        print("This is not a CB-format command.")

goto_dict = {}
goto_dict['Loop'] = 3
goto_dict['Exit'] = 10

command = 'CBNZ Loop'

cb_format(command, False, goto_dict)