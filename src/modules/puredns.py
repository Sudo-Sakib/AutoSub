import subprocess
from termcolor import colored
import os

def run_puredns(domain, wordlist, resolver, output_file):
    """
    Runs PureDNS to brute force and resolve subdomains.
    :param domain: The target domain
    :param wordlist: The path to the subdomain wordlist
    :param resolver: The path to the resolver file
    :param output_file: The output file to save resolved subdomains
    :return: True if successful, False otherwise
    """
    command = ["puredns", "bruteforce", wordlist, domain, "-r", resolver, "-w", output_file]
    print(colored(f"Executing PureDNS for domain: {domain} using wordlist: {wordlist}", "yellow"))

    process = subprocess.run(command, shell=False, text=True, capture_output=True)

    if process.returncode != 0:
        print(colored("Error: PureDNS failed. Check the logs for details.", "red"))
        print(process.stderr)  # Output the error for debugging
        return False

    if os.path.exists(output_file):
        print(colored(f"PureDNS completed successfully. Results saved to {output_file}.", "green"))
        return True
    else:
        print(colored("Warning: PureDNS did not generate the expected output file.", "yellow"))
        return False
