import sys

def get_container():
    if len(sys.argv) == 1:
        print("No container name provided")
        exit()
    else:
        return sys.argv[1]

def main():
    get_container()


if __name__ == "__main__":
    main()