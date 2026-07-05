# Attack Simulation — Lateral Movement

This guide shows how to simulate lateral movement — an attacker who has already accessed one machine and is now moving to other machines on the same internal network.

> **Important:** Only simulate this within your own Azure environment. Never test on networks you don't own.

---

## What This Simulates

After gaining access to Machine A, an attacker discovers credentials and uses them to SSH into Machine B at 2am — outside normal business hours. This matches MITRE ATT&CK **T1021 — Remote Services**.

---

## Setup Required

- Two Azure VMs on the same virtual network (VNet)
- Machine A (compromised): `10.0.0.10`
- Machine B (target): `10.0.0.20`
- Both running Ubuntu Server with SSH enabled

---

## Steps

### Step 1 — SSH from Machine A to Machine B at an unusual hour

From Machine A:
```bash
ssh azureuser@10.0.0.20
```

Do this at an unusual hour — before 8am or after 6pm — to trigger the detection rule. The time is recorded in auth.log.

### Step 2 — Check what gets logged

On Machine B, the successful login will be recorded in `/var/log/auth.log`:
```
Jul 5 02:14:33 soc-lab-vm sshd[2341]: Accepted password for azureuser from 10.0.0.10 port 52134 ssh2
```

Key details captured:
- Source IP: `10.0.0.10` (internal — starts with 10.)
- Hour: `02` (2am — unusual)
- Username: `azureuser`

---

## What to Expect in Splunk

After the simulation, run the `lateral-movement.spl` query in Splunk. You should see:
- `username` = azureuser
- `hour` = 2 (2am)
- `source_ips` = 10.0.0.10
- `severity` = HIGH
- `attack_type` = Lateral Movement
- `mitre_technique` = T1021

---

## Why This Matters

In a real attack, lateral movement often goes undetected because the attacker is using **legitimate credentials** that were stolen earlier. The only way to catch it is by detecting unusual timing or unusual source machines — which is exactly what this detection rule does.
