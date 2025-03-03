import os

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
