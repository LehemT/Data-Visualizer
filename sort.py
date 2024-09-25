
def sort_students_failures_bubble(dict_list: list, order: str) -> list:
    """Given a list of dictionaries and a specified order, the function will return a a list of dictionaries containing 'Failures' in the order specified. If the dictionary does not contain the key 'Failures', the fucntion will return the message "'Failures' key is not present" and return the original list.

    Preconditions: The order input must be 'A' for asending order or 'D' for desending order.

    >>> sort_students_failures_bubble([{'School':'GP','Failures':12},{'School':'GP','Failures':33},{'School':'GP','Failures':10}], 'A')
    [{'School': 'GP', 'Failures': 10}, {'School': 'GP', 'Failures': 12}, {'School': 'GP', 'Failures': 33}]

     >>> sort_students_failures_bubble([{'School':'GP','Failures':12},{'School':'GP','Failures':33},{'School':'GP','Failures':10}], 'D')
    [{'School': 'GP', 'Failures': 33}, {'School': 'GP', 'Failures': 12}, {'School': 'GP', 'Failures': 10}]

    >>> sort_students_failures_bubble([{'School':'GP','Failures':12},{'School':'GP'},{'School':'GP','Failures':10}], 'A')
    'Failures' key is not present
    [{'School': 'GP', 'Failures': 12}, {'School': 'GP'}, {'School': 'GP', 'Failures': 10}]
    """
    arr = dict_list.copy()
    swap = True
    while swap:
        swap = False

        for i in range(len(dict_list) - 1):
            if dict_list[i].get('Failures') == None:
                print("'Failures' key is not present")
                return arr
            elif dict_list[i + 1].get('Failures') == None:
                print("'Failures' key is not present")
                return arr
            elif dict_list[i]['Failures'] > dict_list[i + 1]['Failures']:
                temp = dict_list[i]
                dict_list[i] = dict_list[i + 1]
                dict_list[i + 1] = temp
                swap = True

    if order == 'A':
        return dict_list
    if order == 'D':
        return dict_list[::-1]

#==========================================#
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(dict_list: list[dict], order: str) -> list[dict]:
    """
    Returns a list of dictionaries in order of ascending or descendng order depending on the order selected.

    Preconditions: order == "A" or order == "D"

    >>>sort_students_time_selection([{'School': 'GP', 'Age': 17, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19}, {'School': 'GP', 'Age': 15, 'StudyTime': 8.0, 'Failures': 0, 'Absences': 0, 'G1': 13, 'G2': 14, 'G3': 15}, {'School': 'GP', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 15, 'G2': 16, 'G3': 15},], "D")

    [{'School': 'GP', 'Age': 15, 'StudyTime': 8.0, 'Failures': 0, 'Absences': 0, 'G1': 13, 'G2': 14, 'G3': 15}, {'School': 'GP', 'Age': 17, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19}, {'School': 'GP', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 15, 'G2': 16, 'G3': 15}]


    >>>sort_students_time_selection([{'School': 'GP', 'Age': 17, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19}, {'School': 'GP', 'Age': 15, 'StudyTime': 8.0, 'Failures': 0, 'Absences': 0, 'G1': 13, 'G2': 14, 'G3': 15}, {'School': 'GP', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 15, 'G2': 16, 'G3': 15}], "A")

    [{'School': 'GP', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 15, 'G2': 16, 'G3': 15}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19}, {'School': 'GP', 'Age': 17, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 8.0, 'Failures': 0, 'Absences': 0, 'G1': 13, 'G2': 14, 'G3': 15}]

    >>>sort_students_time_selection([{'School': 'GP', 'Age': 15, 'Failures': 0, 'Absences': 4, 'G1': 15, 'G2': 16, 'G3': 15}], 'A')

    "StudyTime" key is not present
    [{'School': 'GP', 'Age': 15, 'Failures': 0, 'Absences': 4, 'G1': 15, 'G2': 16, 'G3': 15}]


    """

    dl = dict_list
    if len(dict_list) == 0:
        dl = [{}]
    if not dl[0].get("StudyTime"):
        print('"StudyTime" key is not present')

    elif order == "D":
        for i in range(len(dict_list)):
            min_index = i
            for x in range(i + 1, len(dict_list)):
                if dict_list[min_index]["StudyTime"] < dict_list[x]["StudyTime"]:
                    min_index = x

            dict_list[i], dict_list[min_index] = dict_list[min_index], dict_list[i]

    elif order == "A":
        for i in range(len(dict_list)):
            max_index = i
            for x in range(i + 1, len(dict_list)):
                if dict_list[max_index]["StudyTime"] > dict_list[x]["StudyTime"]:
                    max_index = x

            dict_list[i], dict_list[max_index] = dict_list[max_index], dict_list[i]

    return dict_list

