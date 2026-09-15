# ===================================
# Employee Data Management Sytem
# ===================================
# Developed by. Naufal Arkan Muhana
# JCDS - 34


# /************************************/

# /===== Data Model =====/
# Create your data model here

## Imports
from datetime import datetime

## /===== Configuration Lists =====/
### Existing Departments
DEPARTMENTS = {
    "1": {"name": "Finance", "prefix": "FIN"},
    "2": {"name": "Marketing", "prefix": "MKT"},
    "3": {"name": "IT", "prefix": "IT"},
    "4": {"name": "Human Resources", "prefix": "HRM"},
    "5": {"name": "Operations", "prefix": "OPS"}
}

### Genders
GENDERS = {"1": "Male","2": "Female"}

### Banks with Partnership
BANKS = {"1": "BCA", "2": "Mandiri", "3": "BNI", "4": "BRI"}

STATUSES = {"1": "Active", "2": "On Leave", "3": "Suspended", "4": "Terminated"}
## /===== Database =====/
### Dummy Data
data = [
     {
            "employee_id": "FIN001", "national_id": "3171011405990001",
            "employee_name": "Andi Pratama", "gender": "Male", "nationality": "Indonesian",
            "birth_date": "1999-05-14", "phone_number": "081234567890", "email": "andi.p@company.com",
            "department": "Finance", "position": "Financial Analyst", "employment_status": "Active",
            "hire_date": "2023-03-15", "bank_name": "BCA", "bank_account": "1234567890", "salary": 8500000,
        },
     {
            "employee_id": "MKT002", "national_id": "3171022208010002",
            "employee_name": "Siti Rahma", "gender": "Female", "nationality": "Indonesian",
            "birth_date": "2001-08-22", "phone_number": "081345678901", "email": "siti.r@company.com",
            "department": "Marketing", "position": "Marketing Specialist", "employment_status": "Active",
            "hire_date": "2024-06-01", "bank_name": "Mandiri", "bank_account": "2345678901", "salary": 7500000,
        },
   {
           "employee_id": "IT003", "national_id": "3171030211960003",
           "employee_name": "Budi Santoso", "gender": "Male", "nationality": "Indonesian",
           "birth_date": "1996-11-02", "phone_number": "081456789012", "email": "budi.s@company.com",
           "department": "IT", "position": "Software Developer", "employment_status": "Active",
           "hire_date": "2021-01-10", "bank_name": "BNI", "bank_account": "3456789012", "salary": 12000000,
       },
    {
           "employee_id": "IT004", "national_id": "F8493012K0000000",
           "employee_name": "Sarah Jenkins", "gender": "Female", "nationality": "Singaporean",
           "birth_date": "1994-03-22", "phone_number": "081512345678", "email": "sarah.j@company.com",
           "department": "IT", "position": "UI/UX Designer", "employment_status": "Active",
           "hire_date": "2024-02-15", "bank_name": "BCA", "bank_account": "7890123456", "salary": 14500000,
       },
    {
           "employee_id": "FIN005", "national_id": "TK12345670000000",
           "employee_name": "Kenji Sato", "gender": "Male", "nationality": "Japanese",
           "birth_date": "1989-10-12", "phone_number": "081698765432", "email": "kenji.sato@company.com",
           "department": "Finance", "position": "Financial Consultant", "employment_status": "Active",
           "hire_date": "2025-01-10", "bank_name": "Mandiri", "bank_account": "8901234567", "salary": 19000000,
       },
]

### Update History Log
updated_history_log = []

### Recycle Bin
recycle_bin = []


## /===== Helper Functions =====/

## Display labels for each editable field (used by preview / detail / edit screens)
FIELD_LABELS = {
    "employee_name": "Employee Name",
    "gender": "Gender",
    "nationality": "Nationality",
    "birth_date": "Birth Date",
    "phone_number": "Phone Number",
    "email": "Email",
    "position": "Position",
    "employment_status": "Employment Status",
    "bank_name": "Bank Name",
    "bank_account": "Bank Account",
    "salary": "Salary (IDR)",
    "national_id": "National ID",
    "hire_date": "Hire Date",
}

