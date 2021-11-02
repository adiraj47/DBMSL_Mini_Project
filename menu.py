import main
import sqlite3 as sql
import add_data as add
import display_data as display
main.data_creation()
connect = sql.connect("Bank.sqlite")


if __name__ == '__main__':
    choice = ""
    while choice != '0':
        print("""Please choose from the below what operation you want to perform: 
        1) Add a new bank
        2) Add a new branch
        3) Add a new employee
        4) Display the list of banks
        5) Display the list of branches
        6) Display the details of the employee
        7)Update the details of the employee""")
        choice = input("Please Enter your choice: ")
        if choice == '1':
            bank_id = int(input("Please enter the bank ID: "))
            bank_name = input("Please enter the name of the bank")
            add.add_bank(bank_id, bank_name)
        elif choice == '2':
            branch_ifsc = int(input("Please enter the branch IFSC code: "))
            branch_address = input("Please enter the branch address: ")
            branch_name = input("Please enter the branch name: ")
            add.add_branch(branch_ifsc, branch_address, branch_name)
        elif choice == "3":
            employee_id = int(input("Please enter the id of the employee: "))
            employee_name = input("Please enter the name of the employee: ")
            employee_email = input("Please enter the email id of the employee: ")
            employee_address = input("Please enter the address of the employee: ")
            employee_date = input("Please enter the joining date of the employee in the format of dd/mm/yyyy")
            add.add_employee(employee_id, employee_name, employee_email, employee_address, employee_date)
        elif choice == '4':
            display.display_bank()
        elif choice == '5':
            display.display_branch()
        elif choice == '6':
            display.display_employee()
        elif choice=='7':
            updt.update_emp()
