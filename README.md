## Python CRUD Application for Employee Management

A console-based Python application for managing employee records with full Create, Read, Update, and Delete (CRUD) operations, plus a soft-delete Recycle Bin and built-in statistics reporting.

## Business Understanding

This project caters to the Human Resources domain, specifically addressing the need to manage Employee data efficiently. Employee records play a crucial role in HR operations — tracking who works where, their compensation, banking details for payroll, and their employment status over time. Keeping this data centralized, validated, and easy to search reduces manual errors and speeds up everyday HR tasks like onboarding, payroll updates, and reporting.

**Benefits:**

- Improved data accuracy through built-in input validation (dates, emails, phone numbers, unique IDs)
- Streamlined onboarding via auto-generated, department-prefixed Employee IDs
- Enhanced decision-making through an on-demand statistics dashboard (headcount, payroll, tenure)
- Safer deletions thanks to a Recycle Bin, avoiding accidental permanent data loss
- Full traceability of edits through an update history log

**Target Users:**

This application is designed for HR staff and administrators within an organization to facilitate their day-to-day tasks of registering new hires, looking up and updating employee information, processing terminations/offboarding, and generating quick workforce reports.

## Features

- **Create:**
  - Add new employee records by selecting a department (Finance, Marketing, IT, Human Resources, Operations) and entering personal, contact, employment, and banking details.
  - Employee IDs are auto-generated from the department prefix (e.g., FIN001, IT004), incrementing per department.
  - Built-in validation: non-empty fields, valid date format (YYYY-MM-DD), valid email format, digits-only phone/bank account numbers, positive numeric salary, and duplicate-checking on National ID.
  - Preview-and-confirm flow before saving — lets the user review, edit any field, or cancel before the record is written.
- **Read:**
  - View all employees in a summary table, with optional sorting by Hire Date or Salary (ascending/descending).
  - Search for a specific employee by Employee ID or by Employee Name (partial match), showing a full detailed profile.
  - Filter and list employees by department.
- **Update:**
  - Modify an existing employee's editable fields (name, gender, nationality, birth date, phone, email, position, employment status, bank name/account, salary).
  - Employee ID, National ID, Department, and Hire Date are locked and cannot be changed.
  - Every change is confirmed before being written and logged with the old and new values.
  - View a full history log of every modification made across all employees.
- **Delete:**
  - Remove a single employee record, or batch-delete multiple records at once by ID.
  - Implements soft delete: deleted records move to a Recycle Bin rather than being permanently erased.
  - Recycle Bin supports viewing trashed records and restoring them (individually or in batch) back to the active database.
- **Security:**
  - Destructive actions (delete, permanent field updates) require explicit y/n confirmation before executing.
  - Recycle Bin supports viewing trashed records and restoring them (individually or in batch) back to the active database.
  - National ID uniqueness is enforced across both active and recycled records to prevent duplicate registrations.
- **Reporting:**
  - A dedicated Statistics view reports: total active/recycled employee counts, headcount and average salary per department, headcount by gender, headcount by employment status, salary overview (total payroll, average, highest, lowest paid), and tenure highlights (longest-tenured and most recently hired employees).

## Installation

1. **Prerequisites:**
   _ Python version 3.7 or later
   _ Python 3.7 or later
   No external dependencies — the project only uses Python's standard library (datetime)

2. **Installation:**

   ```bash
   git clone [https://github.com/](https://github.com/)naufalarkan2004-spec/Employee_Data_Management_System_Program_Python.git
   cd Employee_Data_Management_System_Program_Python
   pip install -r requirements.txt
   ```

3. **Database Setup:**
   - Database Setup: Not applicable. This project stores data in-memory using Python lists/dictionaries (data, recycle_bin, updated_history_log). All records reset when the program exits — there is no persistent storage or external database connection required.

## Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Main Menu Options:**
   - **1. Add Employee Data:**
   - **2. View Employee Data:**
   - **3. Update Employee Data:**
   - **4. Delete Employee Data:**
   - **5. View Employee Statistics:**
   - **6. Exit:**

3. **CRUD Operations (example workflow):**
   - Create: Select "Add Employee Data," choose a department, and fill in the requested fields (National ID, name, gender, nationality, birth date, phone, email, position, hire date, bank name, bank account, salary). Review the summary and confirm to save.
   - Read: Select "View Employee Data" to list all employees (optionally sorted), search for one by ID or name, or filter the list by department.
   - Update: Select "Update Employee Data," pick an employee by ID, choose the field to change, enter the new value, and confirm to save. Past edits can be reviewed under "View History of Modified Profiles."
   - Delete: Select "Delete Employee Data" to remove one or several employees by ID (moved to the Recycle Bin), or open the Recycle Bin to view/restore previously deleted records.

## Data Model

This project uses an in-memory list of dictionaries (data) to represent employee records, with a mirrored structure used for recycle_bin entries. Each employee record contains the following fields:

- **Products:**
  - Field | Type | Description
  - `employee_id`, (string): Auto-generated unique ID, department-prefixed (e.g., FIN001).
  - `national_id`, (string): National ID / passport number; enforced unique across active + recycled records
  - `employee_name`, (string): Full name of the employee
  - `gender`, (string): Male or Female
  - `nationality`, (string): Employee's nationality
  - `birth_date`, (string): (YYYY-MM-DD) Date of birth
  - `phone_number`, (string): (digits) Contact phone number, minimum 10 digits
  - `email`, (string): Work email address
  - `department`, (string): One of: Finance, Marketing, IT, Human Resources, Operations
  - `position`, (string): Job title / role
  - `employment_status`, (string): Active, On Leave, Suspended, or Terminated
  - `hire_date`, (string (YYYY-MM-DD)): Date the employee was hired
  - `bank_name`, (string): One of: BCA, Mandiri, BNI, BRI
  - `bank_account`, (string (digits)): Bank account number
  - `salary`, (integer): Monthly salary in IDR