# No Empty 
def get_nonempty_input(prompt):
    """Keeps asking until the user provides a non-blank value."""
    value = input(prompt).strip()
    while not value:
        value = input("[X] Input cannot be empty! Try again: ").strip()
    return value

# Numeral Input Validator
def get_validated_number(prompt, num_type=int, min_value=None):
    """Generic numeric validator. Works for any numeric type and any minimum bound,
    so the 'must be positive'."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("[X] Input cannot be empty!")
            continue
        try:
            value = num_type(raw)
        except ValueError:
            print(f"[X] Invalid data type format. Expected a {num_type.__name__}.")
            continue
        if min_value is not None and value < min_value:
            print(f"[X] Value must be at least {min_value}.")
            continue
        return value

# Date Validator
def get_valid_date(prompt):
    while True:
        date_input = input(prompt).strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("[X] Invalid date. Use YYYY-MM-DD format.")


# Digit Validator
def get_digits_input(prompt, min_length=1, label="digits only"):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and len(value) >= min_length:
            return value
        print(f"[X] Please enter {label}.")

# Email Validator
def get_valid_email(prompt):
    while True:
        value = input(prompt).strip()
        if "@" in value and "." in value:
            return value
        print("[X] Invalid format. Enter a valid email.")

# Selection Printer
def select_from_menu(title, options):
    """Prints a numbered menu from a dict and returns (key, display_value).
    Works whether the dict values are plain strings (GENDERS/BANKS/STATUSES)
    or dicts with a 'name' field (DEPARTMENTS)."""
    print(f"\n{title}")
    for key, option in options.items():
        label = option["name"] if isinstance(option, dict) else option
        print(f"[{key}] {label}")
    choice = input("Insert choice (number): ").strip()
    while choice not in options:
        choice = input("[X] Invalid choice. Select a valid number from the list: ").strip()
    value = options[choice]
    return choice, (value["name"] if isinstance(value, dict) else value)

# Confirmation Choice
def confirm(prompt):
    """Single reusable yes/no prompt. Returns True only on 'y'."""
    return input(prompt).strip().lower() == "y"

def parse_id_list(raw_input):
    """Splits a comma/space separated string of IDs into a clean,
    deduplicated, upper-case list (order preserved). Used by batch delete
    and batch restore so both share one parsing rule."""
    raw_ids = raw_input.replace(",", " ").split()
    seen = set()
    ids = []
    for raw_id in raw_ids:
        clean_id = raw_id.strip().upper()
        if clean_id and clean_id not in seen:
            seen.add(clean_id)
            ids.append(clean_id)
    return ids

# /===== Search / Lookup =====/

# Search Employee by id
def search_employee_by_id(existing_id):
    for employee in data:
        if employee["employee_id"].upper() == existing_id.upper():
            return employee
    return None

# Search Employee by name
def search_employee_by_name(name):
    return [e for e in data if name.lower() in e["employee_name"].lower()]

# No Duplicate
def is_duplicate_value(field_key, value):
    """Checks a field's value against both active and recycled records."""
    return any(emp[field_key] == value for emp in data + recycle_bin)

# No Duplicate National ID
def collect_unique_national_id(prompt="National ID / Passport Number: "):
    value = get_nonempty_input(prompt).upper()
    while is_duplicate_value("national_id", value):
        value = get_nonempty_input(
            "[X] This National ID / Passport is already registered. Enter another: "
        ).upper()
    return value

## /===== ID Generation =====/

def generate_emp_id(dept_prefix):
    """Generates a unique employee ID based on the highest existing ID number
    across both active and recycled records."""
    highest_number = 0
    for employee in data + recycle_bin:
        employee_id = employee["employee_id"]
        if employee_id[: len(dept_prefix)] == dept_prefix:
            number_part = employee_id[len(dept_prefix):]
            if number_part.isdigit():
                highest_number = max(highest_number, int(number_part))

    next_counter = highest_number + 1
    if next_counter > 999:
        return None
    return f"{dept_prefix}{str(next_counter).zfill(3)}"

