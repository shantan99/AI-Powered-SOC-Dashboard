# MITRE ATT&CK — Tactics and Techniques Reference

This file explains each ATT&CK technique used in this project in plain language.

---

## T1110 — Brute Force

**Tactic:** Credential Access  
**What it is:** An attacker uses automated tools to try thousands of username and password combinations until one works.  
**Real-world example:** Hackers targeting SSH servers on cloud VMs. They use tools like Hydra or Medusa that can try 100+ passwords per second.  
**How we detect it:** More than 5 failed SSH login attempts from the same IP within 60 seconds.  
**Why it matters:** SSH brute force is one of the most common attacks on cloud VMs. Any internet-facing Linux server sees this daily.

---

## T1548 — Abuse Elevation Control Mechanism

**Tactic:** Privilege Escalation  
**What it is:** After gaining normal user access, an attacker tries to run commands as root/admin using sudo.  
**Real-world example:** Attacker logs in as `www-data` (web server user) then runs `sudo bash` to get a root shell.  
**How we detect it:** We watch for sudo commands run by accounts that are not in the approved admin list.  
**Why it matters:** Without root access, an attacker is limited. With root access, they can do anything — delete logs, install malware, create backdoors.

---

## T1046 — Network Service Discovery

**Tactic:** Discovery  
**What it is:** Before attacking, hackers scan the target network to find what ports and services are running.  
**Real-world example:** `nmap -sV 192.168.1.0/24` — scans every machine in a subnet to find web servers, databases, SSH ports.  
**How we detect it:** We count distinct destination ports contacted by a single IP within 60 seconds. More than 15 = suspicious.  
**Why it matters:** Port scanning is almost always the first step before an attack. Catching it early lets the SOC block the attacker before they find a vulnerability.

---

## T1021 — Remote Services

**Tactic:** Lateral Movement  
**What it is:** After compromising one machine, the attacker uses remote access tools (like SSH) to move to other machines on the same network.  
**Real-world example:** Attacker is on Machine A. They find credentials stored in a config file, then SSH into Machine B, C, and D.  
**How we detect it:** Successful SSH logins between internal IP addresses at unusual hours (before 8am or after 6pm).  
**Why it matters:** Lateral movement turns one compromised machine into full network access. Detecting it early limits the blast radius.

---

## T1048 — Exfiltration Over Alternative Protocol

**Tactic:** Exfiltration  
**What it is:** The attacker copies stolen data out of the network using unusual channels to avoid standard DLP (Data Loss Prevention) tools.  
**Real-world example:** Attacker uses SFTP, DNS tunneling, or raw TCP connections to send data to an external server.  
**How we detect it:** We monitor total outbound bytes per 5-minute window. More than 500MB is flagged as suspicious.  
**Why it matters:** Data exfiltration is the final step in most targeted attacks. Once data leaves the network, it cannot be retrieved.
