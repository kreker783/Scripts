import socket
import sys

hostname = sys.argv[1]
port = sys.argv[2]

def check_ip():
    try:
        socket.inet_aton(hostname)
        return hostname
    except socket.error:
        try:
            return socket.gethostbyname(hostname)
        except socket.error:
            print("Not walid IP or Hostname")
            sys.exit()


def check_port():
    if port.isdigit():
        return port
    else:
        print("Port isn't valid")
        sys.exit()

new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket object socket.socket(family, type)

dest = (check_ip(), int(check_port()))

check = new_socket.connect_ex(dest)

if check == 0:
    print("Port is open")
else:
    print("Port is not open")

new_socket.close()
