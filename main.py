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

# Additional Features

# ID Generator
def generate_emp_id():
    next_counter = len(data) + 1
    
    # Jika counter melewati batas ratusan (999)
    if next_counter > 999:
        return None
        
    return f"EMP{str(next_counter).zfill(3)}"

# Validator
# Tidak boleh input id yang sudah exist (looping check satu satu isi list)
# Tidak boleh input department yang tidak exist

# Upcoming
# display gaji pake koma
# 

# Search Employee
def search_employee_by_id(existing_id):
    for employee in data:
        if employee['employee_id'] == existing_id:
            return data
    return None

#CRUD Program

# /===== Feature Program =====/
# Create your feature program here
def add_data():
    employee_id = generate_emp_id()
    if employee_id is None:
        print("[X] Gagal menambahkan data! Limit ID tercapai (Maksimal EMP999).")
        return
    print(f"Generated Employee ID: {employee_id}")
    employee_name = input('Employee Name: ')
    department = input('Department: ')
    position = input('Position: ')
    salary = float(input('Salary: '))
    years_employed = float(input('Years Employed: '))
    age = int(input('Age: '))
    gender = input('Gender: ')

# Gunakan fungsi all() atau bikin fungsi cek empty field
    if not employee_id or not employee_name or not department or not position or not salary or not years_employed or not age or not gender:
         print('[X] Input tidak boleh kosong!')
         return
# Kasih opsi department
    new_employee ={
       'employee_id': employee_id,
        'employee_name': employee_name,
        'department': department,
        'position': position,
        'salary': salary,
        'years_employed': years_employed,
        'employment_status': 'Active',  # Automatically default new hires to Active
        'age': age,
        'gender': gender
    }
    confirmation = input(f" Are you sure you want to add the data of '{employee_name}'? (y/n): ").strip().lower()
    if confirmation == 'y':
        data.append(new_employee) # tambah opsi jadi simpan atau tidak
        print(f"\n[V] Employee '{employee_name}' has successfully been added with the ID: {employee_id}!")


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
     if not id_input.isdigit():
            print("[X] ID harus berupa angka!")
            return
     employee = search_employee_by_id(id_input)
     if not data:
            print("[X] ID Buku tidak ditemukan!")
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
        data.remove(employee)
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