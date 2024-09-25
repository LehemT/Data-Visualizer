
import string


def student_school_list(file_name: str, school_name: str) -> list[dict]:
    """
    Return the list of students that attend a specified school from the stored data.

    Precondition: file_name in boundary.
    Precondition: schoole_name in file_name.

    >>> student_school_list('student-mat.csv','GP')
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},
     {another element},
     ]

    >>> student_school_list('student-mat.csv','CF')
    [{'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12},
     {another element},
     ]

    >>> student_school_list('student-mat.csv','MS')
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 11, 'G2': 11, 'G3': 11},
     {another element},
     ]

    >>> student_school_list('student-mat.csv','AB')
    []
    """

    student_list = []

    with open(file_name, "r") as infile:

        for line in infile:
            student_data = line.strip().split(',')

            if student_data[0] == school_name:

                student_dict = {'Age': int(student_data[1]), 'StudyTime': float(student_data[2]), 'Failures': int(student_data[3]), 'Health': int(
                    student_data[4]), 'Absences': int(student_data[5]), 'G1': int(student_data[6]), 'G2': int(student_data[7]), 'G3': int(student_data[8])}

                student_list.append(student_dict)

    for student_dict in student_list:

        for a, b in (student_dict.copy()).items():
            if(a == 'School'):
                student_dict.pop('School')

    return student_list


#==========================================#
# Place your student_health_list function after this line


def student_health_list(filename: str, student_health: int) -> list[dict]:
    """
    Returns a list of students whose health equals the condition of 2(poor), removing the health component from the list and pasting everything else about the student.

    Preconditions: 1 <= student_health <= 5

    >>>student_health_list('student-mat.csv', 2)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, {'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, {'School': 'GP', 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'G1': 13, 'G2': 14, 'G3': 14}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 8, 'G2': 10, 'G3': 12}, etc...] 

    >>>student_health_list('student-mat.csv', 1)
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 13, 'G2': 14, 'G3': 15}, {'School': 'GP', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 15, 'G2': 16, 'G3': 15}, etc...]

    >>>student_health_list('student-mat.csv', 6)
    []

    """
    finalhealthlist = []

    infile = open(filename, "r")
    line_1 = 1
    for line in infile:
        school_info = line.strip().split(',')
        if line_1 == 1:
            line_1 += 1
        elif int(school_info[4]) == student_health:
            tempdict = {'School': school_info[0], 'Age': int(school_info[1]), 'StudyTime': float(school_info[2]), 'Failures': int(
                school_info[3]), 'Absences': int(school_info[5]), 'G1': int(school_info[6]), 'G2': int(school_info[7]), 'G3': int(school_info[8])}

            finalhealthlist += [tempdict]

    return finalhealthlist

#==========================================#
# Place your student_age_list function after this line


def student_age_list(file_name: str, student_age: int) -> list[dict]:
    """
    Returns all the data for students from a list of students and data who match a given age parameter

    Preconditions: age >= 0, file_name must be a .csv

    Examples:
    >>>student_age_list('student-mat.csv', 15)
    [{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8}
    {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14}
    {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18}
    etc...]
    >>>student_age_list('student-mat.csv', 17)
    [{'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 3, 'G1': 4, 'G2': 5, 'G3': 5}
    {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 6, 'G2': 6, 'G3': 5}
    {'School': 'GP', 'Study Time': 1.0, 'Failures': 3, 'Absences': 5, 'G1': 16, 'G2': 6, 'G3': 5}
    etc...]
    >>>student_age_list('student-mat.csv', 0)
    []

    """
    file = open(file_name, 'r')
    output = []
    j = 0

    for line in file:
        values = line.split(",")
        tempdict = {'School': 0, 'Age': 0, 'Study Time': 0,
                    'Failures': 0, 'Absences': 0, 'G1': 0, 'G2': 0, 'G3': 0}
        i = 0
        for index, value in tempdict.items():
            tempdict[index] = values[i]
            i += 1
        if(j > 0 and tempdict['Age'] == str(student_age)):
            tempdict.pop('Age')
            output += [tempdict]

        j += 1
    file.close()
    for i in output:
        l = 0
        for a, b in i.items():
            if(l > 0):
                if(a == 'Study Time'):
                    i[a] = float(b)
                else:
                    i[a] = int(b)

            l += 1
    return output


