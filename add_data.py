import main
import sqlite3 as sql
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)


def add_bank(id: int, name: str) -> None:
    """

    :param id:
    :param name:
    :return:
    """
    currsor = connect.cursor()
    currsor.execute("SELECT * FROM bank WHERE bank_id = ?", (id, ))
    row = currsor.fetchone()
    if row:
        print(f"Bank already present {row}")
    else:
        currsor.execute("INSERT INTO bank VALUES (?, ?)", (id, name))
        currsor.connection.commit()
        print(f"The New bank has been created {name}")


def add_branch(ifsc: int, address: str, name: str) -> None:
    """

    :param ifsc:
    :param address:
    :param name:
    :return:
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

    :param id:
    :param name:
    :param email:
    :param address:
    :param joining_date:
    :return:
    """
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM employee WHERE EMP_ID = ?", (id, ))
    row = cursor.fetchone()
    if row:
        print(f"The employee already works here the details our: {row}")
    else:
        cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", (id, name, email, address, joining_date))
        cursor.connection.commit()
        print(f"""The new employee has been added with the following details: 
        Id: {id}
        Name: {name}
        Email-id: {id}
        Address: {address}
        Joining_date: {joining_date}""")


def add_employee_phone(id: int, phone_no: int) -> None:
    """

    :param id:
    :param phone_no:
    :return:
    """
    cursor = connect.cursor()
    cursor.execute("INSERT INTO employee_phone VALUES (?, ?)", (id, phone_no))
    cursor.connection.commit()
    print(f"Phone number added for {id}")


def add_customer(cust_id: int, fname: str, mname: str, lname: str, cust_street: str, cust_city: str, cust_email: str):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM customer WHERE CUST_ID = ?", (cust_id, ))
    row = cursor.fetchone()

    if row:
        print(f"already a customer present for {cust_id} please select other id")
    else:
        cursor.execute("INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?)",(cust_id, fname, mname, lname, cust_street, cust_city))
        cursor.connection.commit()
        print(f"Welcome {fname} to our bank")


def add_customer_phone(cust_id: int, cust_phone: int):
    """

    :param cust_id:
    :param cust_phone:
    :return:
    """
    cursor = connect.cursor()
    cursor.execute("INSERT INTO customer_phone VALUES (?, ?)", (cust_id, cust_phone))
