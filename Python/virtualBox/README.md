# VirtualBox Scripts

Default backup/import directory: `/home/<user>/Documents/vmBackup`

- `export_vbox_vms_all.py` — export all VirtualBox VMs to the default directory  
  Usage: `python export_vbox_vms_all.py`

- `import_vbox_vms.py` — import VirtualBox VMs from the default directory 
   If no arguments are given, all VMs are removed
   Usage: `python import_vbox_vms.py`
   Usage: `python import_vbox_vms.py full/path/to/vm1.ova full/path/to/vm2.ova`

- `remove_vbox_vms.py` — remove VirtualBox VMs  
  If no arguments are given, all VMs are removed.  
  If VM names are passed as arguments, only those VMs are removed.  
  Usage: `python remove_vbox_vms.py`  
  Usage: `python remove_vbox_vms.py vm1 vm2`