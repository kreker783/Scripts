import platform
import socket


def get_hostname():
    return socket.gethostname()


def get_ip():
    return socket.gethostbyname(get_hostname())

def get_os():
    return platform.system()

def get_cpu():
    return platform.machine()

def get_python_version():
    return platform.python_version()

def get_system_info():
    return platform.uname()

def main():
    print(f'Hostname: {get_hostname()}')
    print(f'IP: {get_ip()}')
    print(f'OS: {get_os()}')
    print(f'CPU: {get_cpu()}')
    print(f'Python version: {get_python_version()}')
    print(f'System release: {get_system_info().release}')


if __name__ == "__main__":
    main()