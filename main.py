# ===================================
# Employee Data Management Sytem
# ===================================
# Developed by. Naufal Arkan Muhana
# JCDS - 34


# /************************************/

# /===== Data Model =====/
# Create your data model here

## /===== Configuration Lists =====/
# Existing Departments
DEPARTMENTS = {
    "1": {"name": "Finance", "prefix": "FIN"},
    "2": {"name": "Marketing", "prefix": "MKT"},
    "3": {"name": "IT", "prefix": "IT"},
    "4": {"name": "Human Resources", "prefix": "HRM"},
    "5": {"name": "Operations", "prefix": "OPS"}
}

# Genders
GENDERS = {
    "1": "Male",
    "2": "Female",
}

# Banks with Partnership
BANKS = {
    "1": "BCA",
    "2": "Mandiri",
    "3": "BNI",
    "4": "BRI"
}
## /===== Database =====/
data = [
    {
        "employee_id": "FIN001",
        "national_id": "3171011405990001",
        "employee_name": "Andi Pratama",
        "gender": "Male",
        "nationality": "Indonesian",
        "birth_date": "1999-05-14",
        "phone_number": "081234567890",
        "email": "andi.p@company.com",
        "department": "Finance",
        "position": "Financial Analyst",
        "employment_status": "Active",
        "hire_date": "2023-03-15",
        "bank_name": "BCA",
        "bank_account": "1234567890",
        "salary": 8500000
    },
    {
        "employee_id": "MKT002",
        "national_id": "3171022208010002",
        "employee_name": "Siti Rahma",
        "gender": "Female",
        "nationality": "Indonesian",
        "birth_date": "2001-08-22",
        "phone_number": "081345678901",
        "email": "siti.r@company.com",
        "department": "Marketing",
        "position": "Marketing Specialist",
        "employment_status": "Active",
        "hire_date": "2024-06-01",
        "bank_name": "Mandiri",
        "bank_account": "2345678901",
        "salary": 7500000
    },
    {
         "employee_id": "IT003",
        "national_id": "3171030211960003",
        "employee_name": "Budi Santoso",
        "gender": "Male",
        "nationality": "Indonesian",
        "birth_date": "1996-11-02",
        "phone_number": "081456789012",
        "email": "budi.s@company.com",
        "department": "IT",
        "position": "Software Developer",
        "employment_status": "Active",
        "hire_date": "2021-01-10",
        "bank_name": "BNI",
        "bank_account": "3456789012",
        "salary": 12000000
    },
    {
        "employee_id": "IT004",
        "national_id": "F8493012K0000000", # Format Passport/ID Asing disesuaikan
        "employee_name": "Sarah Jenkins",
        "gender": "Female",
        "nationality": "Singaporean",
        "birth_date": "1994-03-22",
        "phone_number": "081512345678",
        "email": "sarah.j@company.com",
        "department": "IT",
        "position": "UI/UX Designer",
        "employment_status": "Active",
        "hire_date": "2024-02-15",
        "bank_name": "BCA",
        "bank_account": "7890123456",
        "salary": 14500000
    },
    {
        "employee_id": "FIN005",
        "national_id": "TK12345670000000",
        "employee_name": "Kenji Sato",
        "gender": "Male",
        "nationality": "Japanese",
        "birth_date": "1989-10-12",
        "phone_number": "081698765432",
        "email": "kenji.sato@company.com",
        "department": "Finance",
        "position": "Financial Consultant",
        "employment_status": "Active",
        "hire_date": "2025-01-10",
        "bank_name": "Mandiri",
        "bank_account": "8901234567",
        "salary": 19000000
    }
] # Example data model

## /===== Helper Functions =====/

