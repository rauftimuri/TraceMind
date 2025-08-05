# modules/ip_whois.py

import whois
from colorama import Fore, Style

def run_ip_whois():
    ip = input(Fore.YELLOW + "\n[?] Enter an IP address to look up: " + Style.RESET_ALL)
    try:
        print(Fore.CYAN + "[*] Performing WHOIS lookup..." + Style.RESET_ALL)
        result = whois.whois(ip)

        print(Fore.GREEN + "\n--- WHOIS Information ---")
        print("Domain:", result.domain)
        print("Registrar:", result.registrar)
        print("Creation Date:", result.creation_date)
        print("Expiration Date:", result.expiration_date)
        print("Name Servers:", result.name_servers)
        print("Emails:", result.emails)
        print("--------------------------" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + "[!] Error occurred: " + str(e) + Style.RESET_ALL)
