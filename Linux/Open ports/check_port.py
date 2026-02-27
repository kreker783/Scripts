import socket
import sys

try:
    hostname = sys.argv[1]      # Get the hostname from command-line argument
    port = sys.argv[2]          # Get the port from command-line argument
except:
    print("You didn't provide arguments. Script cannot be executed without it")
    exit()  # Exit the script if no arguments provided


def check_ip():         # Defining a function to check the validity of the provided IP address or hostname
    try:
        socket.inet_aton(hostname)
        return hostname
    except socket.error:
        try:
            return socket.gethostbyname(hostname) # Get the IP address from the provided hostname
        except socket.error:
            print("Not walid IP or Hostname")
            sys.exit()  # Exit the script if the provided IP address or hostname is not valid


def check_port():       # Defining a function to check the validity of the provided port number
    if port.isdigit():
        return port
    else:
        print("Port isn't valid")
        sys.exit()   # Exit the script if the provided port is not valid


new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a new socket object for TCP communication

dest = (check_ip(), int(check_port()))

check = new_socket.connect_ex(dest) # Checking if the specified port is open

if check == 0:
    print("Port is open")
else:
    print("Port is not open")

new_socket.close()  # Close the socket object
