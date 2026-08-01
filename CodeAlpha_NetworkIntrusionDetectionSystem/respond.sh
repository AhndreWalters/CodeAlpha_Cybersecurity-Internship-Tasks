#!/bin/bash
# Auto-response script for Suricata alerts

tail -f /var/log/suricata/fast.log | while read line; do
    if echo "$line" | grep -q "Port Scan Detected"; then
        IP=$(echo "$line" | grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | head -1)
        sudo iptables -A INPUT -s $IP -j DROP
        echo "$(date): Blocked $IP" >> /var/log/blocked.log
    fi
done