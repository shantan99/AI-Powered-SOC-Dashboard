# MITRE ATT&CK Mapping

This document maps each detection rule in this project to its corresponding MITRE ATT&CK Tactic and Technique.

MITRE ATT&CK is a globally recognized framework that categorizes the tactics and techniques used by real-world attackers. By mapping our detections here, we ensure that our SOC lab catches the same attack patterns that enterprise security teams defend against.

---

## Detection-to-MITRE Mapping Table

| Detection File | Attack Name | Tactic | Technique ID | Technique Name |
|---|---|---|---|---|
| brute-force.spl | SSH Brute Force | Credential Access | T1110 | Brute Force |
| privilege-escalation.spl | Sudo Abuse | Privilege Escalation | T1548 | Abuse Elevation Control Mechanism |
| port-scanning.spl | Nmap Scan | Discovery | T1046 | Network Service Discovery |
| lateral-movement.spl | Internal SSH | Lateral Movement | T1021 | Remote Services |
| data-exfiltration.spl | Large Outbound Transfer | Exfiltration | T1048 | Exfiltration Over Alternative Protocol |

---

## Tactic Explained

MITRE ATT&CK organizes attacker behavior into **14 Tactics** — each represents a phase in an attack. Below are the tactics covered in this project:

### 1. Credential Access (brute-force.spl)
The attacker tries to steal or guess passwords. In our case, repeated SSH login failures from one IP indicate a brute force attempt. If successful, the attacker gains a valid username + password.

### 2. Privilege Escalation (privilege-escalation.spl)
After logging in as a normal user, the attacker tries to gain admin (root) access using `sudo`. This gives them full control over the system.

### 3. Discovery (port-scanning.spl)
Before attacking, hackers scan the network to see what services and ports are open. Nmap is the most common tool used for this. Our rule catches rapid port connection attempts.

### 4. Lateral Movement (lateral-movement.spl)
Once inside one machine, the attacker tries to log into other machines on the same network using stolen credentials. Our rule detects internal logins at unusual hours.

### 5. Exfiltration (data-exfiltration.spl)
The final goal of many attacks is to steal data. We detect this by monitoring for unusually large outbound data transfers from the Azure VM.

---

## Attack Kill Chain (in order)

```
Reconnaissance (port scan)
       ↓
Initial Access (brute force SSH)
       ↓
Privilege Escalation (sudo abuse)
       ↓
Lateral Movement (internal SSH)
       ↓
Exfiltration (data theft)
```

This is the same sequence a real attacker would follow. Our detection rules catch each stage independently.
