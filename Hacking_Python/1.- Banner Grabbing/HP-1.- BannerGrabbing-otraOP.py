#IMPORTS
import socket
import os
import sys
from termcolor import colored, cprint

#FUNCTIONS
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket()
        sock.connect((ip, port))
        banner = sock.recv(1024)
        banner = banner.decode()
        return banner
    except:
        return


def checkVulns(banner, filename):
    f = open(filename, "r")
    for line in f.readlines():
        if line in banner:
            print(colored('[+] El server es vulnerable: ' + banner, 'red'))

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] File Doesnt Exist!')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] access Denied!')
            exit(0)
    else:
        print('[-] Usage: ' + str(sys.argv[0]) + 'vuln.txt')
        exit(0)
    portlist = [21, 22, 25, 80, 110, 443, 445]
    for x in range(8, 15):
        ip = '192.168.1.' + str(x)
        for port in portlist:
            banner = retBanner(ip, port)
            if banner:
                cprint('[+] ' + ip + '/' + str(port) + ': ' + banner.strip("\n"), 'cyan', 'on_grey')
                checkVulns(banner, filename)

#MAIN
if __name__ == '__main__':
    main()