## /===== Field Collectors (shared by Add and Update) =====/
# Each collector prompts the user and returns a validated value for that field.
# Reused by add_data()'s edit-a-field submenu AND update_data() so the same
# validation logic and prompt text is written exactly once.

FIELD_COLLECTORS = {
    "employee_name": lambda: get_nonempty_input("Enter Employee Name: "),
    "gender": lambda: select_from_menu("Select Gender:", GENDERS)[1],
    "nationality": lambda: get_nonempty_input("Enter Nationality: "),
    "birth_date": lambda: get_valid_date("Birth Date (YYYY-MM-DD): "),
    "phone_number": lambda: get_digits_input(
        "Enter Phone Number: ", 10, "a valid numeric phone number (min 10 digits)"
    ),
    "email": lambda: get_valid_email("Enter Email: "),
    "position": lambda: get_nonempty_input("Enter Position: "),
    "employment_status": lambda: select_from_menu("Select Employment Status:", STATUSES)[1],
    "bank_name": lambda: select_from_menu("Select Bank Name:", BANKS)[1],
    "bank_account": lambda: get_digits_input("Enter Bank Account Number: ", 1, "digits only"),
    "salary": lambda: get_validated_number("Enter Salary (IDR): ", int, min_value=1),
    "national_id": lambda: collect_unique_national_id("Enter new National ID / Passport: "),
    "hire_date": lambda: get_valid_date("Hire Date (YYYY-MM-DD): "),
}

# Field order shown to the user for each screen (number -> field key).
ADD_FIELD_ORDER = [
    ("2", "national_id"), ("3", "employee_name"), ("4", "gender"), ("5", "nationality"),
    ("6", "birth_date"), ("7", "phone_number"), ("8", "email"), ("9", "position"),
    ("10", "hire_date"), ("11", "bank_name"), ("12", "bank_account"), ("13", "salary"),
]  # "1" (department) is handled separately below since it also drives ID generation

UPDATE_FIELD_ORDER = [
    ("1", "employee_name"), ("2", "gender"), ("3", "nationality"), ("4", "birth_date"),
    ("5", "phone_number"), ("6", "email"), ("7", "position"), ("8", "employment_status"),
    ("9", "bank_name"), ("10", "bank_account"), ("11", "salary"),
]

## /===== Display Helpers =====/

###Display lite data
def print_employee_table(target_list):
    if not target_list:
        print("[!] No employee records found.")
        return

    print("\n" + "=" * 145)
    print(f"{'ID':<8} | {'NAME':<20} | {'GENDER':<8} | {'DEPARTMENT':<15} | "
          f"{'POSITION':<22} | {'STATUS':<10} | {'HIRE DATE':<12} | {'SALARY (IDR)':<15}")
    print("=" * 145)
    for emp in target_list:
        print(f"{emp['employee_id']:<8} | {emp['employee_name']:<20} | {emp['gender']:<8} | "
              f"{emp['department']:<15} | {emp['position']:<22} | {emp['employment_status']:<10} | "
              f"{emp['hire_date']:<12} | Rp {emp['salary']:>12,}")
    print("=" * 145)

### Display employee details
def print_employee_detail(employee):
    """Prints one employee's full profile. Called once per employee so that
    multi-result name searches show every match in full."""
    print("\n" + "=" * 55)
    print(f"       DETAILED PROFILE FOR {employee['employee_id']}")
    print("=" * 55)
    print(f" Employee ID      : {employee['employee_id']}")
    print(f" National ID      : {employee['national_id']}")
    print(f" Full Name        : {employee['employee_name']}")
    print(f" Gender           : {employee['gender']}")
    print(f" Nationality      : {employee['nationality']}")
    print(f" Birth Date       : {employee['birth_date']}")
    print(f" Phone Number     : {employee['phone_number']}")
    print(f" Work Email       : {employee['email']}")
    print(f" Department       : {employee['department']}")
    print(f" Job Position     : {employee['position']}")
    print(f" Employment Status: {employee['employment_status']}")
    print(f" Hire Date        : {employee['hire_date']}")
    print(f" Bank Partner     : {employee['bank_name']}")
    print(f" Bank Account No. : {employee['bank_account']}")
    print(f" Monthly Salary   : Rp {employee['salary']:,}")
    print("=" * 55)

