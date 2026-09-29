import csv
from tabulate import tabulate

fn = "students.csv"

sub = ["English", "Maths", "Physics", "Chemistry", "Computer"]

head = ["Roll No", "Name", "English", "Maths", "Physics",
        "Chemistry", "Computer", "Total", "Percentage", "Grade"]


def create_file():
    try:
        f = open(fn, "r")
        f.close()
    except:
        f = open(fn, "w", newline="")
        w = csv.writer(f)
        w.writerow(head)
        f.close()


def find_grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    elif per >= 40:
        return "E"
    else:
        return "F"


def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")

    f = open(fn, "r")
    data = csv.DictReader(f)

    for stu in data:
        if stu["Roll No"] == roll:
            print("Roll No already exists!")
            f.close()
            return

    f.close()

    marks = []

    for s in sub:
        while True:
            try:
                m = int(input("Enter " + s + " marks: "))

                if m >= 0 and m <= 100:
                    marks.append(m)
                    break
                else:
                    print("Marks should be between 0 and 100.")

            except:
                print("Please enter a valid number.")

    total = sum(marks)
    per = total / 5
    gr = find_grade(per)

    f = open(fn, "a", newline="")
    w = csv.writer(f)

    w.writerow([
        roll,
        name,
        marks[0],
        marks[1],
        marks[2],
        marks[3],
        marks[4],
        total,
        "%.2f" % per,
        gr
    ])

    f.close()

    print("Student added successfully!")


def display_students():
    st = []

    f = open(fn, "r")
    data = csv.reader(f)

    next(data)

    for row in data:
        st.append(row)

    f.close()

    if len(st) == 0:
        print("No students found.")
    else:
        print(tabulate(
            st,
            headers=head,
            tablefmt="grid",
            stralign="center"
        ))


def search_student():
    search = input("Enter Roll No or Name: ").lower()

    found = []

    f = open(fn, "r")
    data = csv.DictReader(f)

    for stu in data:
        if (search in stu["Roll No"].lower() or
                search in stu["Name"].lower()):

            found.append([
                stu["Roll No"],
                stu["Name"],
                stu["English"],
                stu["Maths"],
                stu["Physics"],
                stu["Chemistry"],
                stu["Computer"],
                stu["Total"],
                stu["Percentage"],
                stu["Grade"]
            ])

    f.close()

    if len(found) > 0:
        print(tabulate(
            found,
            headers=head,
            tablefmt="grid",
            stralign="center"
        ))
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter Roll No to delete: ")

    st = []
    found = False

    f = open(fn, "r")
    data = csv.DictReader(f)

    for stu in data:
        if stu["Roll No"] == roll:
            found = True
        else:
            st.append(stu)

    f.close()

    if found:
        f = open(fn, "w", newline="")
        w = csv.DictWriter(f, fieldnames=head)

        w.writeheader()
        w.writerows(st)

        f.close()

        print("Student deleted successfully!")
    else:
        print("Student not found.")


create_file()

while True:

    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_student()

    elif ch == "2":
        display_students()

    elif ch == "3":
        search_student()

    elif ch == "4":
        delete_student()

    elif ch == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")

