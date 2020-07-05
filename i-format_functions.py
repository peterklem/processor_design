def i_format(command, binary_flag):
    '''Takes an i-format instruction and translates it into decimal'''

    # Parse the line to get useful data
    command_spl = command.split()
    command_stripped = []
    for i in command_spl:
        command_stripped.append(i.strip(',X#'))

    # Save parsed data to variables
    opcode_str = command_stripped[0]
    Rd = int(command_stripped[1])
    Rn = int(command_stripped[2])
    immediate = int(command_stripped[3])

    opcode_dec = 0
    return_str = ""     # Holds the string to be returned

    if opcode_str == 'ADDI':
        opcode_dec = 580
    elif opcode_str == 'SUBI':
        opcode_dec = 836
    elif opcode_str == 'ANDI':
        opcode_dec = 584
    elif opcode_str == 'ORRI':
        opcode_dec = 712
    elif opcode_str == 'EORI':
        opcode_dec = 840
    elif opcode_str == 'SUBIS':
        opcode_dec = 964


    if binary_flag == False:     # Receive answer in decimal
        return_str = str(opcode_dec) + ' ' + str(Rd) + ' ' + str(Rn) + ' ' + str(immediate)
        return return_str
    else:                        # Receive answer in binary
        opcode_bin = bin(opcode_dec) # Convert op to binary
        Rd_bin = bin(Rd)
        Rn_bin = bin(Rn)
        imm_bin = bin(immediate)

        return_str = str(opcode_bin) + ' ' + str(Rd_bin) + ' ' + str(Rn_bin) + ' ' + str(imm_bin)
        return return_str
        

    



print(i_format('ADDI X9, X21, #10', True))

