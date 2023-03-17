import os
import sys


def check_platform():
    if sys.platform == "linux":
        pass
    else:
        print("Your OS is not supported by script")
        exit()


def print_users_logs(username):
    if username != "":
        os.system(f"last -f /var/run/utmp | grep {username[0]}")
    else:
        os.system("last -f /var/run/utmp")


check_platform()

username = str(input("If you want to find specific user, please provide the username. If not leave blank: ") or "")
print("\n")

print_users_logs(username)
print("\n")
