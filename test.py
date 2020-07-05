# R-format
command = 'ADD X9, X21, X22'

command_spl = command.split()
print(command_spl)
command_stripped = []
for i in command_spl:
    command_stripped.append(i.strip(',X'))
print(command_stripped)



# I-format
command = 'ADDI X9, X21, #10'
command_spl = command.split()
print(command_spl)
command_stripped = []
for i in command_spl:
    command_stripped.append(i.strip(',X#'))
print(command_stripped)

# D-format
command = 'LDUR X19, [X22, #0]'
command_spl = command.split()
print(command_spl)
command_stripped = []
for i in command_spl:
    command_stripped.append(i.strip(',X#[]'))
print(command_stripped)


#CB-format
command = 'B.EQ Exit'
command_spl = command.split()
print(command_spl)