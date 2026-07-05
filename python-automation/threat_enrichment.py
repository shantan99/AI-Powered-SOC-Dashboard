# threat_enrichment.py
# Checks if attacker IP is a known malicious IP using VirusTotal API
# In this demo, we use a local known-bad-IPs list to simulate the API response

import json

# Known malicious IPs (in a real deployment, this is replaced by VirusTotal API call)
known_malicious_ips = {
    "192.168.1.50": {"country": "Unknown", "detections": 45, "label": "SSH Scanner"},
    "172.16.0.5":   {"country": "RU",      "detections": 87, "label": "Port Scanner / Botnet"},
    "45.33.32.156": {"country": "US",      "detections": 12, "label": "Known Attack Infrastructure"},
    "10.0.0.99":    {"country": "Unknown", "detections": 3,  "label": "Suspicious — low detections"},
}

def check_ip_reputation(ip_address):
    print(f"\nChecking IP: {ip_address}")
    print("Querying VirusTotal... (simulated)")

    if ip_address in known_malicious_ips:
        info = known_malicious_ips[ip_address]
        print(f"  Status     : MALICIOUS")
        print(f"  Country    : {info['country']}")
        print(f"  Detections : {info['detections']} security vendors flagged this IP")
        print(f"  Label      : {info['label']}")
        return True
    else:
        print(f"  Status     : CLEAN — not found in threat database")
        print(f"  Recommendation: Monitor but do not block yet")
        return False


# IPs from the Splunk brute force alert
ips_to_check = ["192.168.1.50", "172.16.0.5", "10.0.0.55", "45.33.32.156"]

print("=" * 60)
print("THREAT ENRICHMENT REPORT — IP Reputation Check")
print("=" * 60)

malicious_ips = []

for ip in ips_to_check:
    is_malicious = check_ip_reputation(ip)
    if is_malicious:
        malicious_ips.append(ip)

print("\n" + "=" * 60)
print(f"SUMMARY: {len(malicious_ips)} malicious IPs found")
print("Confirmed malicious IPs:", malicious_ips)
print("Passing to incident_response.py for auto-block...")
