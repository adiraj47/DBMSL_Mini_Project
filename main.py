import sqlite3 as sql


def data_creation():
    connect = sql.connect("Bank.sqlite")
    connect.execute("CREATE TABLE IF NOT EXISTS bank  (bank_id NUMBER(30) PRIMARY KEY, bname VARCHAR(30))")

    connect.execute("CREATE TABLE IF NOT EXISTS branch (ifsc VARCHAR(30) PRIMARY KEY, address VARCHAR(30), "
                    "name VARCHAR(30))")

    connect.execute("CREATE TABLE IF NOT EXISTS employee (EMP_ID NUMBER(30) PRIMARY KEY, EMP_NAME VARCHAR(30),"
                    "EMP_EMAIL_ID VARCHAR(30), EMP_ADDRESS VARCHAR(50), EMP DATE)")

    connect.execute("CREATE TABLE IF NOT EXISTS employee_phone (EMP_ID NUMBER(30) REFERENCES employee(EMP_ID) ,"
                    "EMP_PHONE NUMBER(30))")

    connect.execute("CREATE TABLE IF NOT EXISTS customer (CUST_ID NUMBER(30) PRIMARY KEY,CUST_FNAME VARCHAR(20),"
                    "CUST_MNAME VARCHAR(20),CUST_LNAME VARCHAR(20),CUST_STREET VARCHAR(10),CUST_CITY VARCHAR(10),"
                    "CUST_EMAIL_ID VARCHAR(20))")

    connect.execute("CREATE TABLE IF NOT EXISTS customer_phone(CUST_ID NUMBER(30)  REFERENCES customer(CUST_ID),"
                    "CUST_PHONE NUMBER(30))")

    connect.execute("CREATE TABLE IF NOT EXISTS account(ACC_NO NUMBER(30) PRIMARY KEY,"
                    "CUST_ID NUMBER(30) REFERENCES customer(CUST_ID),"
                    "ACC_BAL NUMBER(10,2))")

    connect.execute("CREATE TABLE IF NOT EXISTS loan(LOAN_NO NUMBER(10) PRIMARY KEY,"
                    "CUST_ID NUMBER(30) REFERENCES customer(CUST_ID),"
                    "LOAN_AMOUNT NUMBER(10,2))")

    connect.execute("CREATE TABLE IF NOT EXISTS bank_b(IFSC VARCHAR(30)  REFERENCES branch(IFSC),"
                    "BANK_ID NUMBER(30) REFERENCES bank(BANK_ID))")

    connect.execute("CREATE TABLE IF NOT EXISTS br_emp(IFSC VARCHAR(30)  REFERENCES branch(IFSC),"
                    "EMP_ID NUMBER(30) REFERENCES employee(EMP_ID))")

    connect.execute("CREATE TABLE IF NOT EXISTS br_acc(IFSC VARCHAR(30)  REFERENCES branch(IFSC),"
                    "ACC_NO NUMBER(30) REFERENCES account(ACC_NO))")

    connect.execute("CREATE TABLE IF NOT EXISTS depos_with(CUST_ID NUMBER(30) REFERENCES customer(CUST_ID),"
                    "ACC_NO NUMBER(30) REFERENCES account(ACC_NO))")

    connect.execute("CREATE TABLE IF NOT EXISTS br_loan(IFSC VARCHAR(30)  REFERENCES branch(IFSC),"
                    "LOAN_NO NUMBER(10) REFERENCES loan(LOAN_NO))")

    connect.execute("CREATE TABLE IF NOT EXISTS borrower(CUST_ID NUMBER(30) REFERENCES customer(CUST_ID),"
                    "LOAN_NO NUMBER(10) REFERENCES loan(LOAN_NO))")
    connect.close()


data_creation()
print("database created")









