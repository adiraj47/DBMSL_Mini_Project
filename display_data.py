import main
import sqlite3 as sql
main.data_creation()
connect = sql.connect("Bank.sqlite")


# The new employee has been added
def display_bank():
    """

    :return:
    """
    print("The banks which our registered are:")
    for row in connect.execute("SELECT * FROM bank"):
        print(row)


def display_branch():
    """

    :return:
    """
    print("The number of branches which our registered are as follows: ")
    for row in connect.execute("SELECT * FROM branch"):
        print(row)


def display_employee():
    """

    :return:
    """
    print("The number of employee which are registered are as follows: ")
    for row in connect.execute("SELECT * FROM employee"):
        print(row)