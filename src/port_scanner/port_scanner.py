import socket
import concurrent.futures as con
import json
import csv

COMMON_PORTS = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389] 
#ftp, ssh, telnet, smtp, dns, http, pop3, imap, https, smb, rdp


def main(args):
    
    if args.verbose:
        print(f"Starting scan on {args.target} from port {args.start_port} to {args.end_port}! ")
        print(f"Scan type: {'UDP' if args.udp else 'TCP'}")
    
    if args.common:
        ports_to_scan = COMMON_PORTS
    elif args.all:
        ports_to_scan = range(1, 65536)
    else:
        ports_to_scan = range(args.start_port, args.end_port +1)
    
    results = run_scan(args, ports_to_scan)
    output_results(results, args.output, args.format)
    
def run_scan(args, ports_to_scan):
    results = {}
    with con.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []
        for port in ports_to_scan:
            if args.udp:
                futures.append(executor.submit(udp_scan, args.target, port, args.timeout, args.retries))
            else:
                futures.append(executor.submit(tcp_scan, args.target, port, args.timeout, args.retries))
                
            
        
        for future in con.as_completed(futures):
            result = future.result()
            if result:
                port, status = result
            #optionally add banner grabbing
                if args.banner:
                    banner = banner_grab(args.target, port)
                    status = f"open ({banner})" if banner else "open"
                results[port] = status
            
    return results



def tcp_scan(target, port, timeout, retries):
    for attempt in range(retries):
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((target,port))
                if result == 0:
                    return port, "open"
        except Exception:
            pass
    return None
    
def udp_scan(target, port, timeout, retries):
    for attempt in range(retries):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(timeout)
                s.sendto(b"", {target,port})
                try:
                    s.recvfrom(1024)
                    return port, "open"
                except socket.timeout:
                    return port, "closed"
        except Exception:
            pass
    return None
    
def banner_grab(target, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((target, port))
            banner = s.recv.decode().strip()
            return banner
    except:
        return None
    
    
def output_results(results, output_file, format):
    if output_file:
        with open(output_file, "w") as f:
            if format == "json":
                json.dump(results, f, indent=4)
            elif format == "csv":
                write = csv.writer(f)
                write.writerow(["Port", "Status"])
                for port, status in results.items():
                    f.write([port, status])
            else:
                for port, status in results.items():
                    f.write(f"Port: {port}, Status: {status}\n")
        print(f"Results saved to {output_file} via {format}")
    else:
        print("Scan Results: ")
        for port, status in results.items():
            print(f"Port: {port}, \t\tStatus: {status} ")
            


