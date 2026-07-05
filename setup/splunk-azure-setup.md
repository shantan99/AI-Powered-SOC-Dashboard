# Setup Guide — Splunk on Microsoft Azure

This guide walks through setting up the full project environment: an Azure Linux VM with Splunk Enterprise installed, log forwarding configured, and detection rules loaded.

---

## Prerequisites

- Microsoft Azure free account (portal.azure.com)
- Splunk Enterprise free developer license (splunk.com/en_us/download.html)
- Basic Linux command line knowledge

---

## Part 1 — Create Azure Virtual Machine

1. Log in to portal.azure.com
2. Click **Create a resource** → **Virtual Machine**
3. Configure:
   - Resource group: `soc-lab-rg` (create new)
   - VM name: `soc-lab-vm`
   - Region: UK South (or your nearest region)
   - Image: **Ubuntu Server 22.04 LTS**
   - Size: Standard B2s (2 vCPUs, 4GB RAM — enough for Splunk free)
   - Authentication: SSH public key (recommended) or password
4. Under **Networking**, allow inbound ports:
   - SSH (22)
   - Splunk Web (8000)
5. Click **Review + Create** → **Create**

---

## Part 2 — Install Splunk Enterprise on the VM

SSH into your Azure VM:
```bash
ssh azureuser@<your-vm-public-ip>
```

Download and install Splunk:
```bash
wget -O splunk-9.2.0-linux-2.6-amd64.deb \
  "https://download.splunk.com/products/splunk/releases/9.2.0/linux/splunk-9.2.0-linux-2.6-amd64.deb"

sudo dpkg -i splunk-9.2.0-linux-2.6-amd64.deb

sudo /opt/splunk/bin/splunk start --accept-license
```

Enable Splunk to start on boot:
```bash
sudo /opt/splunk/bin/splunk enable boot-start
```

Access Splunk Web at: `http://<your-vm-public-ip>:8000`  
Default credentials: `admin` / (set during first start)

---

## Part 3 — Configure Log Collection

Enable syslog monitoring in Splunk:

1. In Splunk Web → **Settings** → **Data Inputs**
2. Add **Files & Directories** input:
   - File path: `/var/log/auth.log`
   - Source type: `linux_secure`
3. Add another input:
   - File path: `/var/log/syslog`
   - Source type: `syslog`

---

## Part 4 — Load Detection Rules

For each `.spl` file in the `detection-rules/` folder:

1. In Splunk Web → **Search & Reporting**
2. Paste the SPL query into the search bar
3. Run the search to verify it works
4. Click **Save As** → **Alert**
5. Configure: Trigger when results > 0, every 5 minutes
6. Set alert action: Log to index (for dashboard)

---

## Part 5 — Azure Network Security Group (NSG) Rules

To allow `incident_response.py` to block IPs automatically:

1. In Azure Portal → **Network Security Groups** → `soc-lab-nsg`
2. Note the NSG name and resource group
3. Update `incident_response.py` with your values:
   ```python
   AZURE_RESOURCE_GROUP = "soc-lab-rg"
   AZURE_NSG_NAME       = "soc-lab-nsg"
   ```

For full Azure SDK integration, install the Azure Python SDK:
```bash
pip install azure-mgmt-network azure-identity
```

---

## Estimated Setup Time

| Step | Time |
|------|------|
| Create Azure VM | 5 minutes |
| Install Splunk | 10 minutes |
| Configure log inputs | 10 minutes |
| Load detection rules | 15 minutes |
| Test with attack simulation | 20 minutes |
| **Total** | **~1 hour** |
