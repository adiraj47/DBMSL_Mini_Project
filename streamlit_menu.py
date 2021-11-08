import streamlit as st
import main
import sqlite3 as sql
import add_data as add
import display_data as display
import updation as updt
import search
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)

side_box = st.sidebar.selectbox("What operation would you like to perform",
                                ("Home","Add", "Delete", "Update", "Display", "Search"))
if side_box == "Home":
    st.title("Welcome to the bank management system")
    st.write("This page can perform basic CRUD applications like add, delete, update, display of all records")

elif side_box == "Add":
    operation = st.selectbox("Please choose which add opreation", ("Bank", "Customer", "Employee", "Loan"))
    if operation == "Bank":
        with st.form("bank_form"):

            bank_id = st.number_input("Please enter the bank id")
            bank_name = st.text_input("Please enter the bank name")
            bank_form = st.form_submit_button("submit")
            if bank_form:
                add.add_bank(bank_id, bank_name)
                st.write(bank_id, bank_name)
    elif operation == "Customer":
        with st.form("add_customer_form"):
            customer_id = st.number_input("Please enter the customer id")
            customer_fname = st.text_input("Please enter the first name of the customer")
            customer_mname = st.text_input("Please enter the middle name of the customer")
            customer_lname = st.text_input("Please enter the last name of the customer")
            customer_street = st.text_input("Please enter the street the name")
            customer_city = st.text_input("Please enter the city of the customer")
            customer_email_id = st.text_input("Please enter the email id of the customer")
            add_customer_form = st.form_submit_button("Submit")
            if add_customer_form:
                add.add_customer(customer_id, customer_fname, customer_mname, customer_lname, customer_street, customer_city, customer_email_id)
    elif operation == "Employee":
        with st.form("add_employee_form"):
            employee_id = st.number_input("Enter the id of the employee")
            employee_name = st.text_input("Please enter the name of the employee")
            employee_mail = st.text_input("Please enter the mail id of the employee")
            employee_address = st.text_input("Please enter the address of the employee here")
            employe_date_joining = st.text_input("Please enter the date in this format dd/mm/yy")

            employee_form = st.form_submit_button("submit")

            if employee_form:
                add.add_employee(employee_id, employee_name, employee_mail, employee_address, employe_date_joining)

    elif operation == "Loan":
        with st.form("add_loan_form"):
            loan_id = st.number_input("Please enter the loan id")
            cust_id = st.number_input("Please enter the customer id ")
            loan_amount = st.number_input("Please enter the amount of loan")
            loan_submit = st.form_submit_button("Submit")
            if loan_submit:
                add.add_loan(loan_id, cust_id, loan_amount)

elif side_box == "Display":
    operation = st.selectbox("Please choose which display operation", ("Bank", "Customer", "Employee", "Loan"))
    if operation == "Bank":
        display.display_bank()
    elif operation == "Customer":
        display.display_customer()
    elif operation == "Employee":
        display.display_employee()
    elif operation == "Loan":
        display.display_loan()
elif side_box == "Search":
    table = st.selectbox("Please choose in which table you want to search", ("Bank", "Customer", "Employee", "Loan"))
    if table == "Bank":
        search_element = st.selectbox("Please select according to which element you want to search: ", ("bank id", "Bank name"))
        if search_element == "bank id":
            value = st.number_input("Please enter the id you want to search")
            result = search.search("bank", "bank_id", value)
            st.write(result)
        elif search_element == "Bank name":
            value = st.text_input("Please enter the name of the bank:")
            result = search.search("bank", "bname", value)
            st.write(result)

    elif table == "Customer":
        search_element = st.selectbox("Please enter the searching parameter: ", ("Customer id", "First name", "City", "Email-id"))
        if search_element == "Customer id":
            value = st.number_input("Please enter the customer id you want to search: ")
            result = search.search("customer", "CUST_ID", value)
            st.write(result)
        elif search_element == "First name":
            value = st.text_input("Please enter the name of the customer: ")
            result = search.search("customer", "CUST_FNAME", value)
            st.write(result)
        elif search_element == "City":
            value = st.text_input("Please enter the city of the customer: ")
            result = search.search("customer", "CUST_CITY", value)
            st.write(result)
        elif search_element == "Email-id":
            value = st.text_input("Please enter the email id of the customer: ")
            result = search.search("customer", "CUST_EMAIL_ID", value)
            st.write(result)
    elif table == "Employee":
        search_element = st.selectbox("Please enter the search parameter", ("ID", "Name"))
        if search_element == "ID":
            value = st.number_input("Please enter the id of the employee: ")
            result = search.search("employee", "EMP_ID", value)
            st.write(result)
        elif search_element == "Name":
            value = st.text_input("Please enter the name of the employee: ")
            result = search.search("employee", "EMP_NAME", value)
            st.write(result)

    elif table == "Loan":
        search_element = st.selectbox("Please enter the search Parameter", ("ID", ))
        if search_element == "ID":
            value = st.number_input("Please enter the id of the loan")
            result = search.search("loan", "LOAN_NO", value)
            st.write(result)



















