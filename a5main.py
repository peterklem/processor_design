from fetch_instruction_type import *
from decode import *
from alu import alu
from data_access_function import *


# Import data memory


def readregister():
    pass


##################### MAIN #########################

# Setting up the register dictionary


RMEM = {}
for i in range(32):
    RMEM[i] = 0

RMEM['ZR'] = 0

DMEM = {}
for i in range(20):
    DMEM[i] = 0

with open('out2.txt', 'r') as f:    mem_list = [i.strip() for i in f.readlines()]

IMEM = {}
for i in range(len(mem_list)):
    IMEM[i] = mem_list[i]

print('IMEM contents:\n\n')
print(IMEM, '\n\n')

# Manual input for data memory
for i in range(10):
    choice = input('Press 1 to change DMEM values or 0 to stop: ')
    choice = int(choice)
    if choice != 1:  # Stop
        break
    elif choice == 1:  # Change MEM value
        DMEM_address = input('Enter from 1 to 10 the DMEM address you want to change: ')
        DMEM_address = int(DMEM_address)
        value = input('Enter value inside the DMEM: ')
        value = int(value)
        DMEM[DMEM_address] = value

print('The memory should update to these values:\n\n')
print(DMEM)

for i in range(len(mem_list)):
    full_text = fetch_instruction(IMEM[i])  # Fetch instruction
    text_split = full_text.split()
    last_entry = text_split[-1]
    opcode_text = text_split[0]
    last_entry = int(last_entry)
    data_list = decode(RMEM, full_text)  # Decode instruction and fetch registers
    # Instantiate register values
    reg1 = data_list[0]

    if len(data_list) == 2:
        reg2 = data_list[1]
    else:
        reg2 = int(text_split[1])
    result_alu = alu(text_split[0], reg1, reg2)  # Input registers into ALU
    # Update registers
    RMEM[last_entry] = result_alu
    if opcode_text in ['LDUR', 'STUR']:
        data_access(DMEM, RMEM, full_text)

# Print out registers at the end of simulation
reg_items = RMEM.items()
data_items = DMEM.items()

print('Register items: \n\n')
for reg in reg_items:
    print('Register: ', reg[0], '\tValue: ', reg[1])

for reg in data_items:
    print('Data memory: ', reg[0], '\tValue: ', reg[1])



