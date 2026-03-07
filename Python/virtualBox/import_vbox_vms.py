import os
import subprocess


currentUser = os.environ['USER']
import_directory = f'/home/{currentUser}/Documents/vmBackup\n'

def check_VBoxManage():
    if subprocess.run(['VBoxManage', '-v'], capture_output=True, text=True).returncode != 0:
        print("VBoxManage is not installed.")
        exit()
    return None

def check_import_directory():
    if not os.path.exists(import_directory):
        print("Import directory does not exist.")
        exit()
    print(f"Import from: {import_directory}")


def main():
    check_VBoxManage()
    check_import_directory()

if __name__ == "__main__":
    main()