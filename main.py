import os

# Modülleri içe aktar
import modules.ip_whois as ip_whois
import modules.geoip as geoip
import modules.dns_ping as dns_ping
import modules.deep_lookup as deep_lookup
import modules.timezone_country as timezone_country

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("\033[91m")
    print("████████╗██████╗  █████╗  ██████╗███████╗███╗   ███╗██╗███╗   ██╗██████╗ ")
    print("╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║██║████╗  ██║██╔══██╗")
    print("   ██║   ██████╔╝███████║██║     █████╗  ██╔████╔██║██║██╔██╗ ██║██║  ██║")
    print("   ██║   ██╔═══╝ ██╔══██║██║     ██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██║  ██║")
    print("   ██║   ██║     ██║  ██║╚██████╗███████╗██║ ╚═╝ ██║██║██║ ╚████║██████╔╝")
    print("   ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ")
    print("\033[0m")

    print("\033[92mCreated by \033[91mRauf TIMURI\033[0m\n")
    print("\033[91m33\033[0m\n")

def show_menu():
    print("[1] IP WHOIS")
    print("[2] GEOIP Lookup")
    print("[3] DNS & Ping")
    print("[4] Deep OSINT Lookup")
    print("[5] Timezone & Country Lookup")
    print("[0] Exit")

def main():
    while True:
        clear()
        banner()
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            ip_whois.run()
        elif choice == "2":
            geoip.run()
        elif choice == "3":
            dns_ping.run()
        elif choice == "4":
            deep_lookup.run()
        elif choice == "5":
            timezone_country.run()
        elif choice == "0":
            print("Exiting TraceMind...")
            break
        else:
            print("[!] Invalid choice.")

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
