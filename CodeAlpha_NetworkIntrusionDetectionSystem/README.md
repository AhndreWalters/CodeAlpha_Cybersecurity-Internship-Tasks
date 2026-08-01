# Network Intrusion Detection System

A Network Intrusion Detection System (NIDS) built with Suricata as Task 4 for the CodeAlpha Cyber Security Internship. This system monitors network traffic in real-time, detects suspicious activity using custom rules, and implements automated response mechanisms to block potential threats.

<img width="1920" height="1080" title="Suricata Test" alt="Screenshot 2026-08-01 194549" src="https://github.com/user-attachments/assets/63d09906-b5b9-49c4-a5e4-146a822a3572" />

<img width="1920" height="1080" title="Alerts Detected" alt="Screenshot 2026-08-01 194850" src="https://github.com/user-attachments/assets/58c9d36e-203d-42d9-9797-8384291f6090" />

### Features

- Real-time network traffic monitoring
- Custom detection rules
- Automated response (IP blocking)
- Alert logging

### Rules Included
- **ICMP Ping Detection** - Detects ping requests
- **Port Scan Detection** - Detects port scanning activity
- **SSH Brute Force Detection** - Detects multiple SSH login attempts

### Installation

```bash
sudo apt update
sudo apt install suricata -y
```

### Usage
#### Start Suricata
```bash
sudo suricata -i eth0 -c /etc/suricata/suricata.yaml
```

#### Run Response Script
```bash
sudo ./respond.sh
```

#### View Alerts
```bash
sudo tail -f /var/log/suricata/fast.log
```

---

<b>[&copy; Ahndre Walters](https://github.com/AhndreWalters/CodeAlpha_Cybersecurity-Internship-Tasks/blob/main/LICENSE)</b>
