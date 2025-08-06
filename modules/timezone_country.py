import requests
from datetime import datetime
import pytz

def get_data_from_ipapi(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[!] ipapi.co failed with status {response.status_code}")
    except Exception as e:
        print(f"[!] ipapi.co error: {e}")
    return {}

def get_data_from_ipwhois(ip):
    try:
        response = requests.get(f"https://ipwho.is/{ip}", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[!] ipwho.is failed with status {response.status_code}")
    except Exception as e:
        print(f"[!] ipwho.is error: {e}")
    return {}

def run():
    ip = input("Enter IP address or domain: ").strip()

    print("\n[🌍] Getting location & timezone data (aggressively)...\n")

    data1 = get_data_from_ipapi(ip)
    data2 = get_data_from_ipwhois(ip)

    country = data1.get("country_name") or data2.get("country")
    city = data1.get("city") or data2.get("city")
    timezone = data1.get("timezone") or data2.get("timezone")

    if not country:
        print("[!] Country not found.")
    else:
        print(f"🌐 Country: {country}")
        if city:
            print(f"🏙️ City: {city}")
        else:
            print("🏙️ City: Not found.")

    if timezone:
        print(f"🕒 Timezone: {timezone}")

        try:
            tz = pytz.timezone(timezone)
            now = datetime.now(tz)
            print(f"⏰ Local Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"[!] Error calculating local time: {e}")
    else:
        print("[!] Timezone not found.")
