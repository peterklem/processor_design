from decimaltobinary import *

def d_format(command, binary_flag):
    '''Takes a d-format instruction and translates it into decimal. Enter False in binary_flag for decimal, True for binary'''
    
    command = command.upper()
    split_comments = command.split('/')
    command_spl = split_comments[0].split()
    command_stripped = []
    #print(command_spl)
    for i in command_spl:
        command_stripped.append(i.strip(',X#[]'))
    #print(command_stripped)
    for item in command_stripped:
        if item == 'ZR':
            item = 0

    opcode = command_stripped[0]
    address = int(command_stripped[3])
    op2 = 0
    Rn = int(command_stripped[2])
    Rt = int(command_stripped[1])

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
        opcode_bin = decimaltobinary(opcode_dec, 11)
        address_bin = decimaltobinary(address, 9)
        op2 = decimaltobinary(op2, 2)
        Rn_bin = decimaltobinary(Rn, 5)
        Rt_bin = decimaltobinary(Rt, 5)
        return_str = str(opcode_bin) + ' ' + str(address_bin) + ' ' + str(op2) + ' ' + str(Rn_bin) + ' ' + str(Rt_bin)
        return return_str

# Testing
#command = 'LDUR X19, [X22, #0] // This is a comment'
#print(d_format(command, False))