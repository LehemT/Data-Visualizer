
from load_data import *
from sort import *
from curve_fit import *
from histogram import *

user_interface = True
data_load = ""
sorting_dict = {'age': "Age", 'studytime': "StudyTime",
                'failures': "Failures", "g_avg": "G_Avg"}
curve_dict = {'school': 'School', 'age': 'Age', 'studytime': 'StudyTime', 'failures': 'Failures',
              'g_avg': 'G_Avg', 'g1': 'G1', 'g2': 'G2', 'g3': 'G3', 'absences': 'Absences', 'health': 'Health'}

while user_interface:
    command = input(
        "\nThe available commands are:\n    L)oad Data\n    S)ort Data\n    C)urve Fit\n    H)istogram\n    E)xit\n\nPlease type your command: ").lower()
    if command == "l":
        file = input("Please enter the name of the file: ")
        attribute = input(
            "Please enter the attribute to use as a filter: ").lower().capitalize()
        valueofattribute = ""

        while attribute not in ["Age", "Health", "Failures", "School", "All"]:
            attribute = input(
                "Invalid Attribute! Please Enter a Valid Attribute: ").lower().capitalize()

        if attribute in ["Age", "Health", "Failures"]:
            while True:
                try:
                    valueofattribute = int(
                        input("Please enter the value of the attribute: "))
                    break
                except ValueError:
                    print("Invalid Value Of Attribute.", end=' ')

        if attribute == "School":
            valueofattribute = input(
                "Please enter the value of the attribute: ")

        try:
            data_load = add_average(
                load_data(file, (attribute, valueofattribute)))
            print("Data loaded")

        except FileNotFoundError:
            print("File Not Found. Please Enter A Valid File")
        except IndexError:
            print("File Not Formatted Properly")
        except:
            print("Unknown Error. Please Try Again")

    elif command == 's':
        if data_load == "":
            print("File not loaded. Please, load a file first. ")
        else:
            sort_valueofattributes = input(
                "Please enter the attribute you want to use for sorting:\n'Age'    'StudyTime'    'Failures'    'G_Avg'\n: ").lower()

            while sort_valueofattributes not in ['age', 'studytime', 'failures', 'g_avg']:
                sort_valueofattributes = input(
                    "Invalid Sort Key! Please Enter a Valid Sort Key: ").lower()

            sort_valueofattributes = sorting_dict[sort_valueofattributes]
            order = input(
                "Ascending (A) or Descending (D) order: ").capitalize()

            while order not in ["A", "D"]:
                order = input(
                    "Invalid Order Key. Please Enter An Order Key: ").capitalize()

            sort_data = sort(data_load, order, sort_valueofattributes)

            if input("Data Sorted. Do you want to display?[Y/N]: \n").capitalize() == 'Y':
                print(sort_data)

    elif command == 'c':
        if data_load == "":
            print("File not loaded. Please, load a file first. ")
        elif data_load == []:
            print("Data Provided Isn't Valid. Cannot Provide A CurveFit")
        else:
            print(
                'Please enter the attribute you want to use to find the best fit for\nG_Avg: ', end='')
            while True:
                curvecommand = input().lower()
                if curvecommand in data_load[0].keys() and curvecommand not in ['School', 'G_Avg']:
                    break
                elif curvecommand in ['age', 'health', 'studytime', 'failures', 'absences', 'g1', 'g2', 'g3']:
                    curvecommand = curve_dict.get(curvecommand, None)
                    if curvecommand in data_load[0].keys():
                        break
                print("Invalid command. Please enter a VALID attribute: ", end='')

            polyfit = input(
                "Please enter the order of the polynomial to be fitted: ")
            while polyfit not in ["1", "2", "3", "4", "5"]:
                polyfit = input(
                    "Invalid Fit. Please enter an interger value for 1 to 5: ")
            curvegraph = curve_fit(data_load, curvecommand, int(polyfit))
            print("The Equation That Will Fit This Data is: ", curvegraph)

    elif command == 'h':
        if data_load == "":
            print("File not loaded. Please, load a file first. ")
        elif data_load == []:
            print("Data Provided Isn't Valid. Cannot Provide A Histogram")
        else:
            print("Please enter the attribute you want to use for plotting: ", end='')
            while True:
                histocommand = input().lower()
                if histocommand in ["school", 'age', 'health', 'studytime', 'failures', 'absences', 'g1', 'g2', 'g3', "g_avg"]:
                    histocommand = curve_dict.get(histocommand, None)
                    if histocommand in data_load[0].keys():
                        break
                print("Invalid command. Please enter a VALID attribute: ", end='')

            histogram(data_load, histocommand)

    elif command == 'e':
        user_interface = False

    else:
        if data_load == "":
            print("No Such Command.")
        else:
            print("Invalid Command.")

