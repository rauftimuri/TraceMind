# modules/geoip.py

import requests
from colorama import Fore, Style

def run_geoip():
    ip = input(Fore.YELLOW + "\n[?] Enter IP address for GEOIP lookup: " + Style.RESET_ALL)

    try:
        print(Fore.CYAN + "[*] Querying ip-api.com..." + Style.RESET_ALL)
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data["status"] == "success":
            print(Fore.GREEN + "\n--- GEOIP Information ---")
            print("IP:", data["query"])
            print("Country:", data["country"])
            print("Region:", data["regionName"])
            print("City:", data["city"])
            print("ZIP:", data["zip"])
            print("Latitude:", data["lat"])
            print("Longitude:", data["lon"])
            print("ISP:", data["isp"])
            print("--------------------------" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"[!] Lookup failed: {data['message']}" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + "[!] Error occurred: " + str(e) + Style.RESET_ALL)
