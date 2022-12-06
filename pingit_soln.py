#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   CHALLENGE 01 - Redesign script so IP addresses are accepted via arguments"""

# standard library
import argparse
import os

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

def main():
    #switchlist = ["172.0.1.2", "sw-1", "sw-2", "8.8.8.8"]   # CUSTOMIZE THIS LIST WITH IPs to PING

    switchlist = args.ip

    ## Use a loop to check each device for ICMP responses
    print("\n***** STARTING ICMP CHECKING *****")
    for x in switchlist:
        if ping_router(x):
            print(f"IP address {x} is responding to ICMP")
        else:
            print(f"IP address {x} is not responding to ICMP")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple ICMP checker')
    # Required positional argument
    # parser.add_argument('ip', type=str, help='A required IP address to ping')

    # allows a user to pass a list via:
    # python3 <name of app> -ip 8.8.8.8 192.168.70.1 host.example.com
    parser.add_argument('-i', '--ip', nargs='+', help='space delimited hosts to ping', required=True, type=str)
    args = parser.parse_args()
    main()

