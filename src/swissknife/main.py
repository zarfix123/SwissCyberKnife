import argparse
from port_scanner.port_scanner import main as port_scanner_main
from pass_gen.pass_gen import main as pass_gen_main
from pass_strength.pass_strength import main as pass_strength_main
from iplookup.iplookup import main as iplookup_main
from encdec.encdec import main as encdec_main


def main():
    parser = argparse.ArgumentParser(prog="swissknife", description="Cyber Swiss Army Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # Define port-scanner subcommand
    subparsers.add_parser("port-scanner", help="Run the port scanner tool")
    subparsers.add_parser("pass-gen", help="Run the password generation tool")
    subparsers.add_parser("pass-strength", help="Run the password strength analyzer tool")
    subparsers.add_parser("iplookup", help="Run the ip lookup tool")
    subparsers.add_parser("encdec", help="Run the encryption/decryption tool")

    
    args = parser.parse_args()

    # Call the main function
    if args.command == "port-scanner":
        port_scanner_main()
    elif args.command == "pass-gen":
        pass_gen_main()
    elif args.command == "pass-strength":
        pass_strength_main()
    elif args.command== "iplookup":
        iplookup_main()
    elif args.command == "encdec":
        encdec_main()
    else:
        parser.print_help()
