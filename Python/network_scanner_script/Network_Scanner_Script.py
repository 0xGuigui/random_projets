# NetworkScanner.py

import nmap
import pandas as pd
import socket
from datetime import datetime
import time

def get_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return ""

def scan_subnets(subnets, output_excel):
    nm = nmap.PortScanner()

    results = []

    for subnet in subnets:
        print(f"🔍 Scanning subnet: {subnet}")
        try:
            nm.scan(hosts=subnet, arguments='-sV -O -Pn -T 4')

            for host in nm.all_hosts():
                if nm[host].state() == "up":
                    ip = host
                    dns = get_dns(ip)

                    os = ""
                    if 'osmatch' in nm[host] and nm[host]['osmatch']:
                        os = nm[host]['osmatch'][0]['name']

                    ports = []
                    services = []
                    for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()
                        for port in sorted(lport):
                            port_info = nm[host][proto][port]
                            ports.append(str(port))
                            service = port_info['name']
                            services.append(service)

                    ports_str = ';'.join(ports)
                    services_str = ';'.join(services)

                    results.append({
                        'IP': ip,
                        'DNS': dns,
                        'Open Ports': ports_str,
                        'Services': services_str,
                        'OS': os
                    })

                    # Display the found IP
                    print(f"✅ Found IP: {ip} | DNS: {dns} | OS: {os}")
        except Exception as e:
            print(f"⚠️ Error scanning {subnet}: {e}")

    df = pd.DataFrame(results)
    df.to_excel(output_excel, index=False)
    print(f"\n📄 Scan completed. Results are saved in {output_excel}")

if __name__ == "__main__":
    print("======================================")
    print("       Network Scanner Script")
    print("     Author: 0xGuigui")
    print(f"     Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("======================================\n")
    time.sleep(2)

    # List of subnets to scan
    subnets = [
        '10.1.10.0/24',
        '10.1.20.0/24',
        '10.1.40.0/24',
        '10.1.70.0/24',
        # Add other subnets here
    ]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_excel = f'nmap_scan_results_{timestamp}.xlsx'

    scan_subnets(subnets, output_excel)