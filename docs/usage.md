# Cyber Swiss Army Tool Usage Guide

![GitHub last commit](https://img.shields.io/github/last-commit/zarfix123/SwissCyberKnife)
![GitHub](https://img.shields.io/github/license/zarfix123/SwissCyberKnife)

## Port Scanner Commands and Options

### Command Structure

'''bash
swissknife port-scanner --target <target> [OPTIONS] 
'''

Options

   - --target / -t: Required. Target IP address or domain.
   - --start-port / -sp: Starting port number for the scan range. Default is 1.
   - --end-port / -ep: Ending port number for the scan range. Default is 1024.
   - --all / -a: Scan all ports from 1 to 65535. Overrides --start-port and --end-port.
   - --common / -c: Scan only the most common ports. 
   - --tcp: Perform a TCP scan (default if neither --tcp nor --udp specified). 
   - --udp: Perform a UDP scan. 
   - --banner / -b: Enable banner grabbing for open ports to retrieve service information.  
   - --output / -o: Specify output file to save results (if used, requires --format).
   - --format / -f: Format for output file. Choices are txt, json, csv.
   - --threads / -th: Number of threads to use for parallel scanning. Default is 1. 
   - --timeout / -to: Timeout (in seconds) for each connection attempt. Default is 0.5.
   - --retries / -r: Number of retries for each port if scan fails initially. Default is 1.
   - --verbose / -v: Show detailed scan progress in the console.

### Example Usage

- **Basic TCP Scan on localhost**
 ```bash
 swissknife port-scanner -t localhost -sp 20 -ep 25 --tco
 ```
- **Full TCP Port Scan with Banner Grabbing**
 ```bash
 swissknife port-scanner -t 192.168.1.1 -a -b
 ```
- **Common Ports Only, Multi-Threaded Scan**
 ```bash
 swissknife port-scanner -t example.com -c -th 5
 ```
- **UDP Scan with Retries and Custom Timeout**
 ```bash
 swissknife port-scanner -t 192.168.1.1 --udp -sp 53 -ep 53 -to 1 -r 3
 ```
- **Save Results to File in JSON Format**
 ```bash
 swissknife port-scanner -t 192.168.1.1 -sp 80 -ep 80 -o results.json -f json
 ```

### Notes
- Use ```sudo``` if permissions are needed for specific ports.