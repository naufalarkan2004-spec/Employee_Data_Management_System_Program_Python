# ===================================
# Employee Data Management Sytem
# ===================================
# Developed by. Naufal Arkan Muhana
# JCDS - 34


# /************************************/

# /===== Data Model =====/
# Create your data model here

## /===== Configuration Lists =====/
DEPARTMENTS = {
    "1": {"name": "Finance", "prefix": "FIN"},
    "2": {"name": "Marketing", "prefix": "MKT"},
    "3": {"name": "IT", "prefix": "IT"},
    "4": {"name": "Human Resources", "prefix": "HRM"},
    "5": {"name": "Operations", "prefix": "OPS"}
}

GENDERS = {
    "1": "Male",
    "2": "Female",
}

data = [
    {
        "employee_id": "FIN001",
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
        "employee_id": "MKT002",
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
        "employee_id": "IT003",
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
        "employee_id": "HRM004",
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
        "employee_id": "OPS005",
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

## /===== Helper Functions =====/

# Create ID Generator
def generate_emp_id(dept_prefix):
    next_counter = len(data) + 1
    
    # Jika counter melewati batas ratusan (999)
    if next_counter > 999:
        return None
        
    return f"{dept_prefix}{str(next_counter).zfill(3)}"

# Create Input Validator
def get_validated_input(prompt, val_type):
    """Ensures input data types are handled safely without crashing."""
    while True:
        try:
            val = input(prompt).strip()
            if not val:
                print("[X] Input cannot be empty!")
                continue
            return val_type(val)
        except ValueError:
            print(f"[X] Invalid data type format. Expected a {val_type.__name__}.")

# Search Employee
def search_employee_by_id(existing_id):
    """Finds and returns a single employee dict matching the id, or None."""
    for employee in data:
        if employee['employee_id'].upper() == existing_id.upper():
            return employee
    return None
# Validator
# Tidak boleh input id yang sudah exist (looping check satu satu isi list)
# Tidak boleh input department yang tidak exist

# Upcoming
# display gaji pake koma


#CRUD Program

# /===== Feature Program =====/
# Create your feature program here
def add_data():
    print("\n== ADD EMPLOYEE DATA ==")
    
    # 1. Department Selection (Determines ID Prefix)
    print("\nSelect Department:")
    for key, dept_info in DEPARTMENTS.items():
        print(f"[{key}] {dept_info['name']}")
    dept_choice = input("Insert choice (number): ").strip()
    while dept_choice not in DEPARTMENTS:
        dept_choice = input("[X] Invalid choice. Select a valid number from the list: ").strip()
    selected_dept = DEPARTMENTS[dept_choice]["name"]
    dept_prefix = DEPARTMENTS[dept_choice]["prefix"]
    # 2. ID Generation
    employee_id = generate_emp_id(dept_prefix)
    if employee_id is None:
        print("[X] Gagal menambahkan data! Limit ID tercapai.")
        return
    print(f"Generated Employee ID: {employee_id}")
      # 3. Handle Text Data
    employee_name = input('Employee Name: ').strip()
    while not employee_name:
        employee_name = input('[X] Name cannot be empty. Employee Name: ').strip()
        
    position = input('Position: ').strip()
    while not position:
        position = input('[X] Position cannot be empty. Position: ').strip()

    # 4. Handle Numeric Fields safely (Years Employed removed from inputs)
    salary = get_validated_input('Salary (IDR): ', float)
    age = get_validated_input('Age: ', int)

    # 5. Gender Selection
    print("\nSelect Gender:")
    for key, gender_name in GENDERS.items():
        print(f"[{key}] {gender_name}")
        
    gender_choice = input("Insert choice (number): ").strip()
    while gender_choice not in GENDERS:
        gender_choice = input("[X] Invalid choice. Select a valid number from the list: ").strip()

    selected_gender = GENDERS[gender_choice]

    # 6. Cofirmation and Editing Loop
    while True:
        print("\n" + "="*40)
        print("         PREVIEW SUMMARY")
        print("="*40)
        print(f"[1] ID Prefix / Dept : {selected_dept} ({employee_id})")
        print(f"[2] Employee Name    : {employee_name}")
        print(f"[3] Position         : {position}")
        print(f"[4] Salary (IDR)     : {salary:,.2f}")
        print(f"[5] Age              : {age}")
        print(f"[6] Gender           : {selected_gender}")
        print("-"*40)
        print("Fields auto-set: Status (Active), Years Employed (0.0)")
        print("="*40)
        
        confirmation = input("\nIs this correct? (y) to save, (e) to edit a field, (c) to cancel entirely: ").strip().lower()

        if confirmation == 'y':
            # Create and append payload
            new_employee = {
                'employee_id': employee_id,
                'employee_name': employee_name,
                'department': selected_dept,
                'position': position,
                'salary': salary,
                'years_employed': 0.0,            
                'employment_status': 'Active', 
                'age': age,
                'gender': selected_gender
            }
            data.append(new_employee)
            print(f"\n[V] Employee '{employee_name}' has successfully been added with ID: {employee_id}!")
            break
            
        elif confirmation == 'c':
            print("[!] Registration cancelled. Data discarded.")
            break
        elif confirmation == 'e':
            # Sub-menu to pick what field to edit
            edit_choice = input("Enter the field number you want to correct (1-6): ").strip()
            
            if edit_choice == "1":
                print("\nChange Department:")
                for key, dept_info in DEPARTMENTS.items():
                    print(f"[{key}] {dept_info['name']}")
                dept_choice = input("Insert choice (number): ").strip()
                while dept_choice not in DEPARTMENTS:
                    dept_choice = input("[X] Invalid choice. Select a valid number: ").strip()
                
                selected_dept = DEPARTMENTS[dept_choice]["name"]
                dept_prefix = DEPARTMENTS[dept_choice]["prefix"]
                employee_id = generate_emp_id(dept_prefix) # Regenerate correct prefix ID
                print(f"New ID Generated: {employee_id}")
        elif edit_choice == "2":
                employee_name = input('Enter new Employee Name: ').strip()
                while not employee_name:
                    employee_name = input('[X] Name cannot be empty: ').strip()

        elif edit_choice == "3":
                position = input('Enter new Position: ').strip()
                while not position:
                    position = input('[X] Position cannot be empty: ').strip()

        elif edit_choice == "4":
                salary = get_validated_input('Enter new Salary (IDR): ', float)

        elif edit_choice == "5":
                age = get_validated_input('Enter new Age: ', int)

        elif edit_choice == "6":
                print("\nChange Gender:")
                for key, gender_name in GENDERS.items():
                    print(f"[{key}] {gender_name}")
                gender_choice = input("Insert choice (number): ").strip()
                while gender_choice not in GENDERS:
                    gender_choice = input("[X] Invalid choice. Select a valid number: ").strip()
                selected_gender = GENDERS[gender_choice]
        else:
                print("[X] Invalid field number choice!")
                
    else:
            print("[X] Invalid option. Please press 'y', 'e', or 'c'.")
    



def view_data():
    print('\n== EMPLOYEE DATA ==')
    if not data:
        print
        return
    print('='*170)
    print(f"{'Employee ID':<15} |  {'Name':<15}  |  {'Department':<15}  |  {'Position':<25}  |  {'Salary':<15}  |  {'Years Employed':<15}  |  {'Employment Status':<20}  |  {'Age':<5}  |  {'Gender':<5}")
    print('='*170)
    for employee in data:
        print(f"{employee['employee_id']:<15} |  {employee['employee_name']:<15}  |  {employee['department']:<15}  |  {employee['position']:<25}  |  {employee['salary']:<15}  |  {employee['years_employed']:<15}  |  {employee['employment_status']:<20}  |  {employee['age']:<5}  |  {employee['gender']:<5}")
    print('-'*170)

def update_data():
    print('\n==UPDATE EMPLOYEE DATA==')
    if not data:
        print('[!] There is no data to update')
        return
        
    id_input = input('Input the employee id that wants to be updated:').strip()
    employee = search_employee_by_id(id_input)
    if not employee:
        print('[X] Employee ID is not found !')
        return
    print('\n== Existing Data =='.upper())
    print(f'Employee ID : {data['employee_id']}')
    print(f'Employee Name : {data['employee_name']}')
    print(f'Department : {data['department']}')
    print(f'Position : {data['position']}')
    print(f'Salary : {data['salary']}')
    print(f'Years Employed : {data['years_employed']}')
    print(f'Employment Status : {data['employment_status']}')
    print(f'Age : {data['age']}')
    print(f'Gender : {data['gender']}')

def delete_data():
     print("\n== DELETE EMPLOYEE DATA ==")
     if not data:
        print("[!] The data to be deleted is not found!")
        return
     id_input = input("Input the employee id that wants to be deleted:: ").strip()
     if not data:
                 print("[X] ID is not found!")
                 return
     
     print("\n=== EMPLOYEE DATA TO BE DELETED ===")
     print(f'Employee ID : {data['employee_id']}')
     print(f'Employee Name : {data['employee_name']}')
     print(f'Department : {data['department']}')
     print(f'Position : {data['position']}')
     print(f'Salary : {data['salary']}')
     print(f'Years Employed : {data['years_employed']}')
     print(f'Employment Status : {data['employment_status']}')
     print(f'Age : {data['age']}')
     print(f'Gender : {data['gender']}')

     confirmation = input("\n[!] Are you sure you want to delete this employee data? (y/n): ").strip().lower()
     if confirmation == 'y':
        data.remove(data)
        print("[V] Employee data has been successfully deleted!")
     else: 
        print("[!] Deletion of employee data is cancelled.")

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