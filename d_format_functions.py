def d_format(command, binary_flag):
    '''Takes a d-format instruction and translates it into decimal. Enter False in binary_flag for decimal, True for binary'''
    
    command = command.upper()
    command_spl = command.split()
    command_stripped = []
    #print(command_spl)
    for i in command_spl:
        command_stripped.append(i.strip(',X#[]'))
    #print(command_stripped)

    opcode = command_stripped[0]
    address = command_stripped[3]
    op2 = 0
    Rn = command_stripped[2]
    Rt = command_stripped[1]

    opcode_dec = 0 # Holds decimal opcode
    return_str = "" # Holds string to be returned
    if opcode == 'LDUR':
        opcode_dec = 1986
    elif opcode == 'STUR':
        opcode_dec = 1984
    if binary_flag == False: # Return code in decimal
        return_str = str(opcode_dec) + ' ' + str(address) + ' ' + str(op2) + ' ' + str(Rn) + ' ' + str(Rt)
        return return_str
    else:                     # Return code in binary
        pass

# Testing
# command = 'LDUR X19, [X22, #0]'
# print(d_format(command, False))