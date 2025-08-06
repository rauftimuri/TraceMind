import requests

def display_section(title, data, keys):
    print(f"\n\033[96m[+] {title}\033[0m")
    for key in keys:
        value = data.get(key)
        if value and value != "Not found":
            print(f"  \033[92m{key.replace('_', ' ').title()}:\033[0m {value}")

def run():
    print("\n\033[94m[🌍] GEOIP Lookup\033[0m")
    ip = input("Enter IP address to locate: ").strip()

    services = {
        "ip-api.com": f"http://ip-api.com/json/{ip}",
        "ipinfo.io": f"https://ipinfo.io/{ip}/json",
        "ipwho.is": f"https://ipwho.is/{ip}",
        "ipapi.co": f"https://ipapi.co/{ip}/json/",
        "geolocation-db": f"https://geolocation-db.com/json/{ip}&position=true"
    }

    for name, url in services.items():
        print(f"\n\033[95m[+] Trying {name}...\033[0m")
        try:
            r = requests.get(url, timeout=8)
            if r.status_code == 200:
                data = r.json()

                if name == "ip-api.com" and data.get("status") == "success":
                    display_section(name, data, [
                        "country", "regionName", "city", "zip",
                        "lat", "lon", "timezone", "isp", "org", "as"
                    ])
                elif name == "ipinfo.io":
                    display_section(name, data, [
                        "ip", "city", "region", "country", "loc", "org", "postal", "timezone"
                    ])
                elif name == "ipwho.is" and data.get("success"):
                    display_section(name, data, [
                        "ip", "type", "continent", "country", "region", "city",
                        "latitude", "longitude", "postal", "capital", "calling_code"
                    ])
                    display_section("ISP Info", data.get("connection", {}), [
                        "asn", "org", "isp", "domain"
                    ])
                    display_section("Timezone", data.get("timezone", {}), [
                        "id", "abbr", "utc", "current_time"
                    ])
                elif name == "ipapi.co" and "error" not in data:
                    display_section(name, data, [
                        "ip", "city", "region", "country_name", "latitude", "longitude", "timezone", "org"
                    ])
                elif name == "geolocation-db":
                    display_section(name, data, [
                        "country_name", "state", "city", "postal", "latitude", "longitude", "IPv4"
                    ])
                else:
                    print("\033[91m[!] No valid data received.\033[0m")
            else:
                print(f"\033[91m[!] {name} returned status code {r.status_code}\033[0m")
        except Exception as e:
            print(f"\033[91m[!] Failed to contact {name}: {e}\033[0m")

    input("\n\033[94mPress Enter to return to menu...\033[0m")
