import socket
import subprocess
import sys

from datetime import datetime

# subprocess.call('clear' shell=True)

remoteserver = input("Enter a remote host to scan:")
remoteserverIP = socket.gethostbye(remoteserver)nam
print("_" *60)
print("please wait,scanning ,remote host",remoteserverIP)
print("_" *60)

t1 = datetime.now()
try:
    for port in range(1,5000):
        sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result =sock.connect_ex((remoteserverIP,port))
        if result ==0:
            print("port {}:     open".format(port))
            sock.close()
except keyboardinterrupt:
      print("you passed ctrl+c")
except socket.gaierror:
    print("hostname could not be resloved.exitting")
    sys.exit()
except socket.error:
    print("couldnt connect to be server")
    sys.exit()


