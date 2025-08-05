# main.py

from colorama import Fore, Style
import sys

# Aktif modülleri içe aktar
from modules.ip_whois import run_ip_whois
from modules.geoip import run_geoip
from modules.dns_ping import run_dns_ping
from modules.username_lookup import run_username_lookup
from modules.shodan_scan import run_shodan_scan
from modules.timezone_country import run_timezone_country

def main_menu():
    while True:
        print(Fore.GREEN + "\n===== TraceMind Menu =====" + Style.RESET_ALL)
        print("[1] IP WHOIS")
        print("[2] GEOIP Lookup")
        print("[3] DNS & Ping")
        print("[5] Username Lookup")
        print("[6] Shodan Scan")
        print("[8] Timezone & Country")
        print("[0] Exit")

        choice = input(Fore.BLUE + "\nEnter your choice: " + Style.RESET_ALL)

        if choice == "1":
            run_ip_whois()
        elif choice == "2":
            run_geoip()
        elif choice == "3":
            run_dns_ping()
        elif choice == "5":
            run_username_lookup()
        elif choice == "6":
            run_shodan_scan()
        elif choice == "8":
            run_timezone_country()
        elif choice == "0":
            print(Fore.RED + "\nExiting TraceMind..." + Style.RESET_ALL)
            sys.exit()
        else:
            print(Fore.RED + "[!] Invalid choice!" + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()
