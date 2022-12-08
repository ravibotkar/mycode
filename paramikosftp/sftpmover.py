#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username="bender", password="alta3")

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

def movethemfiles(con):
    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            con.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

     ## close the connections
    con.close() # close the connection
    # ^ this line needed moved one whitespace to the left :)
    # I moved this line over to be part of this function, otherwise it closed the connection way too early
    t.close()

def main():
    movethemfiles(sftp)

main()

