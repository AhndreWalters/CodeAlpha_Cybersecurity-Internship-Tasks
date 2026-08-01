# Network Intrusion Detection System

A Network Intrusion Detection System (NIDS) built with Suricata as Task 4 for the CodeAlpha Cyber Security Internship. This system monitors network traffic in real-time, detects suspicious activity using custom rules, and implements automated response mechanisms to block potential threats.

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
