# main.py
import os
import re
import signal
from datetime import datetime
from termcolor import colored
from subfinder import run_subfinder
from assetfinder import run_assetfinder
from puredns import run_puredns
from dnsx import run_dnsx
from httpx import run_httpx
from merge import merge_and_remove_duplicates
import shutil

terminate_flag = False

REQUIRED_TOOLS = ["subfinder", "assetfinder", "puredns", "httpx"]

def print_logo():
    logo = """
        ██████╗ ██╗   ██╗██████╗██████╗ ███████╗██╗   ██╗██████╗
        ██╔══██╗██║   ██║  ██   ██╔══██╗██╔════╝██║   ██║██╔══██╗
        ███████║██║   ██║  ██   ██║  ██║███████╗██║   ██║██████╔ 
        ██╔══██║██║   ██║══██═  ██║  ██║  ╔══██╝██║   ██║██╔══██═
        ██║  ██║╚██████╔╝  ██║  ██████╔╝███████╗╚██████╔╝██████║     
        ╚═╝  ╚═╝ ╚═════╝  ╚╝╚╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚╝      
    """
    print(colored(logo, "green"))
    credit = "#### Developed By: SAKIB SHAIKH 🗿"
    print(colored(credit, "magenta"))

def is_valid_domain(domain):
    pattern = r"^(?!\-)([A-Za-z0-9\-]{1,63}(?<!\-)\.)+[A-Za-z]{2,6}$"
    return bool(re.match(pattern, domain))

def check_required_tools():
    missing_tools = []

    for tool in REQUIRED_TOOLS:
        if shutil.which(tool) is None:
            missing_tools.append(tool)
    
    if missing_tools:
        print(colored("Missing tools detected! Please install the following tools before proceeding:\n", "red"))
        for tool in missing_tools:
            print(colored(f" - {tool}", "yellow"))
        return False

    print(colored("Fantastic! All required tools are installed. You're ready to proceed.\n", "green"))
    return True

def signal_handler(sig, frame):
    global terminate_flag
    terminate_flag = True
    print(colored("\nExecution interrupted by user. Exiting gracefully...", "yellow"))

def cleanup():
    print(colored("Returning to the normal state...", "cyan"))

def main():
    global terminate_flag
    signal.signal(signal.SIGINT, signal_handler)
    print_logo()

    if not check_required_tools():
        return
    
    try:
        domain = ""
        while not domain and not terminate_flag:
            user_input = input(colored("Enter the domain: ", "blue")).strip()
            if is_valid_domain(user_input):
                domain = user_input
            elif not terminate_flag:
                print(colored("Error: Invalid domain. Please enter a valid domain name.", "red"))

        wordlist = ""
        while not wordlist and not terminate_flag:
            wordlist_input = input(colored("Enter the path to the subdomain wordlist: ", "blue")).strip()
            if os.path.exists(wordlist_input):
                wordlist = wordlist_input
            elif not terminate_flag:
                print(colored("Error: Wordlist file not found. Please provide a valid file path.", "red"))

        resolver = ""
        while not resolver and not terminate_flag:
            resolver_input = input(colored("Enter the path to the resolver file: ", "blue")).strip()
            if os.path.exists(resolver_input):
                resolver = resolver_input
            elif not terminate_flag:
                print(colored("Error: Resolver file not found. Please provide a valid file path.", "red"))

        if terminate_flag:
            cleanup()
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_dir = f"{domain}_{timestamp}"
        os.makedirs(output_dir, exist_ok=True)

        #SubFinder
        subfinder_output = f"{output_dir}/subfinder_output.txt"
        if not run_subfinder(domain, subfinder_output) or terminate_flag:
            cleanup()
            return

        #AssetFinder
        assetfinder_output = f"{output_dir}/assetfinder_output.txt"
        if not run_assetfinder(domain, assetfinder_output) or terminate_flag:
            cleanup()
            return


        #PureDNS
        puredns_output = f"{output_dir}/puredns_output.txt"
        if not run_puredns(domain, wordlist, resolver, puredns_output) or terminate_flag:
            print(colored("Error running PureDNS.", "red"))
            cleanup()
            return

        #Merging
        merged_output = f"{output_dir}/merged_output.txt"
        if not merge_and_remove_duplicates(subfinder_output, assetfinder_output, puredns_output, merged_output) or terminate_flag:
            print(colored("Error during merging subdomains.", "red"))
            cleanup()
            return
        
        #Httpx Validation
        valid_output = f"{output_dir}/valid_domains.txt"
        if not run_httpx(merged_output, valid_output) or terminate_flag:
            cleanup()
            return

        print(colored(f"Valid subdomains saved to {valid_output}", "green"))

        # DNSX Execution
        ipv4_output = f"{output_dir}/IPv4_output.txt"
        if not run_dnsx(merged_output, ipv4_output) or terminate_flag:
            cleanup()
            return

        print(colored(f"Valid subdomains with their A records saved to {ipv4_output}", "green"))

    except Exception as e:
        print(colored(f"An unexpected error occurred: {e}", "red"))
    finally:
        if terminate_flag:
            cleanup()
        else:
            print(colored("Execution completed.", "green"))

if __name__ == "__main__":
    main()
