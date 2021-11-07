import streamlit as st
import main
import sqlite3 as sql
import add_data as add
import display_data as display
import updation as updt
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)

side_box = st.sidebar.selectbox("What operation would you like to perform",
                                ("Home","Add", "Delete", "Update", "Display", "search"))
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



elif side_box == "Display":
    operation = st.selectbox("Please choose which display operation", ("bank", "customer", "employee", "loan"))
    if operation == "bank":
        display.display_bank()
    if operation == "customer":
        with st.form("customer_form"):
            display.display_customer()










