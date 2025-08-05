# main.py

from colorama import Fore, Style
import sys
from modules.ip_whois import run_ip_whois
from modules.geoip import run_geoip
from modules.dns_ping import run_dns_ping  # ✅ DNS & Ping modülü eklendi

def main_menu():
    while True:
        print(Fore.GREEN + "\n===== TraceMind Menu =====" + Style.RESET_ALL)
        print("[1] IP WHOIS")
        print("[2] GEOIP Lookup")
        print("[3] DNS & Ping")  # ✅ Menüye eklendi
        print("[0] Exit")

        choice = input(Fore.BLUE + "\nEnter your choice: " + Style.RESET_ALL)

        if choice == "1":
            run_ip_whois()
        elif choice == "2":
            run_geoip()
        elif choice == "3":
            run_dns_ping()  # ✅ Seçim kısmına eklendi
        elif choice == "0":
            print(Fore.RED + "Exiting..." + Style.RESET_ALL)
            sys.exit()
        else:
            print(Fore.RED + "[!] Invalid choice!" + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()
