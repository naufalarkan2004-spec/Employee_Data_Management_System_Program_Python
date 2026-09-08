# ===================================
# [Your Program Title]
# ===================================
# Developed by. Bayu Prasetya
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
data = [] # Example data model


# /===== Feature Program =====/
# Create your feature program here
def read():
    """Function for read the data
    """
    return

def create():
    """Function for create the data
    """
    return

def update():
    """Function for update the data
    """
    return

def delete():
    """Function for delete the data
    """
    return

# /===== Main Program =====/
# Create your main program here
def main():
    while True:
        print("="*70)
        print("EMPLOYEE DATA MANAGEMENT SYSTEM")
        print("="*70)
        print("1. Add Employee Data")
        print("2. View Employee Data")
        print("3. Update Employee Data")
        print("4. Delete Employee Data")
        print("5. Exit")
        print("="*70)

        input_user = input("Insert your choice: ").strip()
        if input_user == "1":
            add_data()
        elif input_user == "2":
            view_data()
        elif input_user == "3":
            update_data()
        elif input_user == "4":
            delete_data()
        elif input_user == "5":
            print("\n Thank you for using this program, see you next time!")  
            break  
        else:
            print("[X] Input is not valid !")


if __name__ == "__main__":
    main()