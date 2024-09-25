
import matplotlib.pyplot as plt
import numpy as np


def histogram(student_list: list[dict], attribute: str):
    '''
    Returns a histogram using the specified list and chosen attribute.

    Precondition: type(value) == int or type(value) == float.
    Precondition: type(attribute) == str.

    >>> histogram([{'School': 'GP', 'Age': 18, 'Health': 3, 'G_Avg': 5.66}, {'School': 'MB', 'Age': 15, 'Health': 1, 'G_Avg': 7.01}, {'School': 'GP', 'Age': 16, 'Health': 2, 'G_Avg': 6.44}, {'School': 'CF', 'Age': 17, 'Health': 3, 'G_Avg': 8.00}], 'G_Avg')

    >>> histogram([{'School': 'GP', 'Age': 18, 'Health': 3, 'G_Avg': 5.66}, {'School': 'MB', 'Age': 15, 'Health': 1, 'G_Avg': 7.01}, {'School': 'GP', 'Age': 16, 'Health': 2, 'G_Avg': 6.44}, {'School': 'CF', 'Age': 17, 'Health': 3, 'G_Avg': 8.00}], 'Health')

    '''

    num_students = {}

    for student in student_list:
        value = student[attribute]
        # checks if value's type is integer or float
        if type(value) == int or type(value) == float:
            value = round(value)
        if value in num_students:
            num_students[value] += 1
        else:
            num_students[value] = 1

    # converts dictionary keys and values into a list and assigns to x and y (respectively)
    x = list(num_students.keys())
    y = list(num_students.values())

    plt.bar(x, y)  # creates a bar plot

    plt.title(f'Histogram of {attribute.capitalize()}')  # creat title
    plt.xlabel(attribute.capitalize())  # adds label to x-axis
    plt.ylabel('Number of Students')  # adds label to y-axis

    plt.show()  # displays the plot


# Do NOT include a main script in your submission
