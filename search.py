import sqlite3 as sql
import streamlit as st
import main
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)


def search(table_name, col_name, value):
    """
    This is the genric code for searching thorough various tables.

    :param table_name: Table name which is associated in the database
    :param col_name: The name of the column present in the table
    :param value: The value according to which it is needed to be searched
    :return: The number of rows present according to the search
    """
    cursor = connect.cursor()
    query = f"SELECT * FROM {table_name} WHERE {col_name} = ?"
    cursor.execute(query, (value, ))
    row = cursor.fetchall()
    return row



if __name__ == "__main__":
    result = search("bank", "bank_id", 1)
    print(result)


