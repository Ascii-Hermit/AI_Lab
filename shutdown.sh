#!/bin/bash

# Define the IP address range of your network
network="172.48.16.52"

# Define the username and password for SSH access
username="student"
password="student"

# Function to check if a device is connected and shut it down
shut_down_device() {
    device_ip="$1"
    echo "Checking device at $device_ip..."
    if ping -c 1 "$device_ip" &> /dev/null; then
        echo "Device is connected, shutting down..."
        sshpass -p "$student" ssh "$student@$device_ip" 'sudo shutdown -h now'
    else
        echo "Device is not connected."
    fi
}

# Iterate through IP addresses in the network range
for i in ip.txt; do
    device_ip="$i"
    shut_down_device "$device_ip"
done