#==========================================#
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(dictInput: list[dict], order: str) -> list[dict]:
    """
    Return a sorted list of dictionaries using the insertion sort sorting method evauting based on the G_Avg values.

    Preconditions: order == 'A' or order == 'D'

    >>>sort_students_g_avg_insertion([{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8, 'G_Avg': 8.33}, {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14, 'G_Avg': 10.33}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18, 'G_Avg': 11.33}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 14, 'G3': 15, 'G_Avg': 9.67}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 0, 'G2': 10, 'G3': 8, 'G_Avg': 8.67}, {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 4, 'G2': 10, 'G3': 12, 'G_Avg': 6.0}], 'D')
    [{'School': 'MB', 'Study Time': 1.0, 'Failures': 0, 'Absences': 3, 'G1': 10, 'G2': 18, 'G3': 19, 'G_Avg': 15.67}, {'School': 'GP', 'Study Time': 4.0, 'Failures': 0, 'Absences': 3, 'G1': 12, 'G2': 16, 'G3': 16, 'G_Avg': 14.67}, {'School': 'MB', 'Study Time': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 6, 'G2': 18, 'G3': 19, 'G_Avg': 14.33}, {'School': 'MB', 'Study Time': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 26, 'G2': 7, 'G3': 6, 'G_Avg': 13.0}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 19, 'G3': 18, 'G_Avg': 13.0}, {'School': 'MB', 'Study Time': 1.0, 'Failures': 0, 'Absences': 1, 'G1': 4, 'G2': 16, 'G3': 17, 'G_Avg': 12.33}]
    >>>sort_students_g_avg_insertion([{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8, 'G_Avg': 8.33}, {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14, 'G_Avg': 10.33}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18, 'G_Avg': 11.33}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 14, 'G3': 15, 'G_Avg': 9.67}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 0, 'G2': 10, 'G3': 8, 'G_Avg': 8.67}, {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 4, 'G2': 10, 'G3': 12, 'G_Avg': 2.67}], 'A')
    [{'School': 'MB', 'Study Time': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 0, 'G2': 8, 'G3': 0, 'G_Avg': 2.67}, {'School': 'MB', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 9, 'G3': 0, 'G_Avg': 3.0}, {'School': 'MB', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 11, 'G3': 0, 'G_Avg': 3.67}, {'School': 'MB', 'Study Time': 3.0, 'Failures': 2, 'Absences': 5, 'G1': 0, 'G2': 12, 'G3': 0, 'G_Avg': 4.0}, {'School': 'MB', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 0, 'G2': 6, 'G3': 7, 'G_Avg': 4.33}, {'School': 'GP', 'Study Time': 1.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 8, 'G3': 7, 'G_Avg': 5.0}]
    >>>sort_students_g_avg_insertion([], 'A')
    []
    >>>sort_students_g_avg_insertion([], 'F')
    None
    """
    if((order != 'A') and (order != 'D')):
        return None

    for i in range(0, (len(dictInput) - 1)):
        index = 0
        for i in range(0, len(dictInput) - 1):
            if(dictInput[index].get('G_Avg') > dictInput[index + 1]["G_Avg"]):
                dictInput[index], dictInput[index +
                                            1] = dictInput[index + 1], dictInput[index]
            index += 1

    if order == 'D':
        dictInput.reverse()
    return dictInput


