import main
import sqlite3 as sql
main.data_creation()
connect = sql.connect("Bank.sqlite", check_same_thread=False)

def delete(table_name, col_name, value):
value=search_bank()
if(t==value):
    delete t
else:
     print ("Value not found")
