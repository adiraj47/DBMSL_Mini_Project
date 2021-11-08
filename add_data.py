import main
import sqlite3 as sql
import streamlit as st
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)


def add_bank(id: int, name: str) -> None:
    """
    Adding the bank details in the database

    :param id: Primary key(Unique key) the way to find the
    :param name: The name of the bank
    :return: None
    """
    currsor = connect.cursor()
    currsor.execute("SELECT * FROM bank WHERE bank_id = ?", (id, ))
    row = currsor.fetchone()
    if row:
        st.write(f"Bank already present {row}")
    else:
        currsor.execute("INSERT INTO bank VALUES (?, ?)", (id, name))
        currsor.connection.commit()
        st.write(f"The New bank has been created {name}")


def add_branch(ifsc: int, address: str, name: str) -> None:
    """
    Adding the branch of the bank to the database
    :param ifsc: Enter the ifsc code
    :param address: the address of the bank.
    :param name: The name of the branch
    :return: None
    """
    currsor = connect.cursor()
    currsor.execute("SELECT * FROM branch WHERE ifsc = ?", (ifsc, ))
    row = currsor.fetchone()
    if row:
        print(f"The Brach is already present here our the details: {row}")
    else:
        currsor.execute("INSERT INTO branch VALUES (?, ?, ?)", (ifsc, address, name))
        currsor.connection.commit()
        print(f"""The new branch has been established:
        IFSC: {ifsc}
        Address: {address}
        name: {name}""")


def add_employee(id: int, name: str, email: str, address: str, joining_date: str) -> None:
    """
    Adding the employee details in the bank
    :param id: Primary key in which the id of employee is given
    :param name: The name of the employee
    :param email: E-mail id of the employeee
    :param address: address of the employee
    :param joining_date: joining date of the employee
    :return:
    """
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM employee WHERE EMP_ID = ?", (id, ))
    row = cursor.fetchone()
    if row:
        st.write(f"The employee already works here the details our: {row}")
    else:
        cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", (id, name, email, address, joining_date))
        cursor.connection.commit()
        st.write(f"""The new employee has been added with the following details: 
        Id: {id}
        Name: {name}
        Email-id: {id}
        Address: {address}
        Joining_date: {joining_date}""")


def add_employee_phone(id: int, phone_no: int) -> None:
    """
    Adding the employee phone number in the database
    :param id: id of the employee
    :param phone_no: phone number of the employee
    :return: None
    """
    cursor = connect.cursor()
    cursor.execute("INSERT INTO employee_phone VALUES (?, ?)", (id, phone_no))
    cursor.connection.commit()
    print(f"Phone number added for {id}")


def add_customer(cust_id: int, fname: str, mname: str, lname: str, cust_street: str, cust_city: str, cust_email: str):
    """
    Adding the customer details to the database
    :param cust_id: customer id (Primary key)
    :param fname: First name of the customer
    :param mname: Middle name of the customer
    :param lname: Last name of the customer
    :param cust_street: street in which customer lives
    :param cust_city: City in which customer lives
    :param cust_email: Email-id of the customer
    :return: None
    """
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM customer WHERE CUST_ID = ?", (cust_id, ))
    row = cursor.fetchone()

    if row:
        st.write(f"already a customer present for {cust_id} please select other id")
    else:
        cursor.execute("INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?)",(cust_id, fname, mname, lname, cust_street, cust_city, cust_email))
        cursor.connection.commit()
        st.write(f"Welcome {fname} to our bank")


def add_customer_phone(cust_id: int, cust_phone: int):
    """
    Adding the customer phone number of the customer
    :param cust_id: Id of the customer
    :param cust_phone: Phone of the customer
    :return: None
    """
    cursor = connect.cursor()
    cursor.execute("INSERT INTO customer_phone VALUES (?, ?)", (cust_id, cust_phone))
    cursor.connection.commit()

def add_loan(loan_no: int, cust_id: int, loan_amount: int):
    """
    Loan added to the database
    :param loan_no: loan id (Primary key)
    :param cust_id: customer id to link it
    :param loan_amount: the amount of loan taken by the customer
    :return: None
    """
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM loan WHERE CUST_ID = ?", (cust_id, ))
    row = cursor.fetchone()
    if row:
        st.write(f"The customer with {row[1]}has already taken the loan of {row[2]}")
    else:
        cursor.execute("INSERT INTO loan VALUES (?, ?, ?)", (loan_no, cust_id, loan_amount))
        st.write(f"A loan of {loan_amount} has been issued to {cust_id}.")
        cursor.connection.commit()
