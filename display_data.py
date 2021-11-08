import main
import sqlite3 as sql
import streamlit as st
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)


# The new employee has been added
def display_bank():
    """
    To display all the banks registered in the database
    :return:
    """
    st.write("The banks which our registered are:")
    for row in connect.execute("SELECT * FROM bank"):
        st.write(row)


def display_branch():
    """
    display all the branches registered in the database
    :return:
    """
    st.write("The number of branches which our registered are as follows: ")
    for row in connect.execute("SELECT * FROM branch"):
        st.write(row)


def display_employee():
    """
    display all the employees present in the database
    :return:
    """
    st.write("The number of employee which are registered are as follows: ")
    for row in connect.execute("SELECT * FROM employee"):
        st.write(row)


def display_customer():
    """
    display all the customer present in the database
    :return:
    """
    st.write("The number of customer registered are as follows: ")
    for row in connect.execute("SELECT * FROM customer"):
        st.write(row)


def display_loan():
    """
    display all the loans present in the database
    :return: None
    """
    st.write("Number of people who have taken loan are: ")
    for row in connect.execute("SELECT * FROM loan"):
        st.write(row)
