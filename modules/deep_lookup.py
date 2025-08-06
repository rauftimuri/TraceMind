import requests
import urllib.parse

def search_engines(query):
    encoded = urllib.parse.quote_plus(query)

    targets = {
        # Arama motorları
        "Google": f"https://www.google.com/search?q={encoded}",
        "Bing": f"https://www.bing.com/search?q={encoded}",
        "DuckDuckGo": f"https://duckduckgo.com/?q={encoded}",
        "Yahoo": f"https://search.yahoo.com/search?p={encoded}",

        # Paste ve forumlar
        "Pastebin": f"https://www.google.com/search?q=site:pastebin.com+{encoded}",
        "Reddit": f"https://www.reddit.com/search/?q={encoded}",
        "4chan": f"https://www.google.com/search?q=site:4chan.org+{encoded}",

        # Kod platformları
        "GitHub": f"https://github.com/search?q={encoded}",
        "GitLab": f"https://gitlab.com/search?search={encoded}",

        # Sosyal medya (kullanıcı adı içeriği ile arama)
        "Twitter": f"https://twitter.com/search?q={encoded}",
        "Instagram": f"https://www.instagram.com/{query.replace(' ', '')}/",
        "Facebook": f"https://www.facebook.com/search/top?q={encoded}",
        "TikTok": f"https://www.tiktok.com/@{query.replace(' ', '')}",
        "LinkedIn": f"https://www.linkedin.com/search/results/all/?keywords={encoded}",
        "Tumblr": f"https://www.tumblr.com/search/{encoded}"
    }

    return targets

def categorize_result(url, query):
    q = query.lower()
    if all(word in url.lower() for word in q.split()):
        return "HIGH"
    elif any(word in url.lower() for word in q.split()):
        return "LOW"
    else:
        return None

def run():
    query = input("Enter a name or keyword (e.g., 'first name last name '): ").strip()

    print("\n[🔎] Running Deep OSINT Search...\n")

    links = search_engines(query)

    high_suspicion = []
    low_suspicion = []

    for name, url in links.items():
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; aggressive-bot/1.0)"
            }
            r = requests.get(url, headers=headers, timeout=8, allow_redirects=True)

            if r.status_code == 200:
                category = categorize_result(r.url, query)
                if category == "HIGH":
                    high_suspicion.append((name, url))
                elif category == "LOW":
                    low_suspicion.append((name, url))
                print(f"[+] {name}: ✅")
            elif r.status_code == 404:
                print(f"[-] {name}: Not found")
            else:
                print(f"[!] {name}: Status {r.status_code}")
        except Exception as e:
            print(f"[!] {name} FAILED: {e}")

    print("\n\n========== RESULTS ==========\n")

    print("🔥 HIGH SUSPICION")
    if not high_suspicion:
        print(" - No high suspicion results.")
    for name, url in high_suspicion:
        print(f" - [{name}] {url}")

    print("\n🟡 LOW SUSPICION")
    if not low_suspicion:
        print(" - No low suspicion results.")
    for name, url in low_suspicion:
        print(f" - [{name}] {url}")
