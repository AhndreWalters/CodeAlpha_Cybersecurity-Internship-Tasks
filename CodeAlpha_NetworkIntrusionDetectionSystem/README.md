# Network Intrusion Detection System

Network Intrusion Detection System (NIDS) set up with Snort as Task 4 for the CodeAlpha Cyber Security Internship. This system monitors network traffic in real-time, detects suspicious activity using custom rules for ICMP ping, port scans, and SSH brute force attempts, and implements automated response mechanisms to block malicious IP addresses. Includes configuration files, custom rules, and response scripts for continuous threat monitoring.

### Features

- Real-time network traffic monitoring
- Custom detection rules
- Automated response (IP blocking)
- Alert logging

### Installation

```bash
sudo apt update
sudo apt install snort -y
```

### Rules Included
- ICMP Ping Detection
- Port Scan Detection
- SSH Brute Force Detection

### Usage
#### Start Snort
```bash
sudo snort -i eth0 -c /etc/snort/snort.conf -A console
```

#### Run Response Script
```bash
sudo ./respond.sh
```

#### View Alerts
```bash
sudo cat /var/log/snort/alert
```

<br>

<b>[&copy; Ahndre Walters](https://github.com/AhndreWalters/CodeAlpha_Cybersecurity-Internship-Tasks/blob/main/LICENSE)</b>
