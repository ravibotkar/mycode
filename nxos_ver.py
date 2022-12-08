#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   A simple script that demonstrates using Netmiko against a Cisco NX-OS device."""

# standard library
import os

# python3 -m pip install --user netmiko
from netmiko import ConnectHandler

# call our router
def main():
    """run time code"""
    
#    open_connection = ConnectHandler(device_type='cisco_nxos', ip='sandbox-nxos-1.cisco.com', username='admin', password="Admin_1234!")

    open_connection = ConnectHandler(device_type='arista_eos', ip='sw-1', username='admin', password="alta3")

    commands = ["show ver", "show vlan", "show ip int brie"]
    
    for command in commands:
        print(open_connection.send_command(command))

   # my_command = open_connection.send_command("show ver")

   # print(my_command)

## Call main()
if __name__ == "__main__":
    main()

