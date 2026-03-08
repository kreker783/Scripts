import sys
import subprocess


def check_arguments():
    if len(sys.argv) == 1:
        print("No VM name provided. All VMs will be removed.")
        return None

    return sys.argv[1:]

def check_VBoxManage():
    if subprocess.run(['VBoxManage', '-v'], capture_output=True, text=True).returncode != 0:
        print("VBoxManage is not installed.")
        exit()
    return None

def get_vms():
    vms = subprocess.run(['VBoxManage', 'list', 'vms'], capture_output=True, text=True)
    output = vms.stdout
    vms_list = [line.split(' ')[0].strip('"') for line in output.splitlines()]
    return vms_list


def check_vm_exists(vm_name):
    info = subprocess.run(['VBoxManage', 'showvminfo', vm_name], capture_output=True, text=True)
    if info.returncode == 0:
        return True
    return False

def remove_vm(vms_to_remove):
    if vms_to_remove is None:
        vms_to_remove = get_vms()
    for vm_name in vms_to_remove:
        if check_vm_exists(vm_name):
            subprocess.run(['VBoxManage', 'unregistervm', vm_name, '--delete-all'])
            print(f"VM {vm_name} removed.")
        else:
            print(f"VM {vm_name} does not exist.")


def main():
    check_VBoxManage()
    vms_to_remove = check_arguments()
    remove_vm(vms_to_remove)


if __name__ == "__main__":
    main()