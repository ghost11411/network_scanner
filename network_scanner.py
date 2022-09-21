import subprocess as sp
from datetime import datetime
import os

win = "TTL=128"
lin = "TTL=64"

ip_address = input("IP Address: ")
splitted_ip_digits = ip_address.split('.')
dot = '.'
first_three_ip_digits = splitted_ip_digits[0] + dot + splitted_ip_digits[1] + dot + splitted_ip_digits[2] + dot
starting_number = int(input("Starting IP Number: "))
ending_number = int(input("Ending IP Number: "))
ending_number = ending_number + 1
start_time = datetime.now()

def scan(ip_address):
    res = sp.getoutput("ping " + ip_address)
    value = res.split()
    if value[12] == win:
        print(ip_address + " Windows System") 
    elif value[12] == lin:
        print(ip_address + " Linux")
    elif value[12] == "unreachable.":
        print(ip_address + " Unreacheable")
    else:
        print(ip_address + " Others")
    

def execute():
    for ip in range(starting_number, ending_number):
        ip_address = first_three_ip_digits + str(ip)
        if (scan(ip_address)):
            print(ip_address, "is live")

execute()
end_time = datetime.now()
total_time = end_time - start_time

print("Scanning completed in: ", total_time)
