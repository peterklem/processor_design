from i_format_functions import *
from d_format_functions import *
from cb_format_functions import *
from format_sorter import *

infile = 'code3.txt'       # input file locaition
outfile = 'out1.txt'       # output file location
binary_output = False   # If true, values will be ouptut in binary. If false, they will be output in decimal

if __name__ == '__main__':
    # Variables
    cmd_format = ''         # Holds the format type of the command
    jump_dict = {}          # Holds the jump label and line number
    count = 0               # Holds current line number in the input file
    jump_name = ''          # Temporarily holds the jump/goto label
    line_spl = []           # Holds line when it is split 
    line_converted = ''     # Holds return value from each of the functions 
    output_lines = []       # List of converted lines
    
    # Open file 
    with open(infile, 'r') as file:
        count = 1     # First line is line 1
        for line in file:       # Loop through the file, look for jumps
            cmd_format = format_sorter(line)
            if cmd_format == 'n':   # Jump detected
                print('Jump detected on line ' + str(count))
                line_spl = line.split()
                jump_name = line_spl[0].strip(':')
                print(jump_name)
                jump_dict[jump_name] = count
            count += 1
        
    # All jumps have been sorted and recorded. 
    with open(infile, 'r') as file:
        count = 1 # Starting on line 1
        for line in file:
            cmd_format = format_sorter(line)
            if cmd_format == 'r':
                pass
            elif cmd_format == 'i':
                line_converted = i_format(line, False)
            elif cmd_format == 'd':
                line_converted - d_format(line, False)
            elif cmd_format == 'cb':
                pass
            elif cmd_format == 'b':
                pass
            else:
                # line is either bad or starts with a jump
                # split up line and compare first entry with all entries in jump_dict
                line_spl = line.split()
                print(line_spl)
                line_edited = ''
                for item in range(len(line_spl) - 1):
                    line_edited += line_spl[item + 1] + ' '
                # line_edited is now a valid line 
                cmd_format = format_sorter(line)
                if cmd_format == 'r':
                    pass
                elif cmd_format == 'i':
                    pass
                elif cmd_format == 'd':
                    pass
                elif cmd_format == 'cb':
                    pass
                elif cmd_format == 'b':
                    pass
                else:
                    print("Line " + str(count) + " is not a valid LEGv8 command")
            count += 1

