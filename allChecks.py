#!usr/bin/env python3
import os
import shutil
import sys

def checkReboot():
    """Returns True if the computer is pending reboot."""
    return os.path.exists("/run/reboot-required")

def checkDiskFull(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def main(): 
    if checkReboot():
        print("Pending Reboot.")
        sys.exit(1)
    if checkDiskFull(disk="/", min_gb=2, min_percent=10):
        print("Disk full.")
        sys.exit(1)
    
    print("Everything ok")
    sys.exit(0)

main()