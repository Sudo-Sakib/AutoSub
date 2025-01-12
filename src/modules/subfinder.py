# subfinder.py
from subprocess import run, CalledProcessError
from termcolor import colored

def run_subfinder(domain, output_file):
    command = ["subfinder", "-d", domain, "-silent", "-o", output_file]
    print(colored(f"Executing Subfinder for domain: {domain}", "yellow"))
    try:
        run(command, check=True, text=True)
    except CalledProcessError as e:
        print(colored(f"Error: Subfinder failed with return code {e.returncode}.", "red"))
        return False
    except FileNotFoundError:
        print(colored("Error: Subfinder not found. Please ensure it is installed and in your PATH.", "red"))
        return False
    
    return True