### Organize Header
def print_id_name_dept_list(records, id_header="AVAILABLE ID"):
    print("\n" + "-" * 65)
    print(f"{id_header:<12} | {'EMPLOYEE NAME':<25} | {'DEPARTMENT':<18}")
    print("-" * 65)
    for emp in records:
        print(f"{emp['employee_id']:<12} | {emp['employee_name']:<25} | {emp['department']:<18}")
    print("-" * 65)

### Format Salary
def format_display_value(field_key, value):
    return f"Rp {value:,}" if field_key == "salary" else str(value)

## /===== CRUD Program =====/

def add_data():
    print("\n== ADD EMPLOYEE DATA ==")
### Department selection
    dept_choice, selected_dept = select_from_menu("Select Department:", DEPARTMENTS)
    dept_prefix = DEPARTMENTS[dept_choice]["prefix"]

    employee_id = generate_emp_id(dept_prefix)
    if employee_id is None:
        print("[X] Failed to add employee! ID limit reached for this department.")
        return
    print(f"Generated Employee ID: {employee_id}")

    # Collect all remaining fields using the shared collectors
    values = {"department": selected_dept}
    for _, field_key in ADD_FIELD_ORDER:
        values[field_key] = FIELD_COLLECTORS[field_key]()

    # Preview / confirm / edit loop
    while True:
        print("\n" + "=" * 55)
        print("                  PREVIEW SUMMARY")
        print("=" * 55)
        print(f" [ 1] {'ID Prefix / Dept':<18}: {selected_dept} ({employee_id})")
        for number, field_key in ADD_FIELD_ORDER:
            display = format_display_value(field_key, values[field_key])
            print(f" [{number:>2}] {FIELD_LABELS[field_key]:<18}: {display}")
        print("-" * 55)
        print(" Fields auto-set: Status (Active)")
        print("=" * 55)

        confirmation = input(
            "\nIs this correct? (y) to save, (e) to edit a field, (c) to cancel entirely: "
        ).strip().lower()

        if confirmation == "y":
            new_employee = {
                "employee_id": employee_id,
                "department": selected_dept,
                "employment_status": "Active",
                **values,
            }
            data.append(new_employee)
            print(f"\n[V] Employee '{values['employee_name']}' has successfully been "
                  f"added with ID: {employee_id}!")
            return

        elif confirmation == "c":
            print("[!] Registration cancelled. Data discarded.")
            return

        elif confirmation == "e":
            edit_choice = input("Enter the field number you want to correct (1-13): ").strip()
            if edit_choice == "1":
                dept_choice, selected_dept = select_from_menu("Change Department:", DEPARTMENTS)
                dept_prefix = DEPARTMENTS[dept_choice]["prefix"]
                employee_id = generate_emp_id(dept_prefix)
                print(f"New ID Generated: {employee_id}")
            else:
                field_key = dict(ADD_FIELD_ORDER).get(edit_choice)
                if field_key:
                    values[field_key] = FIELD_COLLECTORS[field_key]()
                else:
                    print("[X] Invalid field number choice!")
        else:
            print("[X] Invalid option. Please press 'y', 'e', or 'c'.")



