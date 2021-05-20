import os
cwd = os.getcwd() 
print("Current working directory:", cwd)

filename = input("Please enter the filename: ")

if os.path.isfile("C:/Users/HP/python_classes/" + filename):
    action = input("Select an action you want to do\nActions are: read-R, delete-D, append-A, replace-Re\n")
    if action == "read" or action == "R":
        print("File Content:")
        with open(filename, "r") as read_file:
            print(read_file.read())
    elif action == "append" or action =="A":
        text = input("Please enter your note: ")
        with open(filename, "a") as append_file:
            append_file.write(text + "\n")
    elif action == "delete" or action == "D":
        os.remove("C:/Users/HP/python_classes/" + filename)
        print("{} have been deleted.".format(filename))

        with open(filename, "w") as write_file:
            write_file.write("")
    elif action == "replace" or action == "Re":
        line_num = int(
            input("Please enter the line number for the replacement: "))
        text = input("Please enter your note: ")
        with open(filename, "r") as read_file:
            lines = read_file.readlines()
        with open(filename, "w") as write_file:
            for idx, line in enumerate(lines):
                if idx == line_num - 1:
                    print("Line num {} needs to be replaced!".format(line_num))
                    write_file.write(text + "\n")
                else:
                    print("Writing \"{}\"".format(line))
                    write_file.write(line)

    else:
        print("Sorry, No Action found")
else:
    print("This file does not exist, Going to create it for you.")
    text = input("Please enter your note: ")
    with open(filename, "w") as write_file:
        write_file.write(text + "\n")