import subprocess
import os

currentUser = os.environ['USER']

output_directory = f'/home/{currentUser}/Documents/vmBackup\n'


def check_VBoxManage():
    if subprocess.run(['VBoxManage', '-v'], capture_output=True, text=True).returncode != 0:
        print("VBoxManage is not installed.")
        exit()
    return None

def check_output_directory():
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    print(f"Output directory: {output_directory}")

def get_vms():
    vms = subprocess.run(['VBoxManage', 'list', 'vms'], capture_output=True, text=True)
    output = vms.stdout
    vms_list = [line.split(' ')[0].strip('"') for line in output.splitlines()]
    return vms_list

def shut_down_vm(vm_name):
    to_shut = input(f"VM {vm_name} is running. Do you want to shut it down? (y/n)  ")
    if to_shut == 'y':
        subprocess.run(['VBoxManage', 'controlvm', vm_name, 'poweroff'])
    else:
        print(f"VM {vm_name} will not be shut down.")
        print(f"Cannot export running VM.")
        exit()
    return None

def check_vm_state(vm_name):
    vm_state = subprocess.run(['VBoxManage', 'showvminfo', vm_name], capture_output=True, text=True)
    if "running" in vm_state.stdout:
        shut_down_vm(vm_name)
    return False

def export_vm(vm_name, output_directory=output_directory):
    if vm_name is None:
        print("VM name cannot be None.")
        return None
    subprocess.run(['VBoxManage', 'export', vm_name, '--output', f'{output_directory}/{vm_name}.ova'])
    print(f"VM {vm_name} exported successfully.")
    return None


def main():
    check_VBoxManage()
    check_output_directory()

    list_of_vms = get_vms()

    for vm_name in list_of_vms:
        print(f"VM to export: {vm_name}")

        check_vm_state(vm_name)
        export_vm(vm_name)

        print("----------------------------------------")


if __name__ == "__main__":
    main()