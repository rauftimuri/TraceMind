import socket
import subprocess
import platform
import dns.resolver

def print_section(title):
    print(f"\n\033[96m[+] {title}\033[0m")

def resolve_record(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type, lifetime=5)
        return [str(rdata) for rdata in answers]
    except Exception as e:
        return [f"Error: {e}"]

def ping_host(host):
    system = platform.system()
    if system == "Windows":
        command = ["ping", "-n", "3", host]
    else:
        command = ["ping", "-c", "3", host]

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True, timeout=8)
        return output
    except subprocess.CalledProcessError as e:
        return e.output
    except Exception as e:
        return f"Ping failed: {e}"

def run():
    print("\n\033[94m[🌐] DNS & Ping Scanner\033[0m")
    domain = input("Enter domain to analyze (e.g., google.com): ").strip()

    print_section("A Record (IPv4)")
    for result in resolve_record(domain, "A"):
        print("  \033[92m- " + result + "\033[0m")

    print_section("AAAA Record (IPv6)")
    for result in resolve_record(domain, "AAAA"):
        print("  \033[92m- " + result + "\033[0m")

    print_section("CNAME Record")
    for result in resolve_record(domain, "CNAME"):
        print("  \033[92m- " + result + "\033[0m")

    print_section("MX Record (Mail Servers)")
    for result in resolve_record(domain, "MX"):
        print("  \033[92m- " + result + "\033[0m")

    print_section("NS Record (Name Servers)")
    for result in resolve_record(domain, "NS"):
        print("  \033[92m- " + result + "\033[0m")

    print_section("TXT Record")
    for result in resolve_record(domain, "TXT"):
        print("  \033[92m- " + result + "\033[0m")

    print_section("Ping Results")
    ping_output = ping_host(domain)
    print("\033[90m" + ping_output + "\033[0m")

    input("\n\033[94mPress Enter to return to menu...\033[0m")
