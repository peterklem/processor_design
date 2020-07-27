def fetch_instruction(line):
    # Gets opcode in text form 
    split = line.split()
    opcode_dict = {} # To hold all opcodes in decimal and text.
    opcode_text = ''
    opcode_type = '' # r, i, d, cb, or b
    # R-format opcodes
    opcode_dict['ADD'] = '1112'
    opcode_dict['SUB'] = '1624'
    opcode_dict['AND'] = '1104'
    opcode_dict['ORR'] = '1360'
    opcode_dict['EOR'] = '1616'
    opcode_dict['LSL'] = '1691'
    opcode_dict['LSR'] = '1690'
    opcode_dict['SUBS'] = '1880'

    # I-format
    opcode_dict['ADDI'] = '580'
    opcode_dict['SUBI'] = '836'
    opcode_dict['ANDI'] = '584'
    opcode_dict['ORRI'] = '712'
    opcode_dict['EORI'] = '840'
    opcode_dict['SUBIS'] = '1928'

    # D-format
    opcode_dict['LDUR'] = '1986'
    opcode_dict['STUR'] = '1984'

    # CB-format
    opcode_dict['CBZ'] = '180'
    opcode_dict['CBNZ'] = '181'
    if split[0] == '84':
        # Determine comparison type
        if split[2] == '10':
            opcode_text = 'B.GE'
        elif split[2] == '0':
            opcode_text = 'B.EQ'
        elif split[2] == '1':
            opcode_text = 'B.NE'
        elif split[2] == '12':
            opcode_text = 'B.GT'
        elif split[2] == '13':
            opcode_text = 'B.LE'
        elif split[2] == '11':
            opcode_text = 'B.LT'
        else:
            raise Exception('CB format function does not have valid Rt value.')

    # B-format
    opcode_dict['B'] = 5

    for op in opcode_dict.items():
        if op[1] == split[0]:
            opcode_text = op[0]
    
    full_text = opcode_text
    for i in range(1, len(split)):
        full_text = full_text +  ' ' + split[i]
    return full_text

# print(fetch_instruction('84 11 10'))
# print(fetch_instruction('580 14 14 21'))

        
