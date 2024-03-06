#!usr/bin/env python3
import os

def checkRebood():
    """Returns True if the computer is pending reboot."""
    return os.path.exist("/run/reboot-required")

def main():
    pass

main()