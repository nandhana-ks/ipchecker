import os

# Take IP input
ip = input("Enter IP address: ")

print("\nPinging the IP address...\n")

# Ping the IP once (Windows uses -n)
response = os.system("ping -n 1 " + ip)

# Check the result
if response == 0:
    print(ip + " is UP")
else:
    print(ip + " is DOWN")
