def cbformatdecimal(command):
    file1 = open(r"code3.txt", "r+")

    count = 0
    for line in file1:
        count += 1

    file1.close()

    command_spl = command.split()
    command_stripped = []
    for i in command_spl:
        command_stripped.append(i.strip(',X#'))
    print(command_stripped)

    count1 = 0  # This will count where we will see the conditional
    file2 = open(r"code3.txt", "r+")
    for j in range(count):
        c = file2.readline()
        d = c.split()

        ##### Since CBZ and B has a small difference
        if command_stripped[0] in ['B.EQ','B.NE','B.GT','B.LT','B.LE','B.GE']:
            if d[0] == command_stripped[1]:
                count1 +=1
                break
            else:
                count1 += 1

        elif command_stripped[0] in ['CBZ', 'CBNZ']:
            if d[0] == command_stripped[2]:
                count1 +=1
                break
            else:
                count1 += 1

    file2.close()


    count2 = 0 #Gonna use this to find the current line again
    file2 = open(r"code3.txt", "r+")
    for i in range(count):
        e = file2.readline()
        if e == command:
            count2 +=1
            break
        else:
            count2 +=1
    file2.close()

    address = count1 - count2



    if command_stripped[0] in ['B.EQ','B.NE','B.GT','B.LT','B.LE','B.GE']:
        if command_stripped[0] in ['B.GE']:
            opcode = 84
            print(opcode, ' ' , address, ' 10')

        elif command_stripped[0] in ['B.EQ']:
            opcode = 84
            print(opcode, ' ', address, ' 0')

        elif command_stripped[0] in ['B.NE']:
            opcode = 84
            print(opcode, ' ', address, ' 1')

        elif command_stripped[0] in ['B.GT']:
            opcode = 84
            print(opcode, ' ', address, ' 12')

        elif command_stripped[0] in ['B.LE']:
            opcode = 84
            print(opcode, ' ', address, ' 13')

        elif command_stripped[0] in ['B.LT']:
            opcode = 84
            print(opcode, ' ', address, ' 11')

    elif command_stripped[0] in ['CBZ','CBNZ']:
        if command_stripped[0] in ['CBZ']:
            opcode = 180
            Rt = int(command_stripped[1])
            print(opcode, ' ', address, ' ', Rt)

        elif command_stripped[0] in ['CBNZ']:
            opcode = 181
            Rt = int(command_stripped[1])
            print(opcode, ' ', address, ' ', Rt)