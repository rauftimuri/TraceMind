# modules/timezone_country.py

import requests
from colorama import Fore, Style

def run_timezone_country():
    ip = input(Fore.YELLOW + "\n[?] Enter IP address: " + Style.RESET_ALL)
    
    try:
        print(Fore.CYAN + "[*] Fetching location and timezone info..." + Style.RESET_ALL)
        response = requests.get(f"http://ip-api.com/json/{ip}")

        data = response.json()

        if data["status"] == "success":
            print(Fore.GREEN + f"\n--- Location Info ---")
            print(f"IP Address : {data['query']}")
            print(f"Country    : {data['country']}")
            print(f"Region     : {data['regionName']}")
            print(f"City       : {data['city']}")
            print(f"Timezone   : {data['timezone']}")
            print(f"ISP        : {data['isp']}")
            print("------------------------" + Style.RESET_ALL)
        else:
            print(Fore.RED + "[!] Failed to fetch data." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}" + Style.RESET_ALL)
