# VulnHawk

# VulnHawk 🛡️

VulnHawk is a beginner-friendly, automated vulnerability scanner built using **Python** and **Nmap**. It scans web ports (80/443) using Nmap's default vulnerability  detection scripts and highlights possible security flaws.

---

## 📦 Requirements

- Python 3.x installed  
- Nmap installed and added to system PATH  
- Works on Windows, macOS, and Linux  
- Internet connection required (to scan public domains)

## 🔧 How it Works

1. Asks user for domain or IP  
2. Runs Nmap with `--script vuln` on ports 80, 443  
3. Displays vulnerabilities results  in the  console  
4. saves full scan report to 'scan_report.txt

---

## 🚀 Usage

```bash

python vulnhawk.py

```
## When prompted
Enter target IP or domain: example.com
[*] Scanning target with Nmap...
[+] Scan complete! Report saved in scan_report.txt

---
## 📝 Output Example

## 📝 Output Example

Target: testphp.vulnweb.com  
IP: 44.228.249.3  
Open Port: 80/tcp (nginx 1.19.0)

[+] Scan complete! Report saved in scan_report.txt

---

 ⚠️ **Legal Warning**

This tool is intended for educational and ethical testing purposes only.  
Do **NOT** scan domains or IPs without proper authorization.  
Use responsibly. ⚠️

---

## ✨ Author

Created by Akshit-pati 
Cybersecurity & Ethical Hacking Enthusiast 🛡️  

---
## License
This project is licensed under the MIT License – see the **LICENSE file** for details.

----
