import os

def menu():
    print("\n\nMenu")
    print("1. Create file")
    print("2. Delete file")
    print("3. Read file")
    print("0. Exit")

def list_files(directory):
    files = os.listdir(directory)
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    return files

def get_directory_path():
    return 'C:/Users/User/Documents/python/learning'

operation_on = True
while operation_on:
    menu()
    choice = int(input("Choose an option: "))
    if choice == 1:
        name = input("Enter name of your file: ")
        filepath = os.path.join(get_directory_path(), name)
        ch2 = input("Do you want to add some data into your file? 'Y' or 'N': ").upper()
        if ch2 == 'Y':
            data = input("Enter your data or text that you want to add: ")
            with open(filepath, 'w') as f:
                f.write(data)
            print("Your file has been created and data added.")
        else:
            open(filepath, 'a').close()
            print("Your file was created.")

    elif choice == 2:
        directory = get_directory_path()
        print("Select file to delete: ")
        files = list_files(directory)
        file_index = int(input()) - 1
        if 0 <= file_index < len(files):
            file_del = files[file_index]
            os.remove(os.path.join(directory, file_del))
            print("File deleted.")
        else:
            print("Invalid selection.")

    elif choice == 3:
        directory = get_directory_path()
        print("Select file to read: ")
        files = list_files(directory)
        file_index = int(input()) - 1
        if 0 <= file_index < len(files):
            file_read = files[file_index]
            with open(os.path.join(directory, file_read), 'r') as f:
                print(f.read())
        else:
            print("Invalid selection.")

    elif choice == 0:
        operation_on = False

