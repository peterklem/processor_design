# Chooses which format type to use

def format_sorter(line):
    r_types = ['ADD', 'SUB', 'AND', 'ORR', 'EOR', 'LSL', 'LSR', 'SUBS']
    i_types = ['ADDI', 'SUBI', 'ANDI', 'ORRI', 'EORI', 'SUBIS']
    d_types = ['LDUR', 'STUR']
    cb_types = ['CBZ', 'CBNZ', 'B.EQ', 'B.NE', 'B.GT', 'B.LT', 'B.GE', 'B.LE']
    b_types = ['B']

    
    line_spl  = line.split()
    # Go through each list, and compare opcode from command
    if line_spl[0] in r_types:
        return 'r'
    elif line_spl[0] in i_types:
        return 'i'
    elif line_spl[0] in d_types:
        return 'd'
    elif line_spl[0] in cb_types:
        return 'cb'
    elif line_spl[0] in b_types:
        return 'b'
    else:
        return 'n'


# command = 'ADD X19, XZR, XZR'
# print(format_sorter(command))

command = 'SUBI X11, X11, #5'
print(format_sorter(command))

# command = '	STUR X14, [X10, #0]'
# print(format_sorter(command))

command = '	B.GE Exit'
print(format_sorter(command))

# command = '	B Loop'
# print(format_sorter(command))

# command = 'Loop:	SUBIS XZR, X19, #4'
# print(format_sorter(command))