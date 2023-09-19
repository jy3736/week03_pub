#! /usr/bin/python3

import subprocess
import platform
import getpass
import re

def main():
    username = getpass.getuser()
    print(f"{username}: Hello, Github World!")

    try:
        ip_result = subprocess.check_output(["ifconfig"])
        ip_result = ip_result.decode("utf-8")
        ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+)')
        ip_matches = ip_pattern.findall(ip_result)
        if len(ip_matches) > 2:
            print(f"IP: {ip_matches[1]}")
        else:
            print("IP Address not found in ifconfig output.")
    except subprocess.CalledProcessError:
        print("Error running ifconfig command.")

    os_info = platform.platform()
    print(f"Operating System: {os_info}")

if __name__ == "__main__":
    main()