def view_data():
    while True:
        print("\n== VIEW EMPLOYEE RECORDS ==")
        print("[1] View All Employees Summary")
        print("[2] Search Individual Employee (Detailed Profile)")
        print("[3] Filter Employees by Department")
        print("[4] Back to Main Menu")
        choice = input("Insert choice (1-4): ").strip()

        if choice == "1":
            if not data:
                print("\n[!] No employee records found.")
                continue

            display_list = data.copy()
            sort_choice = input("\nDo you want to sort the data? (y) to sort, (any other key) to skip: ").strip().lower()

            if sort_choice == "y":
                print("\nSort by:\n[1] Sort by Hire Date\n[2] Sort by Salary")
                criteria = input("Insert sort criteria choice (1-2): ").strip()
                print("\nOrder:\n[1] Ascending (Oldest Date / Lowest Salary)\n[2] Descending (Newest Date / Highest Salary)")
                direction = input("Insert order choice (1-2): ").strip()
                is_descending = direction == "2"

                sort_keys = {"1": ("hire_date", "HIRE DATE"), "2": ("salary", "SALARY")}
                if criteria in sort_keys:
                    key, label = sort_keys[criteria]
                    display_list.sort(key=lambda x: x[key], reverse=is_descending)
                    print(f"\n>> SORTED BY {label} ({'DESCENDING' if is_descending else 'ASCENDING'})")
                else:
                    print("[X] Invalid sort criteria chosen. Displaying defaults instead.")
            else:
                print(f"\n>> TOTAL RECORDS: {len(data)} EMPLOYEE(S) (Default Order)")

            print_employee_table(display_list)

        elif choice == "2":
            search_choice = input("\nSearch by [1] Employee ID or [2] Employee Name: ").strip()

            if search_choice == "1":
                emp_id = input("Enter Employee ID (e.g., FIN001): ").strip().upper()
                employee = search_employee_by_id(emp_id)
                employees = [employee] if employee else []
            elif search_choice == "2":
                name = input("Enter Employee Name: ").strip()
                employees = search_employee_by_name(name)
            else:
                print("[X] Invalid choice.")
                employees = []

            if employees:
                for employee in employees:
                    print_employee_detail(employee)
            else:
                print("[X] No employee found.")

        elif choice == "3":
            dept_choice, target_dept = (None, None)
            print("\nSelect Department to Filter:")
            for key, dept_info in DEPARTMENTS.items():
                print(f"[{key}] {dept_info['name']}")
            dept_choice = input("Insert department number: ").strip()

            if dept_choice in DEPARTMENTS:
                target_dept = DEPARTMENTS[dept_choice]["name"]
                filtered_data = [emp for emp in data if emp["department"] == target_dept]
                print(f"\n>> FILTER RESULTS FOR DEPARTMENT: {target_dept.upper()} ({len(filtered_data)} found)")
                print_employee_table(filtered_data)
            else:
                print("[X] Invalid department selection.")

        elif choice == "4":
            print("[-->] Returning to main menu.")
            break
        else:
            print("[X] Invalid option. Please insert a number between 1 and 4.")

