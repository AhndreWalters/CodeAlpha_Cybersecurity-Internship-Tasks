# Basic Network Sniffer

A Python-based network packet sniffer developed as Task 1 for the CodeAlpha Cyber Security Internship. This program captures and analyzes live network traffic using the Scapy library, displaying essential information such as source/destination IP addresses, protocols (TCP, UDP, ICMP), port numbers, and packet payload data. The tool provides hands-on understanding of how data flows through networks and the structure of network packets.

## Requirements
- Python 3
- Scapy library
- Root privileges (for packet capture)

## Installation
```bash
sudo pip3 install scapy
```

## Usage
```bash
sudo python3 sniffer.py
```
Press <code>Ctrl+C</code> to stop the sniffer.

## Features
- Captures network packets
- Shows source and destination IP addresses
- Identifies protocols (TCP, UDP, ICMP)
- Displays source/destination ports
- Shows packet payload data

## Screenshots
<h3>Starting the Sniffer</h3>
<img width="1920" height="1080" alt="Screenshot 2026-07-22 185059" src="https://github.com/user-attachments/assets/f029a26c-1970-412c-b611-2e5a9a9b9147" />

<h3>Capturing Packets in Real-Time</h3>
<img width="1920" height="1080" alt="Screenshot 2026-07-22 184851-2" src="https://github.com/user-attachments/assets/cef2b512-648c-4c83-90fa-7d8cbe2aeb57" />

## Sample Output
```bash
============================================================
Source IP: 192.168.1.100
Destination IP: 142.250.185.46
Protocol: TCP
Source Port: 54321
Destination Port: 443
Payload (first 50 bytes): b'\x17\x03\x03\x00N\x00\x00...'
============================================================
```

<b>[&copy; 2026 Ahndre Walters](https://github.com/AhndreWalters/CodeAlpha_BasicNetworkSniffer/blob/main/LICENSE)</b>
