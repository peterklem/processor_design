from fetch_instruction_type import *
from decode import *
from alu import alu
# Import data memory


def readregister():
    pass



##################### MAIN #########################

#Setting up the register dictionary


reg_dict = {}
for i in range(32):
    reg_dict[i] = 0

reg_dict['ZR'] = 0


DMEM = {}
for i in range(10):
    DMEM[i] = 0

with open('out2.txt', 'r') as f:    mem_list = [i.strip() for i in f.readlines()]

IMEM = {}
for i in range(len(mem_list)):
    IMEM[i] = mem_list[i]

print('IMEM contents:\n\n')
print(IMEM + '\n\n')

file1 = open()
# Manual input for data memory
for i in range(10):
    choice = input('Press 1 to change DMEM values or 0 to stop: ')
    choice = int(choice)
    if choice != 1: # Stop
        break
    elif choice == 1: # Change MEM value
        DMEM_address = input('Enter from 1 to 10 the DMEM address you want to change: ')
        value = input('Enter value inside the DMEM: ')
        value = int(value)
        DMEM[DMEM_address] = value

print('The memory should update to these values:\n\n')
print(DMEM)

