import os
import sys
import socket

def get_hostname():
    return socket.gethostname()

def get_IP():
    return socket.gethostbyname(get_hostname)


def main():
    print(f'Hostname: {get_hostname}')
    print(f'IP: {get_IP}')

if __name__ == "__main__":
    main()

