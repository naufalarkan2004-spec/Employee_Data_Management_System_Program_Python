# ===================================
# [Your Program Title]
# ===================================
# Developed by. Bayu Prasetya
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
data = [
    {
        "employee_id": "EMP001",
        "employee_name": "Andi Pratama",
        "department": "Finance",
        "position": "Financial Analyst",
        "salary": 8500000,
        "years_employed": 3,
        "employment_status": "Active",
        "age": 27,
        "gender": "Male"
    },
    {
        "employee_id": "EMP002",
        "employee_name": "Siti Rahma",
        "department": "Marketing",
        "position": "Marketing Specialist",
        "salary": 7500000,
        "years_employed": 2,
        "employment_status": "Active",
        "age": 25,
        "gender": "Female"
    },
    {
        "employee_id": "EMP003",
        "employee_name": "Budi Santoso",
        "department": "IT",
        "position": "Software Developer",
        "salary": 12000000,
        "years_employed": 5,
        "employment_status": "Active",
        "age": 30,
        "gender": "Male"
    },
    {
        "employee_id": "EMP004",
        "employee_name": "Nadia Putri",
        "department": "Human Resources",
        "position": "HR Officer",
        "salary": 8000000,
        "years_employed": 4,
        "employment_status": "Active",
        "age": 28,
        "gender": "Female"
    },
    {
        "employee_id": "EMP005",
        "employee_name": "Rizky Maulana",
        "department": "Operations",
        "position": "Operations Supervisor",
        "salary": 10000000,
        "years_employed": 7,
        "employment_status": "On Leave",
        "age": 34,
        "gender": "Male"
    }
] # Example data model


# /===== Feature Program =====/
# Create your feature program here
def add_data():
    print('\n== ADD EMPLOYEE DATA ==')
    employee_id = int(input('Employee ID: '))
    employee_name = input('Employee Name: ')
    department = input('Department: ')
    position = input('Position: ')
    salary = float(input('Salary: '))
    years_employed = float(input('Years Employed: '))
    employment_status = input('Employment Status')
    age = int(input('Age: '))
    gender = input('Gender: ')

    if not employee_id or not employee_name or not department or not position or not salary or not years_employed or not employment_status or not age or not gender:
         print('[X] Input tidak boleh kosong!')
         return


def read():
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
        banner = "EMPLOYEE DATA MANAGEMENT SYSTEM"
        print(banner.center(70))
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