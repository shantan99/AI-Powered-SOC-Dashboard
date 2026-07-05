# incident_response.py
# Automatically blocks confirmed malicious IPs on Azure Firewall
# In production: uses Azure SDK (azure-mgmt-network) to add NSG deny rules
# In this demo: simulates the block action with console output

import datetime

# Malicious IPs confirmed by threat_enrichment.py
malicious_ips = ["192.168.1.50", "172.16.0.5", "45.33.32.156"]

# Azure config (replace with your actual values when deploying)
AZURE_RESOURCE_GROUP = "soc-lab-rg"
AZURE_NSG_NAME       = "soc-lab-nsg"
AZURE_SUBSCRIPTION   = "your-subscription-id"

def block_ip_on_azure(ip_address, rule_number):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{timestamp}] Connecting to Azure NSG: {AZURE_NSG_NAME}")
    print(f"  Adding DENY rule for IP: {ip_address}")
    print(f"  Rule priority  : {rule_number}")
    print(f"  Direction      : Inbound")
    print(f"  Action         : Deny")
    print(f"  Protocol       : Any")
    print(f"  Status         : BLOCKED SUCCESSFULLY")

    # Log the action
    log_entry = {
        "timestamp":   timestamp,
        "ip_blocked":  ip_address,
        "rule_number": rule_number,
        "resource":    AZURE_NSG_NAME,
        "action":      "Deny Inbound",
        "triggered_by": "incident_response.py (automated)"
    }
    return log_entry


print("=" * 60)
print("AUTOMATED INCIDENT RESPONSE — Azure Firewall Block")
print("=" * 60)
print(f"Target: {len(malicious_ips)} malicious IPs to block")

incident_log = []
rule_start = 100

for i, ip in enumerate(malicious_ips):
    log = block_ip_on_azure(ip, rule_start + i)
    incident_log.append(log)

print("\n" + "=" * 60)
print("INCIDENT RESPONSE COMPLETE")
print(f"Total IPs blocked : {len(incident_log)}")
print("All actions logged for SOC audit trail")
print("\nIncident log summary:")
for entry in incident_log:
    print(f"  {entry['timestamp']} | {entry['ip_blocked']} | {entry['action']}")
