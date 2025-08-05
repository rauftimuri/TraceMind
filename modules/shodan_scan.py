# modules/shodan_scan.py

import webbrowser
from colorama import Fore, Style

def run_shodan_scan():
    target = input(Fore.YELLOW + "\n[?] Enter IP or domain for Shodan scan: " + Style.RESET_ALL)
    
    if target:
        print(Fore.CYAN + "[*] Opening Shodan scan in browser..." + Style.RESET_ALL)
        url = f"https://www.shodan.io/host/{target}"
        webbrowser.open(url)
    else:
        print(Fore.RED + "[!] Invalid input. No target provided." + Style.RESET_ALL)
