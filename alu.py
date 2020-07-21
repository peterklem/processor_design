def alu(opcode_text, in_reg1, in_reg2=-1):
    # ALU for all opcode types

    # R and I format cases

    # ADD, ADDI
    if opcode_text in ['ADD', 'ADDI']:
        return in_reg1 + in_reg2
    # SUB, SUBI 
    elif opcode_text in ['SUB', 'SUBI']:
        return in_reg1 - in_reg2
    # AND
    elif opcode_text in ['AND', 'ANDI']:
        return in_reg1 & in_reg2
    # ORR
    elif opcode_text in ['ORR', 'ORRI']:
        return in_reg1 | in_reg2
    # EOR
    elif opcode_text in ['EOR', 'EORI']:
        return in_reg1 ^ in_reg2
    # LSL
    elif opcode_text == 'LSL':
        return in_reg1 << in_reg2
    # LSR
    elif opcode_text == 'LSR':
        return in_reg1 >> in_reg2
    # SUBS, SUBIS
    elif opcode_text in ['SUBS', 'SUBIS']:
        answer = in_reg1 - in_reg2
        # Check flags
        flags = {}
        flag['Negative'] = False
        flag['Zero'] = False
        if answer < 0:
            flag['Negative'] = True
        elif answer == 0:
            flag['Zero'] = True
        return [answer, flags] 

    # D-format functions

    elif opcode_text == 'STUR':
        return in_reg1 + in_reg2

    elif opcode_text == 'LDUR':
        return in_reg1 + in_reg2

    # CB and B-format functions
    elif opcode_text in ['B.EQ', 'B.NE', 'B.GT', 'B.LT', 'B.LE', 'B.GE', 'B']:
        return in_reg1 - in_reg2