# modules/username_lookup.py

import requests
from colorama import Fore, Style

def run_username_lookup():
    username = input(Fore.YELLOW + "\n[?] Enter a username to search: " + Style.RESET_ALL)

    platforms = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }

    print(Fore.CYAN + "\n[*] Checking username across platforms..." + Style.RESET_ALL)

    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Found on {platform}: {url}" + Style.RESET_ALL)
            elif response.status_code == 404:
                print(Fore.RED + f"[-] Not found on {platform}" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + f"[!] Unknown response from {platform}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"[!] Error checking {platform}: {e}" + Style.RESET_ALL)
