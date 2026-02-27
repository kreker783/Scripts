import os.path


def get_path():
    # Get a files location from user and validate it
    while True:
        file1 = input("Please enter full path to the main file: ")

        if os.path.isfile(file1):
            break
        else:
            print("File does not exit in this location please try again.")

    while True:
        file2 = input("Please enter full path to the second file: ")

        if os.path.isfile(file2):
            break
        else:
            print("File does not exit in this location please try again.")

    return file1, file2


def read_file(filename):
    # Read the contents of a file and return a list of lines
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def compare_files(file1, file2):
    # Read in the contents of both files
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    # Find and delete not unique values
    with open('file1.txt', 'w') as f:
        for username in lines1:
            if username not in lines2:
                f.write(username)


if __name__ == '__main__':
    # Get path to files
    file1, file2 = get_path()

    # Compare the files and delete not unique values
    compare_files(file1, file2)