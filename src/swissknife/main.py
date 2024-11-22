import argparse
from port_scanner.port_scanner import main as port_scanner_main
from pass_gen.pass_gen import main as pass_gen_main
from pass_strength.pass_strength import main as pass_strength_main
from iplookup.iplookup import main as iplookup_main
from encdec.encdec import main as encdec_main

TOOLS = {
    "port-scanner": port_scanner_main,
    "pass-gen": pass_gen_main,
    "pass-strength": pass_strength_main,
    "iplookup": iplookup_main,
    "encdec": encdec_main,
}

def add_port_scanner_arguments(parser):
    # Port scanner specific arguments
    parser.add_argument("--target", "-t", required=True, help="Target IP address or domain")
    parser.add_argument("--start-port", "-sp", type=int, default=1, help="Starting port for the scan")
    parser.add_argument("--end-port", "-ep", type=int, default=1024, help="Ending port for the scan")
    parser.add_argument("--common", "-c", action="store_true", help="Scan only the most common ports")
    parser.add_argument("--all", "-a", action="store_true", help="Scan all ports (1-65535)")
    parser.add_argument("--tcp", action="store_true", help="Perform a TCP scan (default)")
    parser.add_argument("--udp", action="store_true", help="Perform a UDP scan")
    parser.add_argument("--banner", "-b", action="store_true", help="Enable banner grabbing (more detail)")
    parser.add_argument("--output", "-o", type=str, help="Specify output file to save scan results")
    parser.add_argument("--format", "-f", choices=["txt", "json", "csv"], help="Specify output format")
    parser.add_argument("--threads", "-th", type=int, default=1, help="Number of threads to use for parallel scanning")
    parser.add_argument("--timeout", "-to", type=float, default=0.5, help="Set the timeout for each scan attempt")
    parser.add_argument("--retries", "-r", type=int, default=1, help="Number of retries per port if scan fails")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed scan progress")

def add_pass_strength_arguments(parser):
    parser.add_argument("password", type=str, help="Password or hash to analyze")
    parser.add_argument("--hash-check", "-hc", action="store_true", help="Check if input is a known hash and has collisions")
    parser.add_argument("--entropy", "-en", action="store_true", help="Calculate provided passwords entropy (only works for passwords not hash)")
    parser.add_argument("--rockyou-check", "-ry", action="store_true", help="Check if password contains common dictionary words (rockyou)")
    parser.add_argument("--wordlist", "-wl", type=str, help="Check if password contains words from provided wordlist (give path)")

def add_pass_gen_arguments(parser):
    parser.add_argument("--length", "-l", type=int, default=15, help="Set custom length for password (defualt is 15)")
    parser.add_argument("--no-upper", "-nu", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", "-nl", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-num", "-nn", action="store_true", help="Exclude numbers")
    parser.add_argument("--no-special", "-ns", action="store_true", help="Exclude special characters")
    parser.add_argument("--exclude", "-ex", type=str, help="Accepts a string of characters to exclude")
    parser.add_argument("--alphanumeric", "-an", action="store_true", help="Give password using only alphanumeric characters")
    parser.add_argument("--hex", action="store_true", help="Gives password in hex")
    parser.add_argument("--base64", "-b64", action="store_true", help="Gives password in base64")
    parser.add_argument("--hash", action="store_true", help="This flag should be called alone. Will prompt for string and algorithm.")
    parser.add_argument("--memorable", "-mem", action="store_true", help="Leverages rockyou wordlist for a memorable password")
    parser.add_argument("--count", type=int, help="Takes an integer of how many passwords to generate")
    parser.add_argument("--seperator", "-sep", type=str, help="Takes a string of characters to use as seperator when using --memorable")

def add_iplookup_arguments(parser):
    parser.add_argument("--target", "-t", required=True, help="Target Ip to Lookup")   
    parser.add_argument("--ipv6", "-v6", action="store_true", help="Change to IPV6 mode")
    parser.add_argument("--dns", "-d", action="store_true", help="Perform a DNS lookup on the provided IP target")
    parser.add_argument("--reverse", "-rv", action="store_true", help="Perform a reverse DNS lookup")
    parser.add_argument("--geo", "-g", action="store_true", help="Fetch geolocation information for the target")
    parser.add_argument("--asn", action="store_true", help="Retrieve ASN")
    parser.add_argument("--output", "-o", type=str, help="Set output location (path)")
    parser.add_argument("--json", action="store_true", help="output in json format")
    parser.add_argument("--csv", action="store_true", help="output in csv format")
    
def main():
    parser = argparse.ArgumentParser(
        prog="swissknife",
        description="Cyber Swiss Army Toolkit\n\nUsage:\n"
                    "  swissknife {port-scanner, pass-gen, pass-strength, iplookup, encdec} -h\n"
                    "Use -h after any subcommand for specific help on that tool.",
        formatter_class=argparse.RawTextHelpFormatter,
        usage=argparse.SUPPRESS  # Suppress the default usage line
    )
    subparsers = parser.add_subparsers(dest="command", required=False)

    # Define subparsers for each tool
    port_scanner_parser = subparsers.add_parser("port-scanner", help="Run the port scanner tool")
    add_port_scanner_arguments(port_scanner_parser)
    
    pass_strength_parser = subparsers.add_parser("pass-strength", help="Run the password strength analyzer tool")
    add_pass_strength_arguments(pass_strength_parser)
    
    pass_gen_parser = subparsers.add_parser("pass-gen", help="Run the password generation tool")
    add_pass_gen_arguments(pass_gen_parser)
    
    iplookup_parser = subparsers.add_parser("iplookup", help="Run the IP lookup tool")
    add_iplookup_arguments(iplookup_parser)
    
    
    subparsers.add_parser("encdec", help="Run the encryption/decryption tool")
    args = parser.parse_args()

    # Display help message if no command is provided
    if not args.command:
        print("No command provided. Use -h after a command for specific help.\n")
        parser.print_help()
        return

    # Execute the selected tool’s main function
    if args.command in TOOLS:
        TOOLS[args.command](args)
    else:
        parser.print_help()
