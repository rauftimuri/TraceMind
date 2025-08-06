import whois

def run():
    print("\n\033[94m[🌐] IP WHOIS Lookup\033[0m")
    domain = input("Enter a domain (e.g., google.com): ")

    try:
        w = whois.whois(domain)
        print("\n\033[93m========== WHOIS INFO ==========\033[0m\n")

        def print_if_exists(label, data):
            if data:
                # Listeyse virgülle birleştir
                if isinstance(data, list):
                    data = ', '.join(str(d) for d in data)
                elif isinstance(data, set):
                    data = ', '.join(data)
                print(f"\033[92m{label}:\033[0m {data}")

        print_if_exists("Domain Name", w.domain_name)
        print_if_exists("Registrar", w.registrar)
        print_if_exists("WHOIS Server", w.whois_server)
        print_if_exists("Updated Date", w.updated_date)
        print_if_exists("Created Date", w.creation_date)
        print_if_exists("Expiration Date", w.expiration_date)
        print_if_exists("Name Servers", w.name_servers)
        print_if_exists("Status", w.status)
        print_if_exists("Emails", w.emails)
        print_if_exists("DNSSEC", w.dnssec)
        print_if_exists("Organization", w.org)
        print_if_exists("Country", w.country)

    except Exception as e:
        print(f"\n\033[91m[!] Error: {e}\033[0m")

    input("\n\033[94mPress Enter to return to menu...\033[0m")
