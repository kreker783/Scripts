import subprocess
import os
import argparse


output_directory = '/home/kreker/personal/vm_backup'

get_vms = subprocess.run(['VBoxManage', 'list', 'vms'], capture_output=True, text=True)
output = get_vms.stdout
vms_list = [line.split(' ')[0].strip('"') for line in output.splitlines()]

for vm_name in vms_list:
    print(f"VM to export: {vm_name}")
