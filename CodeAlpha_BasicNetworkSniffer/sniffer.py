#!/usr/bin/env python3
"""
Basic Network Sniffer - Continuous Mode
CodeAlpha Cyber Security Internship - Task 1
Author: [Your Name]
Date: [Current Date]
Description: A simple packet sniffer that continuously captures and analyzes network traffic.
Press Ctrl+C to stop.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP

# Counter for packets captured
packet_count = 0

def packet_callback(packet):
    """
    Callback function that processes each captured packet.
    Extracts and displays source/destination IPs, protocol, ports, and payload.
    """
    global packet_count
    packet_count += 1
    
    if IP in packet:
        # Extract IP addresses
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Identify the protocol and extract relevant information
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            payload = bytes(packet[TCP].payload)
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            payload = bytes(packet[UDP].payload)
        elif ICMP in packet:
            protocol = "ICMP"
            src_port = "N/A"
            dst_port = "N/A"
            payload = bytes(packet[ICMP].payload)
        else:
            protocol = "Other"
            src_port = "N/A"
            dst_port = "N/A"
            payload = b""
        
        # Display packet information in a clean format
        print(f"\n[# {packet_count}] {'=' * 55}")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        print(f"Source Port: {src_port}")
        print(f"Destination Port: {dst_port}")
        print(f"Payload (first 50 bytes): {payload[:50]}")
        print("=" * 60)

def main():
    """
    Main function to start the packet sniffer in continuous mode.
    """
    global packet_count
    
    print("=" * 60)
    print("      BASIC NETWORK SNIFFER - CONTINUOUS MODE")
    print("=" * 60)
    print("\n[INFO] Starting packet capture...")
    print("[INFO] Capturing packets continuously. Press Ctrl+C to stop.\n")
    
    try:
        # Sniff indefinitely (no count parameter)
        sniff(prn=packet_callback)
        
    except KeyboardInterrupt:
        print(f"\n\n[INFO] Sniffing stopped by user.")
        print(f"[INFO] Total packets captured: {packet_count}")
        print("[INFO] Goodbye!")
    except PermissionError:
        print("\n[ERROR] Permission denied! Please run with sudo:")
        print("        sudo python3 sniffer.py")
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")

if __name__ == "__main__":
    main()