# Create ID Generator
def generate_emp_id(dept_prefix):
    next_counter = len(data) + 1
    
    # If counter reaches (999)
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

     # 3. Personal & Identity Text Data Inputs
    national_id = input('National ID / Passport Number: ').strip().upper()
    while not national_id or len(national_id) == 20 :
        phone_number = input('[X] Enter a valid numeric phone number (min 10 digits): ').strip()

    employee_name = input('Employee Name: ').strip()
    while not employee_name:
        employee_name = input('[X] Name cannot be empty. Employee Name: ').strip()

    print("\nSelect Gender:")
    for key, gender_name in GENDERS.items():
        print(f"[{key}] {gender_name}")
        
    gender_choice = input("Insert choice (number): ").strip()
    while gender_choice not in GENDERS:
        gender_choice = input("[X] Invalid choice. Select a valid number from the list: ").strip()

    selected_gender = GENDERS[gender_choice]
    
    email = input('Work Email: ').strip()
    while "@" not in email or "." not in email:
        email = input('[X] Invalid format. Enter a valid work email: ').strip()
    
    position = input('Position: ').strip()
    while not position:
        position = input('[X] Position cannot be empty. Position: ').strip()

    hire_date = input('Hire Date (YYYY-MM-DD): ').strip()
    while len(hire_date) != 10 or '-' not in hire_date:
        hire_date = input('[X] Use proper YYYY-MM-DD format (e.g. 2024-01-15): ').strip()
    
    # 4. Handle Numeric Fields safely (Years Employed removed from inputs)
    print("\nSelect Bank Name:")
    for key, b_name in BANKS.items():
        print(f"[{key}] {b_name}")
    bank_choice = input("Insert choice (number): ").strip()
    while bank_choice not in BANKS:
        bank_choice = input("[X] Invalid choice. Select a valid number from the list: ").strip()
    selected_bank = BANKS[bank_choice]

    bank_account = input('Bank Account Number: ').strip()
    while not bank_account.isdigit():
        bank_account = input('[X] Bank account must contain numeric digits only: ').strip()

    salary = get_validated_input('Salary (IDR): ', int)

  # 7. Confirmation and Interactive Sub-editing Loop
    while True:
        print("\n" + "="*55)
        print("                  PREVIEW SUMMARY")
        print("="*55)
        print(f" [1] ID Prefix / Dept : {selected_dept} ({employee_id})")
        print(f" [2] National ID      : {national_id}")
        print(f" [3] Employee Name    : {employee_name}")
        print(f" [4] Gender           : {selected_gender}")
        print(f" [5] Nationality      : {nationality}")
        print(f" [6] Birth Date       : {birth_date}")
        print(f" [7] Phone Number     : {phone_number}")
        print(f" [8] Email            : {email}")
        print(f" [9] Position         : {position}")
        print(f" [10] Hire Date       : {hire_date}")
        print(f" [11] Bank Name       : {selected_bank}")
        print(f" [12] Bank Account    : {bank_account}")
        print(f" [13] Salary (IDR)    : Rp {salary:,}")
        print("-"*55)
        print(" Fields auto-set: Status (Active)")
        print("="*55)
        
        confirmation = input("\nIs this correct? (y) to save, (e) to edit a field, (c) to cancel entirely: ").strip().lower()

        if confirmation == 'y':
            new_employee = {
                'employee_id': employee_id,
                'national_id': national_id,
                'employee_name': employee_name,
                'gender': selected_gender,
                'nationality': nationality,
                'birth_date': birth_date,
                'phone_number': phone_number,
                'email': email,
                'department': selected_dept,
                'position': position,
                'employment_status': 'Active', 
                'hire_date': hire_date,
                'bank_name': selected_bank,
                'bank_account': bank_account,
                'salary': salary
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
                national_id = input('Enter new National ID / Passport: ').strip().upper()
                while not national_id:national_id = input('[X] Cannot be empty: ').strip().upper()
            elif edit_choice == "3":
                employee_name = input('Enter new Employee Name: ').strip()
                while not employee_name:
                    employee_name = input('[X] Name cannot be empty: ').strip()
            elif edit_choice == "4":
                print("\nChange Gender:")
                for key, gender_name in GENDERS.items():
                    print(f"[{key}] {gender_name}")
                gender_choice = input("Insert choice (number): ").strip()
                while gender_choice not in GENDERS:
                    gender_choice = input("[X] Invalid choice. Select a valid number: ").strip()
                selected_gender = GENDERS[gender_choice]
            elif edit_choice == "5":
                nationality = input('Enter new Nationality: ').strip()
                while not nationality:nationality = input('[X] Cannot be empty: ').strip()
            elif edit_choice == "6":
                birth_date = input('Enter new Birth Date (YYYY-MM-DD): ').strip()
            elif edit_choice == "7":
                phone_number = input('Enter new Phone Number: ').strip()
            elif edit_choice == "8":
                email = input('Enter new Email: ').strip()
            elif edit_choice == "9":
                position = input('Enter new Position: ').strip()
            elif edit_choice == "10":
                hire_date = input('Enter new Hire Date (YYYY-MM-DD): ').strip()
            elif edit_choice == "11":
                print("\nChange Bank Name:")
                for key, b_name in BANKS.items():print(f"[{key}] {b_name}")
                bank_choice = input("Insert choice (number): ").strip()
                while bank_choice not in BANKS:
                    bank_choice = input("[X] Invalid choice: ").strip()
                    selected_bank = BANKS[bank_choice]
            elif edit_choice == "12":
                bank_account = input('Enter new Bank Account Number: ').strip()
            elif edit_choice == "13":
                salary = get_validated_input('Enter new Salary (IDR): ', int)
            else:
                print("[X] Invalid field number choice!")   
    else:
        print("[X] Invalid option. Please press 'y', 'e', or 'c'.")
    



def view_data():
    print('\n== EMPLOYEE DATA ==')
    if not data:
        print
        return
    print('='*150)
    print(f"{'Employee ID':<10} |  {'Name':<15}  |  {'Department':<15}  |  {'Position':<20}  |  {'Salary':<15}  |  {'Y/E':<5}  |  {'E/S':<5}  |  {'Age':<5}  |  {'Gender':<5}")
    print('='*170)
    for employee in data:
        print(f"{employee['employee_id']:<10} |  {employee['employee_name']:<15}  |  {employee['department']:<15}  |  {employee['position']:<20}  |  {employee['salary']:<15}  |  {employee['years_employed']:<5}  |  {employee['employment_status']:<5}  |  {employee['age']:<5}  |  {employee['gender']:<5}")
    print('-'*150)

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
            print("\nThank you for using this program, see you next time!")  
            break  
        else:
            print("[X] Input is not valid !")


if __name__ == "__main__":
    main()