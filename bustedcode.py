#!/usr/bin/env python3

import time
import sys
import netifaces


def delay_print(s):
    # there's nothing wrong with this function, it's just some cool code that
    # will print out strings one character at a time! :)
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

delay_print("Good morning, Mr. Stark. Here are your network interfaces:\n")
print(netifaces.interfaces())

for i  in netifaces.interfaces():
     with open("challenge.log", 'a') as bar:                 # opens writeable file for logging
        try:
           print('Logging addresses for interface',i)     # prints name of interface being logged
           print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'], file=bar) # Prints the MAC address to file
           print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'], file=bar) # Prints the IP address to file
        except:
           print('Could not collect adapter information') # Print an error message
