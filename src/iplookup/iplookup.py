import socket
import requests
import maxminddb
import json
import csv

def main(args):
    target = args.target
    results = {}
    
    if args.dns:
        results["DNS Lookup"] = dns_lookup(args.target, ipv6=args.ipv6)
    
    if args.reverse:
        results["Reverse DNS"] = reverse_dns(args.target, ipv6=args.ipv6)
    
    if args.geo:
        results["Geolocation Lookup"] = geo(args.target, include_asn=args.asn)
                
    if not args.output:
        print_results(results)
    else:
        output(results, args)
        
    
def dns_lookup(targetip, ipv6=False):
    try:
        if ipv6:
            adr_info = socket.getaddrinfo(targetip, None, socket.AF_INET6)
            ip_addrs = [adr_info[4][0] for info in adr_info]
            result = {
                "Hostname": targetip,
                "IP Addresses (IPv6)": ip_addrs
            }
        else:
            
            info = socket.gethostbyname_ex(targetip)
        
            hostname, aliaslist, ipaddrlist = info
        
            result = {
                "Hostname": hostname,
                "Aliases": aliaslist,
                "IP Addresses": ipaddrlist
            }
        return result
    except socket.gaierror as e:
        return(f"DNS lookup failed for {targetip}: {e}")
    
def reverse_dns(targetip, ipv6=False):
    try:
        if ipv6:
            addr_info = socket.getaddrinfo(targetip, None, socket.AF_INET6)
            ip_addrs = [addr_info[4][0] for info in addr_info]
            results = {}
            for info in addr_info:
                ip = info[4][0]
                try:
                    hostname, _, _ = socket.gethostbyaddr(ip)
                    results[ip] = hostname 
                except socket.herror:
                    results[ip]=("No Hostname found for IPv6 Address.")
            return results
        else:
            
            hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(targetip)
            return {
                "Hostname": hostname,
                "Aliases": aliaslist,
                "IP Addresses": ipaddrlist
            }
    except socket.herror as e:
        return(f"Failed Reverse DNS lookup for {targetip}: {e}")        
            
def geo(targetip,  include_asn=False, db_path="src/extra/country_asn.mmdb"):
    try:
        
        with maxminddb.open_database(db_path) as reader:
            response = reader.get(targetip)
            print(response)
            if not response:
                return "No Data Found for this IP"  
        
            result = {
                "Continent": response.get("continent_name"),
                "Country": response.get("country_name"),
                "Continent Code": response.get("continent"),
                "Country Code": response.get("country"),
            }

            if include_asn:
                result["ASN"] = response.get("as_name")
                result["ASN Number"] = response.get("asn")
                result["ASN Domain"] = response.get("as_domain")

            return result
    
    except Exception as e:
        return f"An error occurred: {e}"

def output(results, args):
    try:
        output_path = args.output
        if args.json:
            with open(output_path, "w") as json_file:
                json.dump(results,json_file, indent=0)
            print(f"Results saved to {output_path} in JSON format.")
        elif args.csv:
            with open(output_path, "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Category", "Key", "Value"])
                for category, data in results.items():
                    if isinstance(data, dict):
                        for key, value in data.items():
                            writer.writerow(category, key, value)
                    elif isinstance(data, list):
                        for item in data:
                            writer.writerow([category, "List Item", item])
                    else:
                        writer.writerow([category, "Value", data])
                print(f"Results saved to {output_path}")
            
    except Exception as e:
        print("An error occurred: {a}")
    
def print_results(results):
    for key, value in results.items():
        print(f"{key}:")
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        elif isinstance(value, list):
            for item in value:
                print(f"  -{item}")
        else:
            print(f"  {value}")
    print("\n")