import streamlit as st
import main
import sqlite3 as sql
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)

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
              
                 
                  
         
        
              
                 
             
                  
                     
                  
                     
           
            
               
               
                 
                 
                   
            
                   