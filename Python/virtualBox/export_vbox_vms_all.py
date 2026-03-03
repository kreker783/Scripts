import subprocess
import os

currentUser = os.environ['USER']

output_directory = f'/home/{currentUser}/Documents/vmBackup\n'

def check_output_directory():
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    print(f"Output directory: {output_directory}")

def get_vms():
    vms = subprocess.run(['VBoxManage', 'list', 'vms'], capture_output=True, text=True)
    output = vms.stdout
    vms_list = [line.split(' ')[0].strip('"') for line in output.splitlines()]
    return vms_list

def check_vm_state(vm_name):
    vm_state = subprocess.run(['VBoxManage', 'showvminfo', vm_name], capture_output=True, text=True)
    print(vm_state.stdout)
    if "running" in vm_state.stdout:
        print(f"VM {vm_name} is running. Please shut it down before exporting.")
        return False
    return True

def main():
    check_output_directory()

    list_of_vms = get_vms()
    for vm_name in list_of_vms:
        print(f"VM to export: {vm_name}")
        check_vm_state(vm_name)


if __name__ == "__main__":
    main()