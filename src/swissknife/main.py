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
    subparsers.add_parser("pass-gen", help="Run the password generation tool")
    subparsers.add_parser("pass-strength", help="Run the password strength analyzer tool")
    subparsers.add_parser("iplookup", help="Run the IP lookup tool")
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
