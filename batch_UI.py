
from load_data import *
from sort import *
from curve_fit import *
from histogram import *


while(True):

    data = []

    filename = input(
        'Please enter the name of the file where your commands are stored:')

    try:

        file = open(filename, 'r')

        for line in file:
            commands = line.strip().split(';')

            if(commands[0].upper() == 'L'):
                data = add_average(
                    load_data(commands[1], (commands[2], commands[3])))
                print('Data Loaded')

            elif(commands[0].upper() == 'S'):
                data = sort(data, commands[2], commands[1])
                print('Data Sorted')
                if(commands[3] == 'Y'):
                    print(data)

            elif(commands[0].upper() == 'C'):

                print(curve_fit(data, commands[1], int(commands[2])))

            elif(commands[0].upper() == 'H'):
                histogram(data, commands[1])

            elif(commands[0].upper() == 'E'):
                exit()
            else:
                print('Invalid Batch File')

    except (FileExistsError, FileNotFoundError):
        print('Invalid File Name')



