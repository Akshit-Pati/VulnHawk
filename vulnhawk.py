import os

target = input("Enter target IP or domain: ")
print("[*] Scanning target with Nmap...")

os.system(f"nmap -sV -T4 {target} -oN scan_report.txt")

print("[+] Scan complete! Report saved in scan_report.txt")