### Update
def update_data():
    while True:
        print("\n== UPDATE EMPLOYEE RECORDS ==")
        print(" [1] Modify Existing Employee Profile")
        print(" [2] View History of Modified Profiles")
        print(" [3] Back to Main Menu")

        choice = input("Insert choice (1-3): ").strip()

        if choice == "1":
            if not data:
                print("\n[!] No employee records available to update.")
                continue

            print_id_name_dept_list(data)
            emp_id = input("\nEnter Employee ID to update (e.g., FIN001): ").strip().upper()
            employee = search_employee_by_id(emp_id)

            if not employee:
                print(f"[X] Employee with ID '{emp_id}' does not exist in the database.")
                continue

            print("\n" + "=" * 55)
            print(f"       CURRENT RECORD FOR {employee['employee_id']}")
            print("=" * 55)
            for number, field_key in UPDATE_FIELD_ORDER:
                display = format_display_value(field_key, employee[field_key])
                print(f" [{number:>2}] {FIELD_LABELS[field_key]:<18}: {display}")
            print("-" * 55)
            print(" Note: ID, National ID, Dept, & Hire Date are locked keys.")
            print("=" * 55)

            edit_choice = input("\nEnter the field number you want to change (1-11) or 'c' to cancel: ").strip().lower()
            if edit_choice == "c":
                print("[!] Update operation cancelled.")
                continue

            field_key = dict(UPDATE_FIELD_ORDER).get(edit_choice)
            if not field_key:
                print("[X] Invalid choice configuration input.")
                continue

            old_value = employee[field_key]
            new_value = FIELD_COLLECTORS[field_key]()

            display_new = format_display_value(field_key, new_value)
            display_old = format_display_value(field_key, old_value)
            print(f"\n[!] Staged modification: Changing '{field_key}' from '{display_old}' to '{display_new}'")

            if confirm("Confirm modification permanent rewrite? (y) to update, (any key) to drop: "):
                updated_history_log.append({
                    "employee_id": employee["employee_id"],
                    "employee_name": employee["employee_name"],
                    "modified_field": field_key.replace("_", " ").title(),
                    "old_value": display_old,
                    "new_value": display_new,
                })
                employee[field_key] = new_value
                print("\n[V] Success! Employee record updated permanently.")
            else:
                print("[!] Process abandoned. No values written.")

        elif choice == "2":
            if not updated_history_log:
                print("\n[!] The update log registry is empty. No profile edits have been made yet.")
                continue

            print("\n" + "=" * 110)
            print(f"{'LOG ID':<8} | {'EMP ID':<8} | {'EMPLOYEE NAME':<20} | {'FIELD CHANGED':<18} | "
                  f"{'OLD VALUE':<20} | {'NEW VALUE':<20}")
            print("=" * 110)
            for idx, entry in enumerate(updated_history_log, 1):
                print(f"Log #{idx:<4} | {entry['employee_id']:<8} | {entry['employee_name']:<20} | "
                      f"{entry['modified_field']:<18} | {entry['old_value']:<20} | {entry['new_value']:<20}")
            print("=" * 110)

        elif choice == "3":
            print("[-->] Returning to main menu.")
            break
        else:
            print("[X] Invalid option choice number.")

