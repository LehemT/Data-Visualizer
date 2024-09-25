
def test_return_list():

    # test that student_school_list returns a list (3 different test cases required)

    check.equal(type(student_school_list(

        "student-test.csv", ("School", "GP"))), list)

    check.equal(type(student_school_list(

        "student-test.csv", ("School", "CF"))), list)

    check.equal(type(student_school_list(

        "student-test.csv", ("School", "MS"))), list)

    # test that student_age_list returns a list (3 different test cases required)

    check.equal(type(student_age_list(

        "student-test.csv", ("Age", 15))), list)

    check.equal(type(student_age_list(

        "student-test.csv", ("Age", 16))), list)

    check.equal(type(student_age_list(

        "student-test.csv", ("Age", 17))), list)

    # test that student_health_list returns a list (3 different test cases required)

    check.equal(type(student_health_list(

        "student-test.csv", ("Health", 3))), list)

    check.equal(type(student_health_list(

        "student-test.csv", ("Health", 4))), list)

    check.equal(type(student_health_list(

        "student-test.csv", ("Health", 5))), list)

   # test that student_failures_list returns a list (3 different test cases required)

    check.equal(type(student_failures_list(

        "student-test.csv", ("Failures", 0))), list)

    check.equal(type(student_failures_list(

        "student-test.csv", ("Failures", 1))), list)

    check.equal(type(student_failures_list(

        "student-test.csv", ("Failures", 2))), list)

    # test that load_data returns a list (6 different test cases required)

    check.equal(type(load_data("student-test.csv", ("School", "MB"))), list)

    check.equal(type(load_data("student-test.csv", ("Age", 18))), list)

    check.equal(type(load_data("student-test.csv", ("StudyTime", 2.0))), list)
    check.equal(type(load_data("student-test.csv", ("Failures", 3))), list)

    check.equal(type(load_data("student-test.csv", ("Absences", 10))), list)

    check.equal(type(load_data("student-test.csv", ("G1", 8))), list)

    # test that add_average returns a list (3 different test cases required)

    check.equal(type(add_average([{'School': 'GP', 'Study Time': 2.0,

                'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8}])), list)

    check.equal(type(add_average([{'School': 'GP', 'Study Time': 3.0,

                'Failures': 0, 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14}])), list)

    check.equal(type(add_average([{'School': 'GP', 'Study Time': 2.0,

                'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18}])), list)

    check.summary()

# Place test_return_list_correct_lenght function here


def test_return_list_correct_lenght():
    # Complete the function with your test cases

    # test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(student_school_list("student-test.csv", "GP")), 3)
    check.equal(len(student_school_list("student-test.csv", "MS")), 4)
    check.equal(len(student_school_list("student-test.csv", "CF")), 3)

    # test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_age_list("student-test.csv", 18)), 4)
    check.equal(len(student_age_list("student-test.csv", 16)), 2)
    check.equal(len(student_age_list("student-test.csv", 19)), 0)

    # test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_health_list("student-test.csv", 3)), 8)
    check.equal(len(student_health_list("student-test.csv", 4)), 3)
    check.equal(len(student_health_list("student-test.csv", 1)), 1)

    # test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(len(student_failures_list("student-test.csv", 0)), 11)
    check.equal(len(student_failures_list("student-test.csv", 2)), 2)
    check.equal(len(student_failures_list("student-test.csv", 6)), 0)

    # test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data("student-test.csv", ("School", "GP"))), 3)
    check.equal(len(load_data("student-test.csv", ("Age", 17))), 6)
    check.equal(len(load_data("student-test.csv", ("Failures", 2))), 2)
    check.equal(len(load_data("student-test.csv", ("School", "BD"))), 3)
    check.equal(len(load_data("student-test.csv", ("Age", 19))), 0)
    check.equal(len(load_data("student-test.csv", ("Failures", 0))), 11)

    # test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(add_average([])), 0)
    check.equal(len(add_average([{'School': 'GP', 'Study Time': 2.0,
                'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])), 1)
    check.equal(len(add_average([{'School': 'MB', 'StudyTime': 1.0, 'Failures': 0, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}, {
                'School': 'CF', 'StudyTime': 5.0, 'Failures': 2, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}])), 2)

    check.summary()


# Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():

    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(student_school_list('student-mat.csv', 'GP')
                [0], {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(student_school_list('student-mat.csv', 'CF')[-1], {
                'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 13, 'G2': 11, 'G3': 11})
    check.equal(student_school_list('student-mat.csv', 'MB')
                [0], {'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5})

    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(student_age_list('student-mat.csv', 15)
                [0], {'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8})
    check.equal(student_age_list('student-mat.csv', 16)[-1], {
                'School': 'BD', 'Study Time': 1.0, 'Failures': 0, 'Absences': 3, 'G1': 0, 'G2': 8, 'G3': 9})
    check.equal(student_age_list('student-mat.csv', 18)
                [0], {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 3, 'G1': 6, 'G2': 5, 'G3': 6})

    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(student_health_list('student-mat.csv', 3)
                [0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(student_health_list('student-mat.csv', 4)[-1], {
                'School': 'MS', 'Age': 20, 'StudyTime': 2.0, 'Failures': 2, 'Absences': 11, 'G1': 9, 'G2': 9, 'G3': 9})
    check.equal(student_health_list('student-mat.csv', 5)
                [0], {'School': 'GP', 'Age': 15, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15})

    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(student_failures_list('student-mat.csv', 0)
                [0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(student_failures_list('student-mat.csv', 1)[-1], {
                'School': 'MS', 'Age': 18, 'StudyTime': 2.0, 'Health': 5, 'Absences': 0, 'G1': 6, 'G2': 5, 'G3': 0})
    check.equal(student_failures_list('student-mat.csv', 2)
                [0], {'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Health': 5, 'Absences': 14, 'G1': 6, 'G2': 9, 'G3': 8})

    # test that load_data returns a correct dictionary inside the list (6 different test cases required)
    check.equal(load_data('student-mat.csv', ('Age', 16))
                [0], {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 5, 'G1': 4, 'G2': 6, 'G3': 10})
    check.equal(load_data('student-mat.csv', ('School', 'CF'))[-1], {
                'Age': '17', 'Study Time': 2.0, 'Failures': 0, 'Absences': 3, 'G1': 2, 'G2': 13, 'G3': 11})
    check.equal(load_data('student-mat.csv', ('Failures', 0))
                [0], {'School': 'GP', 'Age': 18, 'Study Time': 2.0, 'Absences': 3, 'G1': 6, 'G2': 5, 'G3': 6})
    check.equal(load_data('student-mat.csv', ('Absences', 5))[-1], {
                'School': 'MS', 'Age': 19, 'Study Time': 1.0, 'Failures': 0, 'G1': 5, 'G2': 8, 'G3': 9})
    check.equal(load_data('student-mat.csv', ('G2', 8))
                [0], {'School': 'GP', 'Age': 16, 'Study Time': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 4, 'G3': 10})
    check.equal(load_data('student-mat.csv', ('G3', 15))[-1], {
                'School': 'MS', 'Age': 18, 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 15})

    # test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)
    check.equal(add_average([{'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8},
                             {'School': 'GP', 'Study Time': 3.0, 'Failures': 0,
                                 'Absences': 5, 'G1': 2, 'G2': 15, 'G3': 14},
                             {'School': 'GP', 'Study Time': 2.0, 'Failures': 0, 'Absences': 1, 'G1': 0, 'G2': 16, 'G3': 18}])[0],
                {'School': 'GP', 'Study Time': 2.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 7, 'G3': 8, 'G_Avg': 8.33})
    check.equal(add_average([{'School': 'CF', 'Study Time': 6.0, 'Failures': 2, 'Absences': 5, 'G1': 7, 'G2': 3, 'G3': 5},
                             {'School': 'MB', 'Study Time': 1.0, 'Failures': 1,
                                 'Absences': 1, 'G1': 17, 'G2': 4, 'G3': 12},
                             {'School': 'CF', 'Study Time': 3.0, 'Failures': 5, 'Absences': 6, 'G1': 17, 'G2': 0, 'G3': 19}])[-1],
                {'School': 'CF', 'Study Time': 3.0, 'Failures': 5, 'Absences': 6, 'G1': 17, 'G2': 0, 'G3': 19, 'G_Avg': 12.0})
    check.equal(add_average([{'School': 'GP', 'Study Time': 5.0, 'Failures': 7, 'Absences': 6, 'G1': 18, 'G2': 17, 'G3': 6},
                             {'School': 'MB', 'Study Time': 2.0, 'Failures': 4,
                                 'Absences': 7, 'G1': 12, 'G2': 24, 'G3': 9},
                             {'School': 'MB', 'Study Time': 1.0, 'Failures': 1, 'Absences': 4, 'G1': 9, 'G2': 5, 'G3': 21}])[0],
                {'School': 'GP', 'Study Time': 5.0, 'Failures': 7, 'Absences': 6, 'G1': 18, 'G2': 17, 'G3': 6, 'G_Avg': 13.67})

    check.summary()

# Place test_add_average function here


def test_add_average():

  # Complete the function with your test cases

    # test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)

    check.equal(len(load_data('student-test.csv', ('School', "GP"))),
                (len(add_average(load_data('student-test.csv', ('School', "GP"))))))

    check.equal(len(load_data('student-test.csv', ('Age', 18))),
                (len(add_average(load_data('student-test.csv', ('Age', 18))))))

    check.equal(len(student_health_list('student-test.csv', 3)),
                (len(add_average(student_health_list('student-test.csv', 3)))))

    check.equal(len(load_data('student-test.csv', ('Failures', 0))),
                (len(add_average(load_data('student-test.csv', ('Failures', 0))))))

    check.equal(len(load_data('student-test.csv', ('All',))),
                (len(add_average(load_data('student-test.csv', ('All',))))))

    # test that the function returns an empty list when it is called whith an empty list

    empty_list = []

    check.equal(len(add_average(empty_list)), 0)

    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)

    check.equal(len(load_data('student-test.csv', ('All',))
                [0]), len(add_average(load_data('student-test.csv', ('All',)))[0]) - 1)

    check.equal(len(load_data('student-test.csv', ('School', "BD"))[0]), len(
        add_average(load_data('student-test.csv', ('School', "BD")))[0]) - 1)

    check.equal(len(load_data('student-test.csv', ('Absences', 4))[0]), len(
        add_average(load_data('student-test.csv', ('Absences', 4)))[0]) - 1)

    check.equal(len(load_data('student-test.csv', ('Age', 17))
                [0]), len(add_average(load_data('student-test.csv', ('Age', 17)))[0]) - 1)

    check.equal(len(student_health_list('student-test.csv', 5)
                [0]), len(add_average(student_health_list('student-test.csv', 5))[0]) - 1)

    # test that the G_Avg value is properly calculated  (5 different test cases required)

    check.within(add_average(load_data('student-test.csv', ('All', )))[0]["G_Avg"], (load_data('student-test.csv', ('All',))[
                 0]["G1"] + load_data('student-test.csv', ('All',))[0]["G2"] + load_data('student-test.csv', ('All',))[0]["G3"]) / 3, 0.01)

    check.within(add_average(load_data('student-test.csv', ('School', 'CF')))[0]["G_Avg"], (load_data('student-test.csv', ('School', 'CF'))[
                 0]["G1"] + load_data('student-test.csv', ('School', 'CF'))[0]["G2"] + load_data('student-test.csv', ('School', 'CF'))[0]["G3"]) / 3, 0.01)

    check.within(add_average(student_health_list('student-test.csv', 3))[0]["G_Avg"], (student_health_list('student-test.csv', 3)[
                 0]["G1"] + student_health_list('student-test.csv', 3)[0]["G2"] + student_health_list('student-test.csv', 3)[0]["G3"]) / 3, 0.01)

    check.within(add_average(load_data('student-test.csv', ('Failures', 0)))[0]["G_Avg"], (load_data('student-test.csv', ('Failures', 0))[
                 0]["G1"] + load_data('student-test.csv', ('Failures', 0))[0]["G2"] + load_data('student-test.csv', ('Failures', 0))[0]["G3"]) / 3, 0.01)

    check.within(add_average(load_data('student-test.csv', ('Age', 17)))[0]["G_Avg"], (load_data('student-test.csv', ('Age', 17))[
                 0]["G1"] + load_data('student-test.csv', ('Age', 17))[0]["G2"] + load_data('student-test.csv', ('Age', 17))[0]["G3"]) / 3, 0.01)

    check.summary()


# Do NOT include a main script in your submission
