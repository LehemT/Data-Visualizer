
import numpy as np


def curve_fit(dict_list: list, attribute: str, order: int) -> str:
    """ When given a list of dictionaries, an attribute to call and an order, the function returns a string specifying the equation for the graph plotted from the input values.

    Preconditions: order must be from 1-5, and all dictionaries in the list must contain 'G_Avg' and have all the same keys.

    >>> curve_fit([{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg':12}, {'School': 'GP', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 16, 'G1': 6, 'G2': 5, 'G3': 5, 'G_Avg': 3}, {'School': 'GP', 'Age': 17, 'StudyTime': 1.0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10, 'G_Avg': 23}, {'School': 'MB', 'Age': 19, 'StudyTime': 2.0, 'Health': 5, 'Absences': 2, 'G1': 7, 'G2': 8, 'G3': 9,'G_Avg': 5}, {'School': 'MB', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 5, 'G2': 0, 'G3': 0, 'G_Avg': 4}, {'School': 'MB', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 0, 'G1': 6, 'G2': 7, 'G3': 0, 'G_Avg':9}], 'Age', 2)
    'y = -0.56x^2 + 17.75x + - 129.19'

    >>>curve_fit([{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg':12}, {'School': 'GP', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 16, 'G1': 6, 'G2': 5, 'G3': 5, 'G_Avg': 3}, {'School': 'GP', 'Age': 17, 'StudyTime': 1.0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10, 'G_Avg': 23}, {'School': 'MB', 'Age': 19, 'StudyTime': 2.0, 'Health': 5, 'Absences': 2, 'G1': 7, 'G2': 8, 'G3': 9,'G_Avg': 5}, {'School': 'MB', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 5, 'G2': 0, 'G3': 0, 'G_Avg': 4}, {'School': 'MB', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 0, 'G1': 6, 'G2': 7, 'G3': 0, 'G_Avg':9}], 'Health', 1)
    'y = -5.33x + 30.67'

    >>> curve_fit([{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg':12}, {'School': 'GP', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 16, 'G1': 6, 'G2': 5, 'G3': 5, 'G_Avg': 3}, {'School': 'GP', 'Age': 17, 'StudyTime': 1.0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10, 'G_Avg': 23}, {'School': 'MB', 'Age': 19, 'StudyTime': 2.0, 'Health': 5, 'Absences': 2, 'G1': 7, 'G2': 8, 'G3': 9,'G_Avg': 5}, {'School': 'MB', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 5, 'G2': 0, 'G3': 0, 'G_Avg': 4}, {'School': 'MB', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 0, 'G1': 6, 'G2': 7, 'G3': 0, 'G_Avg':9}], 'G3', 3)
    'y = 0.23x^3 + - 3.04x^2 + 8.83x + 6.5'

    """
    att_dict = {}
    for i in range(len(dict_list)):
        key = dict_list[i].get(attribute)

        if att_dict.get(key) == None:
            att_dict[key] = float(dict_list[i].get('G_Avg'))
        else:
            if type(att_dict[key]) != list:
                att_dict[key] = [att_dict[key]] + \
                    [float(dict_list[i].get('G_Avg'))]
            else:
                att_dict[key] = att_dict[key] + \
                    [float(dict_list[i].get('G_Avg'))]

    for j in att_dict:
        if type(att_dict[j]) == list:
            att_dict[j] = sum(att_dict[j]) / len(att_dict[j])

    grade_list = list(att_dict.values())
    key_list = list(att_dict.keys())

    if len(grade_list) <= order:
        coef = np.polyfit(key_list, grade_list, len(grade_list) - 1)
    else:
        coef = np.polyfit(key_list, grade_list, order)

    equation = 'y = '
    for k in range(len(coef)):
        power = len(coef) - k - 1
        coeff_string = str(round(coef[k], 2))
        if k > 0:
            coeff_string = coeff_string.replace('-', '- ')
        if power == 0:
            equation += coeff_string
        elif power == 1:
            equation += coeff_string + 'x + '
        else:
            equation += coeff_string + 'x^' + str(power) + ' + '
    equation = equation.strip(' +')

    return equation


# Do NOT include a main script in your submission