def delete_data():
     while True:
        print("\n== DELETE EMPLOYEE RECORDS ==")
        print(" [1] Terminate & Remove Employee Record")
        print(" [2] Batch Delete Multiple Records")
        print(" [3] Open Recycle Bin (View & Restore Records)")
        print(" [4] Back to Main Menu")

        choice = input("Insert choice (1-4): ").strip()
 
        if choice == "1":
            if not data:
                print("\n[!] No active employee records available to delete.")
                continue
 
            print_id_name_dept_list(data)
            emp_id = input("\nEnter Employee ID to delete from the list above: ").strip().upper()
            employee = search_employee_by_id(emp_id)
 
            if not employee:
                print(f"[X] Employee with ID '{emp_id}' does not exist in the active database.")
                continue
 
            print("\n" + "!" * 45)
            print("        CRITICAL ACTION: CONFIRM RECORD")
            print("!" * 45)
            print(f" Target ID     : {employee['employee_id']}")
            print(f" Name          : {employee['employee_name']}")
            print(f" Department    : {employee['department']}")
            print(f" Job Position  : {employee['position']}")
            print("!" * 45)
            print(" Note: Record will be moved to the Recycle Bin.")
            print("=" * 45)
 
            if confirm(f"\nAre you sure you want to delete {employee['employee_name']}? (y/n): "):
                recycle_bin.append(employee)
                data.remove(employee)
                print(f"\n[V] Success! Record '{emp_id}' has been moved to the Recycle Bin.")
            else:
                print("[!] Deletion process aborted.")
 
        elif choice == "2":
            if not data:
                print("\n[!] No active employee records available to delete.")
                continue
 
            print_id_name_dept_list(data)
            raw_ids = input(
                "\nEnter Employee IDs to delete, separated by commas or spaces: "
            ).strip()
            requested_ids = parse_id_list(raw_ids)
 
            if not requested_ids:
                print("[X] No valid IDs entered.")
                continue
 
            matched, unmatched = [], []
            for emp_id in requested_ids:
                employee = search_employee_by_id(emp_id)
                (matched if employee else unmatched).append(employee or emp_id)
 
            if unmatched:
                print(f"[!] These IDs were not found and will be skipped: {', '.join(unmatched)}")
 
            if not matched:
                print("[X] None of the entered IDs matched an active record.")
                continue
 
            print("\n" + "!" * 45)
            print("     CRITICAL ACTION: CONFIRM BATCH DELETE")
            print("!" * 45)
            for employee in matched:
                print(f" - {employee['employee_id']} | {employee['employee_name']} | {employee['department']}")
            print("!" * 45)
            print(f" Note: {len(matched)} record(s) will be moved to the Recycle Bin.")
            print("=" * 45)
 
            if confirm(f"\nAre you sure you want to delete these {len(matched)} record(s)? (y/n): "):
                for employee in matched:
                    recycle_bin.append(employee)
                    data.remove(employee)
                print(f"\n[V] Success! {len(matched)} record(s) moved to the Recycle Bin.")
            else:
                print("[!] Batch deletion aborted. No records were removed.")
 
        elif choice == "3":
            while True:
                print("\n== RECYCLE BIN ==")
                print(" [1] View Trash List")
                print(" [2] Restore a Deleted Employee")
                print(" [3] Batch Restore Multiple Employees")
                print(" [4] Back to Delete Menu")
 
                bin_choice = input("Insert choice (1-4): ").strip()
 
                if bin_choice == "1":
                    if not recycle_bin:
                        print("\n[!] The Recycle Bin is empty.")
                        continue
                    print_id_name_dept_list(recycle_bin, id_header="TRASHED ID")
 
                elif bin_choice == "2":
                    if not recycle_bin:
                        print("\n[!] No records available to restore.")
                        continue
 
                    restore_id = input("\nEnter the Employee ID you wish to restore: ").strip().upper()
                    target_restore = next((e for e in recycle_bin if e["employee_id"] == restore_id), None)
 
                    if target_restore:
                        print(f"\nStaged Restore: Bringing back '{target_restore['employee_name']}' "
                              f"({target_restore['employee_id']})")
                        if confirm("Confirm restoration to active database? (y/n): "):
                            data.append(target_restore)
                            recycle_bin.remove(target_restore)
                            print(f"\n[V] Success! {restore_id} is now back in the active employee records.")
                        else:
                            print("[!] Restore process dropped.")
                    else:
                        print(f"[X] ID '{restore_id}' was not found inside the Recycle Bin.")
 
                elif bin_choice == "3":
                    if not recycle_bin:
                        print("\n[!] No records available to restore.")
                        continue
 
                    print_id_name_dept_list(recycle_bin, id_header="TRASHED ID")
                    raw_ids = input(
                        "\nEnter Employee IDs to restore, separated by commas or spaces: "
                    ).strip()
                    requested_ids = parse_id_list(raw_ids)
 
                    if not requested_ids:
                        print("[X] No valid IDs entered.")
                        continue
 
                    matched, unmatched = [], []
                    for emp_id in requested_ids:
                        target = next((e for e in recycle_bin if e["employee_id"] == emp_id), None)
                        (matched if target else unmatched).append(target or emp_id)
 
                    if unmatched:
                        print(f"[!] These IDs were not found in the Recycle Bin and will be skipped: "
                              f"{', '.join(unmatched)}")
 
                    if not matched:
                        print("[X] None of the entered IDs matched a recycled record.")
                        continue
 
                    print(f"\nStaged Restore: Bringing back {len(matched)} record(s):")
                    for employee in matched:
                        print(f" - {employee['employee_id']} | {employee['employee_name']}")
 
                    if confirm("\nConfirm restoration of these records to the active database? (y/n): "):
                        for employee in matched:
                            data.append(employee)
                            recycle_bin.remove(employee)
                        print(f"\n[V] Success! {len(matched)} record(s) restored to active employee records.")
                    else:
                        print("[!] Batch restore dropped. No records were restored.")
 
                elif bin_choice == "4":
                    break
                else:
                    print("[X] Invalid option selection.")
 
        elif choice == "4":
            print("[-->] Returning to main menu.")
            break
        else:
            print("[X] Invalid choice option number.")

