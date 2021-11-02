import main
import sqlite3 as sql
main.data_creation()
connect = sql.connect("Bank.sqlite")

def update_emp():
    cursor=connect.cursor()
    ch=0
    id=int(input("Enter the employee id"))
    cursor.execute("SELECT * FROM employee WHERE EMP_ID = ?", (id, ))
    row = cursor.fetchone()
    if (row==0):
        print(f"There is no employee with id: {id}")
    else:
        print("Enter 1. to update the name")
        print("Enter 2. to update the email id")
        print("Enter 3. to update the address")
        print("Enter 4. to update the phone no.")
        ch=int(input())
        if(ch==1):
            print("Enter the new name")
            t=input()
            cursor.execute("UPDATE EMPLOYEE SET EMP_NAME=? WHERE EMP_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully")
        elif(ch==2):
            print("Enter the new email id")
            t=input()
            cursor.execute("UPDATE EMPLOYEE SET EMP_EMAIL_ID=? WHERE EMP_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully")
        elif(ch==3):
            print("Enter the new Address")
            t=input()
            cursor.execute("UPDATE EMPLOYEE SET EMP_ADDRESS=? WHERE EMP_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully")     
        elif(ch==4):
            print("Enter the old Phone no")
            t=input()
            cursor.execute("SELECT * FROM employee_phone WHERE EMP_ID = ? AND EMP_PHONE=?", (id,t ))
            r1=cursor.fetchone()
            if(r1==0):
                print(f"No such phone number given with the id:{id}")
            else:
                print("Enter the new Phone no")
                n=input()
                cursor.execute("UPDATE EMPLOYEE_PHONE SET EMP_PHONE=? WHERE EMP_ID=? AND EMP_PHONE=?",(n,id,t))
                cursor.connection.commit()
                print("Updation done successfully") 
def update_cust():
    cursor=connect.cursor()
    ch=0
    id=int(input("Enter the customer id"))
    cursor.execute("SELECT * FROM CUSTOMER WHERE CUST_ID = ?", (id, ))
    row = cursor.fetchone()
    if (row==0):
        print(f"There is no customer with id: {id}")
    else:
        print("Enter 1. to update the first name")
        print("Enter 2. to update the Middle name")
        print("Enter 3. to update the Last name")
        print("Enter 4. to update the street")
        print("Enter 5. to update the city")
        print("Enter 6. to update the email id")
        print("Enter 7. to update the phone no.")
        ch=int(input())
        if(ch==1):
            print("Enter the new first name")
            t=input()
            cursor.execute("UPDATE CUSTOMER SET CUST_FNAME=? WHERE CUST_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully")
        elif(ch==2):
            print("Enter the new Middle name")
            t=input()
            cursor.execute("UPDATE CUSTOMER SET CUST_MNAME=? WHERE CUST_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully")
        elif(ch==3):
            print("Enter the new last name")
            t=input()
            cursor.execute("UPDATE CUSTOMER SET CUST_LNAME=? WHERE CUST_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully")
        elif(ch==4):
            print("Enter the new Street")
            t=input()
            cursor.execute("UPDATE CUSTOMER SET CUST_STREET=? WHERE CUST_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully") 
        elif(ch==5):
            print("Enter the new city")
            t=input()
            cursor.execute("UPDATE CUSTOMER SET CUST_CITY=? WHERE CUST_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully")
        elif(ch==6):
            print("Enter the new Email id")
            t=input()
            cursor.execute("UPDATE CUSTOMER SET CUST_EMAIL_ID=? WHERE CUST_ID=?",(t,id,))
            cursor.connection.commit()
            print("Updation done successfully") 
        elif(ch==7):
            print("Enter the old Phone no")
            t=input()
            cursor.execute("SELECT * FROM CUSTOMER_phone WHERE CUST_ID = ? AND CUST_PHONE=?", (id,t ))
            r1=cursor.fetchone()
            if(r1==0):
                print(f"No such phone number given with the customer id:{id}")
            else:
                print("Enter the new Phone no")
                n=input()
                cursor.execute("UPDATE CUSTOMER_PHONE SET CUST_PHONE=? WHERE CUST_ID=? AND CUST_PHONE=?",(n,id,t))
                cursor.connection.commit()
                print("Updation done successfully") 
