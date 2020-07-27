from decimaltobinary import *

def i_format(command, binary_flag):
    '''Takes an i-format instruction and translates it into decimal. Enter False in binary_flag for decimal, True for binary'''

    # Parse the line to get useful data
    command = command.upper()
    split_comments = command.split('/')
    command_spl = split_comments[0].split()
    command_stripped = []
    for i in command_spl:
        command_stripped.append(i.strip(',X#'))

    #print(command_stripped)

    # Save parsed data to variables
    opcode_str = command_stripped[0]
    immediate = int(command_stripped[3])

    # Need to check for XZR register

    if command_stripped[1] == 'ZR':
        Rd = 0
    else:
        Rd = int(command_stripped[1])

    if command_stripped[2] == 'ZR':
        Rn = 0
    else:
        Rn = int(command_stripped[2])

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
        return_str = str(opcode_dec) + ' ' + str(immediate) + ' ' + str(Rn) + ' ' + str(Rd)
        return return_str
    else:                        # Receive answer in binary
        opcode_bin = decimaltobinary(opcode_dec, 10) # Convert op to binary
        Rd_bin = decimaltobinary(Rd, 5)
        Rn_bin = decimaltobinary(Rn, 5)
        imm_bin = decimaltobinary(immediate, 12)

        return_str = str(opcode_bin) + ' ' + str(imm_bin) + ' ' + str(Rn_bin) + ' ' +  str(Rd_bin)
        return return_str
        

    


 #Testing
print(i_format('ADDI X9, X21, #10 //This is a comments', False))

