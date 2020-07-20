def readregister():
    pass








##################### MAIN #########################

#Setting up the register dictionary


reg_dict = {}
for i in range(32):
    reg_dict[i] = 0

reg_dict['ZR'] = 0

print(reg_dict)

DMEM = {}
# Manual input for data memory
for i in range(10):
    choice = input('Press 1 to change DMEM values or 0 to stop: ')
    choice = int(choice)
    if choice == 0:
        break
    elif choice == 1:
        DMEM_address = input('Enter from 1 to 10 the DMEM address you want to change: ')
        value = input('Enter value inside the DMEM: ')
        value = int(value)
        DMEM[DMEM_address] = value

print(DMEM)

