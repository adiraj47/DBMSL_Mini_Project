import streamlit as st
import main
import sqlite3 as sql
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)

def update_emp():
    cur=connect.cursor()
    user_choice2=st.selectbox("Select the required updaion",["Name","Email id","Address","Phone no"],index=0)
    if(user_choice2=="Name"):
        with st.form("update_name_form1"):
            id=st.number_input("Enter the id of the employee")
            t=st.text_input("Please enter the new name of the employee")
            updt_employee_form2 = st.form_submit_button("submit")
            if updt_employee_form2 :
                cur.execute("SELECT * FROM employee WHERE EMP_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE EMPLOYEE SET EMP_NAME=? WHERE EMP_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Employee with the given id not present")
    elif(user_choice2=="Email id"):
        with st.form("update_name_form2"):
            id=st.number_input("Enter the id of the employee")
            t=st.text_input("Please enter the new email id of the employee")
            updt_employee_form3 = st.form_submit_button("submit")
            if updt_employee_form3 :
                cur.execute("SELECT * FROM employee WHERE EMP_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE EMPLOYEE SET EMP_EMAIL_ID=? WHERE EMP_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Employee with the given id not present")
    elif(user_choice2=="Address"):
        with st.form("update_name_form3"):
            id=st.number_input("Enter the id of the employee")
            t=st.text_input("Please enter the new address of the employee")
            updt_employee_form4 = st.form_submit_button("submit")
            if updt_employee_form4 :
                cur.execute("SELECT * FROM employee WHERE EMP_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE EMPLOYEE SET EMP_ADDRESS=? WHERE EMP_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Employee with the given id not present")
    elif(user_choice2=="Phone no"):
        with st.form("update_name_form4"):
            id=st.number_input("Enter the id of the employee")
            t=st.text_input("Please enter the new phone no of the employee")
            updt_employee_form5 = st.form_submit_button("submit")
            if updt_employee_form5:
                cur.execute("SELECT * FROM employee_phone WHERE EMP_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE EMPLOYEE_PHONE SET EMP_PHONE=? WHERE EMP_ID=?",(t,id,))
                    cur.connection.commit()

                    st.write("Updation done successfully") 
                else:
                    st.write(f"Employee with the given id not present")   
def update_cust():
    cur=connect.cursor()
    user_choice3=st.selectbox("Select the required updaion",["First Name","Middle Name","Last Name","Street","City","Email id","Phone no"],index=0)
    if(user_choice3=="First Name"):
        with st.form("update_cust_form1"):
            id=st.number_input("Enter the id of the Customer")
            t=st.text_input("Please enter the new First name of the Customer")
            updt_form1 = st.form_submit_button("submit")
            if updt_form1 :
                cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE CUSTOMER SET CUST_FNAME=? WHERE CUST_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Customer with the given id not present")
    elif(user_choice3=="Middle Name"):
        with st.form("update_cust_form2"):
            id=st.number_input("Enter the id of the Customer")
            t=st.text_input("Please enter the new Middle name of the Customer")
            updt_form2 = st.form_submit_button("submit")
            if updt_form2 :
                cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE CUSTOMER SET CUST_MNAME=? WHERE CUST_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Customer with the given id not present")
    elif(user_choice3=="Last Name"):
        with st.form("update_cust_form3"):
            id=st.number_input("Enter the id of the Customer")
            t=st.text_input("Please enter the new Last name of the Customer")
            updt_form3 = st.form_submit_button("submit")
            if updt_form3 :
                cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE CUSTOMER SET CUST_LNAME=? WHERE CUST_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Customer with the given id not present")
    elif(user_choice3=="Street"):
        with st.form("update_cust_form4"):
            id=st.number_input("Enter the id of the Customer")
            t=st.text_input("Please enter the new Street")
            updt_form4 = st.form_submit_button("submit")
            if updt_form4 :
                cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE CUSTOMER SET CUST_STREET=? WHERE CUST_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Customer with the given id not present")
    elif(user_choice3=="City"):
        with st.form("update_cust_form5"):
            id=st.number_input("Enter the id of the Customer")
            t=st.text_input("Please enter the new City")
            updt_form5 = st.form_submit_button("submit")
            if updt_form5 :
                cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE CUSTOMER SET CUST_CITY=? WHERE CUST_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Customer with the given id not present")
    elif(user_choice3=="Email id"):
        with st.form("update_cust_form6"):
            id=st.number_input("Enter the id of the Customer")
            t=st.text_input("Please enter the new Email Id of the Customer")
            updt_form6 = st.form_submit_button("submit")
            if updt_form6:
                cur.execute("SELECT * FROM CUSTOMER WHERE CUST_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE CUSTOMER SET CUST_EMAIL_ID=? WHERE CUST_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Customer with the given id not present")
    elif(user_choice3=="Phone no"):
        with st.form("update_cust_form7"):
            id=st.number_input("Enter the id of the Customer")
            t=st.text_input("Please enter the new phone no of the Customer")
            updt_form7 = st.form_submit_button("submit")
            if updt_form7:
                cur.execute("SELECT * FROM CUSTOMER_PHONE WHERE CUST_ID = ?", (id, ))
                row = cur.fetchone()
                if row:
                    cur.execute("UPDATE CUSTOMER_PHONE SET CUST_PHONE=? WHERE CUST_ID=?",(t,id,))
                    cur.connection.commit()
                    st.write("Updation done successfully") 
                else:
                    st.write(f"Customer with the given id not present")

