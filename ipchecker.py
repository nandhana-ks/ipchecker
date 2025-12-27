import os
import ipaddress

ip = input("Enter IP address: ")
print("\nAnalyzing IP address...\n")

# Check IP type (Public / Private)
try:
    ip_obj = ipaddress.ip_address(ip)

    if ip_obj.is_private:
        print("[+] IP Type   : Private")
    else:
        print("[+] IP Type   : Public")

except ValueError:
    print("[-] Invalid IP address")
    exit()

# Check IP reachability (Windows)
response = os.system("ping -n 1 " + ip + " >nul 2>&1")

if response == 0:
    print("[+] IP Status : UP")
else:
    print("[-] IP Status : DOWN")
