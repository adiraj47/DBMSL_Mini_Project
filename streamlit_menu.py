import streamlit as st
import main
import sqlite3 as sql
import add_data as add
import display_data as display
import updation as updt
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)

side_box = st.sidebar.selectbox("What operation would you like to perform",
                                ("Home","Add", "Delete", "Update", "Display"))
if side_box == "Home":
    st.title("Welcome to the bank management system")
    st.write("This page can perform basic CRUD applications like add, delete, update, display of all records")

elif side_box == "Add":
    operation = st.selectbox("Please choose which add opreation", ("bank", "customer", "employee", "loan"))
    if operation == "bank":
        with st.form("bank_form"):

            bank_id = st.number_input("Please enter the bank id")
            bank_name = st.text_input("Please enter the bank name")
            bank_form = st.form_submit_button("submit")
            if bank_form:
                add.add_bank(bank_id, bank_name)
                st.write(bank_id, bank_name)
elif side_box == "Display":
    operation = st.selectbox("Please choose which display operation", ("bank", "customer", "employee", "loan"))
    if operation == "bank":
        display.display_bank()









