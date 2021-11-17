import main
import sqlite3 as sql
import streamlit as st
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)

def delete(table_name, col_name, search_value):
    cursor = connect.cursor()
    query = f"SELECT {col_name} FROM {table_name} WHERE {col_name} = ?"
    cursor.execute(query, (search_value, ))
    row = cursor.fetchone()
    if row:
        query = f"DELETE FROM {table_name} WHERE {col_name} = ?"
        cursor.execute(query, (row[0], ))
        cursor.connection.commit()
        st.write("Entry deleted")
    else:
        st.write("Entry is not present")

def table_details(table_name):
    cursor = connect.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    field_name = (i[0] for i in cursor.description)
    return field_name



