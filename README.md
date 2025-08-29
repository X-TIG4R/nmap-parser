#  Nmap Parser

A polished, educational-grade CLI tool to parse raw Nmap scan outputs and list connected devices with IP, MAC, and manufacturer details in a clean, readable format.  
Perfect for network admins, pen-testers, or anyone needing quick visual insight from Nmap results.

---

##  Legal & Ethical Use Disclaimer

THIS TOOL IS PROVIDED FOR EDUCATIONAL, AUTHORIZED, AND ETHICAL PURPOSES ONLY.

-  **AUTHORIZED USE ONLY:** Use on systems you own or have explicit written permission to test.
-  **EDUCATIONAL PURPOSES:** Great for learning, audits, or understanding network environments.
-  **NO MALICIOUS USE:** Misuse—such as unauthorized scanning or data collection—is strictly prohibited.
-  Users are solely responsible for compliance with local laws and ethical guidelines.

---

##  Features

-  **Robust Parsing:** Extracts IP, MAC, and vendor/manufacturer info from raw Nmap output.
-  **Interactive Interface:** Clear ASCII banner, colored terminal output, and prompt-based input.
-  **Neat Visualization:** Tabulated display using `tabulate` for clean, readable output.
-  **Cross‑Platform ANSI Support:** Ensured via `colorama`, even on Windows.
-  **Modular Setup:** Can be run directly or installed as a console command.

---

##  Sample Output

/created by x.tig4r


🔍 Welcome to the Nmap Device Parser!
This tool helps you extract IP, MAC, and Manufacturer info from raw Nmap output.
[Press Enter to continue...]

Paste your Nmap output (end with an empty line):

Nmap scan report for 192.168.1.10
MAC Address: AA:BB:CC:DD:EE:FF (Cisco Systems)
Nmap scan report for 192.168.1.12
MAC Address: 11:22:33:44:55:66 (Unknown)
📋 Connected Devices:

IP Address	MAC Address	       Manufacturer
192.168.1.10	AA:BB:CC:DD:EE:FF	Cisco Systems
192.168.1.12	11:22:33:44:55:66	Unknown


---

##  Installation

### Prerequisites

- Python 3.6 or higher installed.
- `pip` package manager functioning.

### Steps

```bash
git clone https://github.com/yourusername/nmap-device-parser.git
cd nmap-device-parser
pip install -r requirements.txt

### How It Works

Banner & Prompt: Displays an ASCII banner and waits for your input.

Paste Nmap Output: Simply paste your Nmap scan results into the terminal; end with an empty line.

Parse & Display: Extracts key details (IP, MAC, vendor) and presents them in a formatted table.

### License

This project is for educational and authorized use only.
Any misuse, unauthorized distribution, or malicious intent is strongly prohibited.
Users must abide by all applicable laws and ethical standards.

---

### What’s in this README

- **Legal/Ethics**: A clear disclaimer for responsible usage.
- **Overview + Features**: Highlights how the tool works and what it offers.
- **Installation & Usage**: Step-by-step guidance.
- **Optional CLI Setup**: Instructions to install as a command.
- **Sample Output**: A visual preview.
- **Enhancements & Contributions**: Encourages future improvements.
- **Author & License**: Proper attribution and usage limitations.

Let me know if you'd like help preparing a `LICENSE.md`, adding badges, or even converting this into a template for your repository!
::contentReference[oaicite:0]{index=0}