def view_statistics():
    """Read-only reporting feature: computes and displays aggregate
    statistics over the active employee dataset — headcount and average
    salary per department, headcount by gender and employment status, a
    salary overview (total/average/highest/lowest), and tenure highlights.
    Does not modify any data."""
    print("\n== EMPLOYEE STATISTICS ==")
 
    if not data:
        print("[!] No employee records available for statistics.")
        return
 
    total_active = len(data)
    print(f"\nTotal Active Employees   : {total_active}")
    print(f"Total Recycled Employees : {len(recycle_bin)}")
 
    print("\n-- Headcount & Avg Salary by Department --")
    for dept_info in DEPARTMENTS.values():
        dept_name = dept_info["name"]
        members = [e for e in data if e["department"] == dept_name]
        avg_text = f"Rp {sum(e['salary'] for e in members) / len(members):,.0f}" if members else "N/A"
        print(f"  {dept_name:<18}: {len(members):>3} employee(s) | Avg Salary: {avg_text}")
 
    print("\n-- Headcount by Gender --")
    for gender in GENDERS.values():
        count = sum(1 for e in data if e["gender"] == gender)
        print(f"  {gender:<10}: {count:>3} ({count / total_active * 100:.1f}%)")
 
    print("\n-- Headcount by Employment Status --")
    for status in STATUSES.values():
        count = sum(1 for e in data if e["employment_status"] == status)
        if count:
            print(f"  {status:<12}: {count}")
 
    salaries = [e["salary"] for e in data]
    highest = max(data, key=lambda e: e["salary"])
    lowest = min(data, key=lambda e: e["salary"])
    print("\n-- Salary Overview --")
    print(f"  Total Monthly Payroll : Rp {sum(salaries):,}")
    print(f"  Average Salary        : Rp {sum(salaries) / total_active:,.0f}")
    print(f"  Highest Paid          : {highest['employee_name']} ({highest['employee_id']}) - Rp {highest['salary']:,}")
    print(f"  Lowest Paid           : {lowest['employee_name']} ({lowest['employee_id']}) - Rp {lowest['salary']:,}")
 
    def years_employed(emp):
        """Returns an employee's tenure in years (float) based on hire_date."""
        hire = datetime.strptime(emp["hire_date"], "%Y-%m-%d")
        return (datetime.now() - hire).days / 365.25
 
    longest = max(data, key=years_employed)
    newest = min(data, key=years_employed)
    print("\n-- Tenure Overview --")
    print(f"  Longest Tenured       : {longest['employee_name']} "
          f"({years_employed(longest):.1f} yrs, since {longest['hire_date']})")
    print(f"  Most Recently Hired   : {newest['employee_name']} "
          f"({years_employed(newest):.1f} yrs, since {newest['hire_date']})")
 
    print("\n" + "=" * 55)

## /===== Main Program =====/

### Display Main Menu
def main():
    while True:
        print("=" * 70)
        print("EMPLOYEE DATA MANAGEMENT SYSTEM".center(70))
        print("=" * 70)
        print("1. Add Employee Data")
        print("2. View Employee Data")
        print("3. Update Employee Data")
        print("4. Delete Employee Data")
        print("5. View Employee Statistics")
        print("6. Exit")
        print("=" * 70)
 
        choice = input("Insert your choice (1-6): ").strip()
        if choice == "1":
            add_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            view_statistics()
        elif choice == "6":
            print("\nThank you for using this program, see you next time!")
            break
        else:
            print("[X] Input is not valid !")

if __name__ == "__main__":
    main()
