
🧠 TraceMind – Terminal-Based OSINT & Recon Tool

TraceMind is a powerful, terminal-based reconnaissance and OSINT (Open Source Intelligence) tool designed for cybersecurity researchers and ethical hackers.

It integrates several aggressive scanning modules to support fast and informative analysis across IPs, domains, and open sources.

⸻

🔍 Features
	•	[1] IP WHOIS – Retrieves domain/IP registration information.
	•	[2] GEOIP Lookup – Determines geolocation via multiple APIs.
	•	[3] DNS & Ping – Performs DNS enumeration and fast ICMP scanning.
	•	[4] Deep OSINT Lookup – Searches across the internet (Google, GitHub, Reddit, Pastebin, etc.) for leaked or suspicious data.
	•	[5] Timezone & Country – Detects timezone and country for a given IP.

⸻

⚠️ Module 4 Warning – Deep OSINT Lookup

Module 4 performs broad, multi-platform querying using aggressive headers and deep search logic.
It can uncover potentially sensitive data and access public traces across indexed platforms.
🛑 Use it carefully and ethically, and only on targets you’re authorized to analyze.

⸻

💻 Installation

git clone https://github.com/rauftimuri/TraceMind.git
cd TraceMind
pip install -r requirements.txt
python3 main.py

Works on Kali Linux, Parrot OS, and other Python3-enabled distros.

⸻

📁 Modules
	•	ip_whois.py
	•	geoip.py
	•	dns_ping.py
	•	deep_lookup.py
	•	timezone_country.py

⸻

✅ Usage

Perfect for:
	•	CTF & red team recon
	•	Threat intelligence training
	•	OSINT research & early incident response
	•	Learning ethical hacking fundamentals

⸻

Created by Rauf TIMURI

⸻
