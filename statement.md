# Student Management System

## Problem Statement

Managing student academic records manually can be time-consuming and may lead to errors in storing, calculating, searching, and deleting student information. There is a need for a simple computerized system that can maintain student records and perform basic academic calculations efficiently.

The **Student Management System** is a Python-based application that stores student details and marks in a CSV file. It automatically calculates the total marks, percentage, and grade of each student. The system also provides options to display, search, and delete student records.

## Scope of the Project

The project focuses on managing basic student academic information through a simple menu-driven Python application.

The system can:

- Store student roll number and name.
- Accept marks for English, Maths, Physics, Chemistry, and Computer.
- Validate marks so that they remain between 0 and 100.
- Calculate the total marks obtained by a student.
- Calculate the student's percentage.
- Assign a grade based on the percentage.
- Store records permanently in a CSV file.
- Display all student records in a formatted table.
- Search for students using their roll number or name.
- Delete a student record using the roll number.
- Prevent duplicate roll numbers from being added.

The project is designed for basic student record management and does not include advanced features such as user authentication, database servers, online access, or multiple user accounts.

## Target Users

The main target users of this project are:

- **Teachers** – to maintain and manage students' academic records.
- **School or college staff** – to store and retrieve student marks and results.
- **Students** – to view their academic information when permitted.
- **Beginners learning Python** – to understand file handling, CSV operations, functions, loops, conditional statements, and basic data management.

## High-Level Features

### 1. Add Student
Allows the user to enter a student's roll number, name, and marks in five subjects. The system calculates the total, percentage, and grade automatically.

### 2. Display Students
Displays all stored student records in a structured table using the `tabulate` library.

### 3. Search Student
Allows the user to search for a student using either the roll number or name.

### 4. Delete Student
Allows the user to delete a student record by entering the student's roll number.

### 5. Automatic Result Calculation
The system automatically calculates:

- Total marks
- Percentage
- Grade

Grades are assigned according to the following scale:

| Percentage | Grade |
|------------|-------|
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| 40–49      | E     |
| Below 40   | F     |

### 6. CSV File Storage
Student records are stored in `students.csv`, allowing the information to remain available after the program is closed.

### 7. Input Validation
The system checks that entered marks are valid numbers between 0 and 100 and prevents duplicate roll numbers.