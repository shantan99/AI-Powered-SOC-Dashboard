# alert_triage.py
# Automatically classifies Splunk alerts by severity level
# SOC Analyst task: Level 1 triage — no manual reading needed

alerts = [
    {"type": "SSH Brute Force",      "failed_logins": 45, "src_ip": "192.168.1.50"},
    {"type": "SSH Brute Force",      "failed_logins": 8,  "src_ip": "10.0.0.22"},
    {"type": "Privilege Escalation", "sudo_count": 3,     "src_ip": "192.168.1.75"},
    {"type": "Port Scanning",        "ports_scanned": 120, "src_ip": "172.16.0.5"},
    {"type": "Lateral Movement",     "login_hour": 2,     "src_ip": "10.0.0.10"},
    {"type": "Data Exfiltration",    "mb_sent": 1500,     "src_ip": "192.168.2.1"},
]

def classify_severity(alert):
    attack = alert["type"]

    if attack == "SSH Brute Force":
        count = alert.get("failed_logins", 0)
        if count > 20:
            return "CRITICAL"
        elif count > 10:
            return "HIGH"
        else:
            return "MEDIUM"

    elif attack == "Privilege Escalation":
        return "HIGH"

    elif attack == "Port Scanning":
        ports = alert.get("ports_scanned", 0)
        if ports > 100:
            return "CRITICAL"
        elif ports > 50:
            return "HIGH"
        else:
            return "MEDIUM"

    elif attack == "Lateral Movement":
        hour = alert.get("login_hour", 12)
        if hour < 5 or hour > 23:
            return "HIGH"
        else:
            return "MEDIUM"

    elif attack == "Data Exfiltration":
        mb = alert.get("mb_sent", 0)
        if mb > 2000:
            return "CRITICAL"
        elif mb > 500:
            return "HIGH"
        else:
            return "MEDIUM"

    return "LOW"


print("=" * 60)
print("SOC ALERT TRIAGE REPORT")
print("=" * 60)

for alert in alerts:
    severity = classify_severity(alert)
    print(f"\nAttack Type : {alert['type']}")
    print(f"Source IP   : {alert['src_ip']}")
    print(f"Severity    : {severity}")
    print(f"Action      : {'Block IP immediately' if severity == 'CRITICAL' else 'Investigate and monitor'}")
    print("-" * 40)

print("\nTriage complete. Pass CRITICAL alerts to incident_response.py")
