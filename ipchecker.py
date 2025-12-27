import os
import ipaddress

ip = input("Enter IP address: ")

# Ping the IP once (Windows)
response = os.system("ping -n 1 " + ip)  # Use "-c 1" on Linux/macOS

# Check if IP is up or down
if response == 0:
    print(ip + " is UP")
else:
    print(ip + " is DOWN")

# Check if IP is public or private
try:
    ip_obj = ipaddress.ip_address(ip)
    if ip_obj.is_private:
        print(ip + " is a PRIVATE IP")
    else:
        print(ip + " is a PUBLIC IP")
except ValueError:
    print("Invalid IP address")
