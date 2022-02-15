import os
import socket
import pyfiglet

os.system('apt update && apt upgrade')
os.system('pip install pyfiglet')
os.system('clear')

banner = pyfiglet.figlet_format("DNS LOOKUP")
print("[+]================================================[+]")
print(banner, "by B33X")
print("[+]================================================[+]\n")

url = input("url (example google.com) > ")
ip = socket.gethostbyname(url)

print("IP {} = {}".format(url, ip))
