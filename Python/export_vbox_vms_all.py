import virtualbox
from virtualbox.library import ExportOptions

VM_NAME = 'test_lab'

vbox = virtualbox.VirtualBox()
vm = vbox.find_machine(VM_NAME)

appliance = vbox.create_appliance()
desc = slredmine.export_to(appliance, VM_NAME)
p = appliance.write('ovf-2.0', [ExportOptions.create_manifest], '/home/kreker/personal/vm_backup/test5.ovf')
