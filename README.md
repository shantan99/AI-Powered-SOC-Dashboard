# AI-Powered SOC Dashboard — FUTURE_CS_04

## Project Overview

This project simulates a real-world Security Operations Center (SOC) environment using **Splunk on Microsoft Azure**. It automatically detects five types of cyberattacks, maps each to the **MITRE ATT&CK framework**, and uses **Python automation scripts** to triage alerts, enrich threat intelligence, and trigger incident response — without manual analyst intervention.

This is an upgrade from traditional local-VM SOC labs. Everything runs on **Azure Cloud**, making it closer to how enterprise SOC teams actually operate.

---

## Why I Built This

Most entry-level SOC projects run on local virtual machines and only detect one or two attack types manually. I wanted to build something that:
- Runs on real cloud infrastructure (Azure)
- Detects multiple attack patterns simultaneously
- Automates the alert-to-response pipeline using Python
- Maps detections to MITRE ATT&CK so they mean something in a real SOC context

---

## Architecture

```
[Azure VM — Linux]
       |
  Logs generated (auth.log, syslog, network logs)
       |
  [Splunk Universal Forwarder]
       |
  [Splunk Enterprise — Indexer & Search Head]
       |
  Detection Rules (SPL Queries) fire on suspicious patterns
       |
  [Python Automation Layer]
       |
  ┌────────────────────────────────────┐
  │  alert_triage.py     → classify severity (CRITICAL/HIGH/MEDIUM/LOW)
  │  threat_enrichment.py → check IP against VirusTotal API
  │  incident_response.py → auto-block malicious IP on Azure Firewall
  └────────────────────────────────────┘
       |
  [Splunk Dashboard — Real-time SOC view]
```

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Microsoft Azure | Cloud infrastructure — VM hosting, firewall, networking |
| Splunk Enterprise | SIEM — log collection, indexing, search, alerting |
| Splunk Universal Forwarder | Ships logs from Azure VM to Splunk indexer |
| Python 3 | Automation — alert triage, threat enrichment, response |
| VirusTotal API | IP reputation check for threat enrichment |
| MITRE ATT&CK | Framework for mapping detected techniques |
| Nmap | Network scanning simulation (attacker tool) |
| Hydra | SSH brute force simulation (attacker tool) |

---

## Detections — 5 Attack Types

| # | Attack | MITRE Technique | Detection Logic |
|---|--------|-----------------|-----------------|
| 1 | SSH Brute Force | T1110 | > 5 failed SSH logins from same IP in 60 seconds |
| 2 | Privilege Escalation | T1548 | sudo command by non-admin user account |
| 3 | Port Scanning | T1046 | Rapid connection attempts across multiple ports |
| 4 | Lateral Movement | T1021 | Internal SSH login at unusual hours |
| 5 | Data Exfiltration | T1048 | Outbound data transfer > 500MB in short window |

---

## Project Structure

```
ai-powered-soc-dashboard/
├── README.md
├── architecture.png
├── setup/
│   ├── splunk-azure-setup.md
│   └── requirements.txt
├── detection-rules/
│   ├── brute-force.spl
│   ├── privilege-escalation.spl
│   ├── lateral-movement.spl
│   ├── port-scanning.spl
│   └── data-exfiltration.spl
├── mitre-attack/
│   ├── attack-mapping.md
│   └── tactics-techniques.md
├── python-automation/
│   ├── alert_triage.py
│   ├── threat_enrichment.py
│   └── incident_response.py
├── dashboards/
│   └── screenshots/
└── attack-simulation/
    ├── brute-force-sim.md
    └── lateral-movement-sim.md
```

---

## How to Run This Project

### Prerequisites
- Microsoft Azure free account
- Splunk Enterprise (free 60-day trial or developer license)
- Python 3.8+
- VirusTotal free API key

### Step 1 — Set up Azure VM
See: [setup/splunk-azure-setup.md](setup/splunk-azure-setup.md)

### Step 2 — Install Python dependencies
```bash
pip install -r setup/requirements.txt
```

### Step 3 — Load detection rules into Splunk
Import the `.spl` files from `detection-rules/` into Splunk as saved searches with alerting enabled.

### Step 4 — Simulate attacks
Follow the guides in `attack-simulation/` to generate realistic log data.

### Step 5 — Run Python automation
```bash
python python-automation/alert_triage.py
python python-automation/threat_enrichment.py
python python-automation/incident_response.py
```

---

## Key Learnings

- How a real SOC pipeline works: log collection → detection → triage → response
- Writing SPL (Splunk Processing Language) detection rules
- Mapping real attacks to MITRE ATT&CK tactics and techniques
- Using Python to automate SOC analyst tasks
- Deploying and configuring Splunk on Azure cloud

---

## Author

**Narayandas Shantan Achary**  
Aspiring SOC Analyst | Security Enthusiast  
GitHub: [shantan99](https://github.com/shantan99)

*Part of the FUTURE_CS series — hands-on cybersecurity projects building toward a SOC Analyst career.*