#==========================================#
# Place your student_failures_list function after this line

def student_failures_list(filename: str, failure_number: int) -> list:
    """ when given a file name and the number of failures, the function return a list of dictionaries containing the information of a students with the specified number of failures.

    preconditions: the input file must be in the same

    >>> student_failures_list('student-mat.csv', 3)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'GP', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 16, 'G1': 6, 'G2': 5, 'G3': 5}, {another element}, ...]
    >>> student_failures_list('student-mat.csv', 0)
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {another element}, ...]
    >>> student_failures_list('student-mat.csv', 1)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 2.0, 'Health': 3, 'Absences': 25, 'G1': 7, 'G2': 10, 'G3': 11}, {'School': 'GP', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 14, 'G1': 10, 'G2': 10, 'G3': 9}, {another element}, ...]
    """

    final_failure_list = []

    infile = open(filename, 'r')
    firstline = 1
    for line in infile:
        info = line.strip().split(',')
        if firstline == 1:
            firstline += 1
        elif int(info[3]) == failure_number:
            temp = {'School': info[0], 'Age': int(info[1]), 'StudyTime': float(info[2]), 'Health': int(
                info[4]), 'Absences': int(info[5]), 'G1': int(info[6]), 'G2': int(info[7]), 'G3': int(info[8])}

            final_failure_list += [temp]

    return final_failure_list

#==========================================#
# Place your load_data function after this line


def load_data(file_name: str, data_to_get: tuple) -> list[dict]:
    """
    Returns the wanted data from an input file or returns all data if specified as 'All' given specifications

    Preconditions: data_to_get must be a valid data type, file_name must be a .csv

    >>> load_data('student-mat.csv', ('Age', 15))
    [{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8},
    {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14},
    {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18}...
    >>> load_data('student-mat.csv', ('Age', 17))
    [{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8},
    {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14},
    {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18}...
    >>> load_data('student-mat.csv', ('Age', 0))
    []
    """
    file = open(file_name, 'r')
    output = []
    j = 0

    for line in file:
        values = line.split(",")
        tempdict = {'School': 0, 'Age': 0, 'Study Time': 0, 'Failures': 0,
                    'Health': 0, 'Absences': 0, 'G1': 0, 'G2': 0, 'G3': 0}
        i = 0
        for index, value in tempdict.items():
            tempdict[index] = values[i]
            i += 1

        if(j > 0 and data_to_get[0] == 'All'):
            output += [tempdict]
        elif(j > 0 and tempdict[data_to_get[0]] == str(data_to_get[1])):
            tempdict.pop(data_to_get[0])
            output += [tempdict]

        j += 1
    file.close()
    for i in output:
        l = 0
        for a, b in i.items():
            if(l > 0):
                if(a == 'Study Time'):
                    i[a] = float(b)
                else:
                    i[a] = int(b)

            l += 1

    return output


#==========================================#
# Place your add_average function after this line


def add_average(list_of_dicts: list[dict]) -> list[dict]:
    """
    Returns the same given dictiionaries with an added key of G-Avg which represents the average of the three grades G1, G2, G3

    Precondtitions: list_of_dicts != None

    >>> add_average([{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8},
    {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14},
    {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18}...])
    [{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8, G_Avg: 8.33},
    {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 16, G_Avg: 11.00},
    {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 10, 'G2': 10, 'G3': 10, G_Avg: 10.00}...   
    >>> add_average([])
    []
    """
    output = list_of_dicts
    for i in output:
        avg = (int(i.get('G1')) + int(i.get('G2')) + int(i.get('G3')))
        avg = avg / 3
        avg = round(avg, 2)
        i['G_Avg'] = avg

    return output


# Do NOT include a main script in your submission

