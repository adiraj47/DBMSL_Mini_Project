import streamlit as st
import main
import sqlite3 as sql
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)
def deposit():
    cur=connect.cursor()
    with st.form("deposit_form1"):   
        id=st.number_input("Enter the id of the Customer")
        acc=st.number_input("Enter the account no of the Customer")
        amt=st.number_input("Enter the amount to deposit")
        deposit_cust_form25 = st.form_submit_button("submit")
        if deposit_cust_form25 :
            cur.execute("SELECT ACC_BAL FROM account WHERE CUST_ID = ?", (id,))
            row = cur.fetchone()
            amount=row[0]
            if row:
                amount=amount+amt
                cur.execute("UPDATE account  SET  ACC_BAL=? WHERE CUST_ID = ?", (amount,id,))
                cur.connection.commit()
                st.write("Amount has been deposited.Below is the balance")
                st.write("Rs",amount)
            else:
                st.write("Account does not exist")
def withdraw():
    cur=connect.cursor()
    with st.form("withdraw_form1"):   
        id=st.number_input("Enter the id of the Customer")
        acc=st.number_input("Enter the account no of the Customer")
        amt=st.number_input("Enter the amount to withdraw")
        withdraw_cust_form2 = st.form_submit_button("submit")
        if withdraw_cust_form2:
            cur.execute("SELECT ACC_BAL FROM account WHERE CUST_ID = ?", (id,))
            row = cur.fetchone()
            amount=row[0]
            if amount-amt>=5000:
                amount=amount-amt
                cur.execute("UPDATE account  SET  ACC_BAL=? WHERE CUST_ID = ?", (amount,id,))
                cur.connection.commit()
                st.write("Amount has been withdrawn.Below is the balance")
                st.write("Rs",amount)
            else:
                 st.write("Dear Customer,You do not have sufficient balance to withdraw")
def add_acount():
    cur=connect.cursor()
    with st.form("dept_form1"):
        ifsc=st.text_input("Enter the ifsc of the Bank")
        id=st.number_input("Enter the id of the Customer")
        acc=st.number_input("Enter the account no of the Customer")
        dept_cust_form2 = st.form_submit_button("submit")
        acc_bal=5000
        if  dept_cust_form2:
            cur.execute("SELECT * FROM depos_with WHERE CUST_ID = ?", (id,))
            row = cur.fetchone()
            if row:
                  st.write(f"Customer account already present")
            else:
                cur.execute("INSERT INTO account VALUES(?,?,?)",(acc,id,acc_bal))
                cur.connection.commit()
                cur.execute("INSERT INTO br_acc VALUES(?,?)",(ifsc,acc))
                cur.connection.commit()
                cur.execute("INSERT INTO depos_with  VALUES (?, ?)" ,(id,acc))
                cur.connection.commit()
                st.write("Account added successfullyn with minimum amount:Rs 5000")
              
                 
                  
         
        
              
                 
             
                  
                     
                  
                     
           
            
               
               
                 
                 
                   
            
                   
