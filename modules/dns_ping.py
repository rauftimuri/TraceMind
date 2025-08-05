# modules/dns_ping.py

import socket
import subprocess
from colorama import Fore, Style

def run_dns_ping():
    domain = input(Fore.YELLOW + "\n[?] Enter domain or IP: " + Style.RESET_ALL)

    try:
        # DNS çözümleme
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"[*] Resolved IP: {ip}" + Style.RESET_ALL)

        # Ping at
        print(Fore.CYAN + f"[*] Pinging {domain}...\n" + Style.RESET_ALL)
        output = subprocess.getoutput(f"ping -c 4 {domain}")
        print(Fore.WHITE + output + Style.RESET_ALL)

    except socket.gaierror:
        print(Fore.RED + "[!] Invalid domain or IP!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}" + Style.RESET_ALL)
