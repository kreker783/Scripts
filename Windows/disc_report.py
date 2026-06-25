import sys
from ctypes import HRESULT

try:
    import psutil
except ImportError:
    sys.exit("ERROR: missing requirements\n"
             "Install: pip install -r requirements.txt\n")

def disc_info():
    result = []
    for part in psutil.disk_partitions():
        usage = psutil.disk_usage(part.mountpoint)

        result.append(
            {
                "drive": part.device,
                "total": f"{round(usage.total / (1024 ** 3), 2)}GB",
                "used": f"{round(usage.used / (1024 ** 3), 2)}GB",
                "free": f"{round(usage.free / (1024 ** 3), 2)}GB",
                "used-percent": f"{usage.percent}%",
            }
        )

    return result

def print_disc_info(report):
    print("-"*92)

    for disc in report:
        for metric, result in disc.items():
            print(f"{metric}: {result}")
        print("-"*92)

if __name__ == "__main__":
    report = disc_info()
    print_disc_info(report)

