import os

# student_grade = {}

# def add_student(name, grade):
#     student_grade[name] = grade
#     print(f"Added {name} with a {grade}")

# def update_student(name, grade):
#     if name in student_grade:
#         student_grade[name] = grade
#         print(f"{name} with marks are updated {grade}")
#     else:
#         print(f"{name} not found in data")

# def delete_student(name):
#     if name in student_grade:
#         del student_grade[name]
#         print(f"{name} has been successfully deleteed")
#     else:
#         print(f"{name} is not found in data")

# def display_all_studedents():
#     if student_grade:
#         for name, grade in student_grade.items():
#             print(f"{name} : {grade}")
#     else:
#         print("no student found in data")



# def main():
#     while True:
#         print("\nStudent grades managment system")
#         print("1. Add Student")
#         print("2. Update Student")
#         print("3. Delete Student")
#         print("4. View Student")
#         print("5. Exit")

#         user = int(input("Enter your choice = "))
#         if user == 1:
#             name = input("Enter student name = ")
#             grade = int(input("Enter stdent grade = "))
#             add_student(name, grade)
#         elif user == 2:
#             name = input("Enter student name = ")
#             grade = int(input("Enter stdent grade = "))
#             update_student(name, grade)
#         elif user == 3:
#             name = input("Enter student name = ")
#             delete_student(name)
#         elif user == 4:
#             display_all_studedents()
#         elif user == 5:
#             print("closing the program.....")
#             break
#         else:
#             print("invalid choice, 'something wrong' ")

# main()


def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"file name {filename} : Created Successfully.")
    except FileExistsError:
        print(f"file name {filename} already exists in system")
    except Exception as E:
        print("an error occured !")

def view_all_file():
    files = os.listdir()
    if not files:
        print("No file found in system")
    else:
        print("Files in directory")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file name {filename} has been deleted successfully")
    except FileNotFoundError:
        print("File not found in system")
    except Exception as E:
        print("an error occured")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"{filename} file content is => {content}")
    except FileNotFoundError:
        print(f"{filename} not found in system")
    except Exception as E:
        print("an error occured")

def Edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("enter data to add in file = ")
            f.write(content)
            print(f"content added to {filename} successfully")
    except FileNotFoundError:
        print(f"{filename} doesn't exists in system")
    except Exception as E:
        print("an error occured")

def main():
    while True:
        print("FILE MANAGEMTNT APP OR SYSTEM")
        print("1. Create file")
        print("2. View all file")
        print("3. Delete file")
        print("4. Read file")
        print("5. Edit file")
        print("6. Exit")

        user = int(input("Enter your choice = "))
        if user == 1:
            name = input("Enter file name to create = ")
            create_file(name)
        elif user == 2:
            view_all_file()  
        elif user == 3:
            name = input("Enter file name to delete = ")
            delete_file(name)
        elif user == 4:
            name = input("Enter file name to read = ")
            read_file(name)
        elif user == 5:
            name = input("Enter file name to edit = ")
            Edit_file(name)
        elif user == 6:
            print("program closing...")
            break
        else:
            print("invald choice (something went wrong)")
        
    
main()