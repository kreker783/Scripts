import os
import subprocess
import sys

currentUser = os.environ['USER']
import_directory = f'/home/{currentUser}/Documents/vmBackup'

def check_arguments():
    if len(sys.argv) == 1:
        print("No VM name provided. All VMs will be imported.")
        return None
    else:
        return sys.argv[1:]

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

def get_vms():
    files = os.listdir(import_directory)
    return files

def import_vm(vm_name, import_directory=import_directory):
    subprocess.run(['VBoxManage', 'import', f'{import_directory}/{vm_name}'])


def main():
    check_VBoxManage()
    check_import_directory()

    provided_vms_to_import = check_arguments()

    if provided_vms_to_import is None:
        vms_to_import = get_vms()
    else:
        vms_to_import = provided_vms_to_import

    for vm_name in vms_to_import:
        import_vm(vm_name)

    print("All VMs imported.")


if __name__ == "__main__":
    main()