#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_age_bubble(list_dict: list[dict], order: str) -> list[dict]:
    '''
    Return the sorted list of the specified list of dictionaries and sorting order.

    Precondition: len(list_dict) > 0.
    Precondition: order == 'A' or order == 'D'.

    >>>sort_students_age_bubble([{'Age':17,'School':'BD'}, {'Age':18,'School':'MS'}], 'D')
    [{'Age': 18, 'School': 'MS'}, {'Age': 17, 'School': 'BD'}]

    >>>sort_students_age_bubble([{'Age':16,'School':'GP'}, {'Age':15,'School': 'MS'}], 'A')
    [{'Age': 15, 'School': 'MS'}, {'Age': 16, 'School': 'GP'}]

    >>>sort_students_age_bubble([{'School':'GP'}, {'School': 'CF'}], 'A')
    "Age" key not present
    [{'School': 'GP'}, {'School': 'CF'}]

    '''
    if not list_dict:
        return []

    n = len(list_dict)

    for i in range(n):
        for j in range(0, n - i - 1):
            if 'Age' not in list_dict[j] or 'Age' not in list_dict[j + 1]:
                print('\"Age\" key not present')
                return list_dict
            if order == 'A':
                if list_dict[j]['Age'] > list_dict[j + 1]['Age']:
                    list_dict[j], list_dict[j
                                            + 1] = list_dict[j + 1], list_dict[j]
            elif order == 'D':
                if list_dict[j]['Age'] < list_dict[j + 1]['Age']:
                    list_dict[j], list_dict[j +
                                            1] = list_dict[j + 1], list_dict[j]
            else:
                return []

        return list_dict


#==========================================#
# Place your sort function after this line
def sort(dictInput: list[dict], order: str, choice: str) -> list[dict]:
    """
    Return a sorted list of dictionaries using the insertion sort sorting method evauting based on the choice values.

    Preconditions: order == 'A' or order == 'D'

    >>>sort_by_key([{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8, 'G_Avg': 8.33}, {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14, 'G_Avg': 10.33}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18, 'G_Avg': 11.33}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 14, 'G3': 15, 'G_Avg': 9.67}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 0, 'G2': 10, 'G3': 8, 'G_Avg': 8.67}, {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 4, 'G2': 10, 'G3': 12, 'G_Avg': 6.0}], 'D', 'G_Avg')
    [{'School': 'MB', 'Study Time': 1.0, 'Failures': 0, 'Absences': 3, 'G1': 10, 'G2': 18, 'G3': 19, 'G_Avg': 15.67}, {'School': 'GP', 'Study Time': 4.0, 'Failures': 0, 'Absences': 3, 'G1': 12, 'G2': 16, 'G3': 16, 'G_Avg': 14.67}, {'School': 'MB', 'Study Time': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 6, 'G2': 18, 'G3': 19, 'G_Avg': 14.33}, {'School': 'MB', 'Study Time': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 26, 'G2': 7, 'G3': 6, 'G_Avg': 13.0}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 19, 'G3': 18, 'G_Avg': 13.0}, {'School': 'MB', 'Study Time': 1.0, 'Failures': 0, 'Absences': 1, 'G1': 4, 'G2': 16, 'G3': 17, 'G_Avg': 12.33}]
    >>>sort_by_key([{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8, 'G_Avg': 8.33}, {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14, 'G_Avg': 10.33}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18, 'G_Avg': 11.33}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 14, 'G3': 15, 'G_Avg': 9.67}, {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 0, 'G2': 10, 'G3': 8, 'G_Avg': 8.67}, {'School': 'GP', 'Study Time': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 4, 'G2': 10, 'G3': 12, 'G_Avg': 2.67}], 'A', 'G_Avg')
    [{'School': 'MB', 'Study Time': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 0, 'G2': 8, 'G3': 0, 'G_Avg': 2.67}, {'School': 'MB', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 9, 'G3': 0, 'G_Avg': 3.0}, {'School': 'MB', 'Study Time': 3.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 11, 'G3': 0, 'G_Avg': 3.67}, {'School': 'MB', 'Study Time': 3.0, 'Failures': 2, 'Absences': 5, 'G1': 0, 'G2': 12, 'G3': 0, 'G_Avg': 4.0}, {'School': 'MB', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 0, 'G2': 6, 'G3': 7, 'G_Avg': 4.33}, {'School': 'GP', 'Study Time': 1.0, 'Failures': 0, 'Absences': 5, 'G1': 0, 'G2': 8, 'G3': 7, 'G_Avg': 5.0}]
    >>>sort_by_key([], 'A', Age)
    []
    >>>sort_by_key([], 'F', StudyTime)
    None
    """
    if(choice == 'Age'):
        return sort_students_age_bubble(dictInput, order)

    if(choice == 'StudyTime'):
        return sort_students_time_selection(dictInput, order)

    if(choice == 'G_Avg'):
        return sort_students_g_avg_insertion(dictInput, order)

    if(choice == 'Failures'):
        return sort_students_failures_bubble(dictInput, order)

    else:
        return ('Cannot be sorted as input "', choice, '" is not valid')


# Do NOT include a main script in your submission

