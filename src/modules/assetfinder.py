# assetfinder.py
from subprocess import run, CalledProcessError
from termcolor import colored

def run_assetfinder(domain, output_file):
    command = ["assetfinder", "--subs-only", domain]
    print(colored(f"Executing Assetfinder for domain: {domain}", "yellow"))
    try:
        with open(output_file, "w") as f:
            run(command, stdout=f, check=True, text=True)
    except CalledProcessError as e:
        print(colored(f"Error: Assetfinder failed with return code {e.returncode}.", "red"))
        return False
    except FileNotFoundError:
        print(colored("Error: Assetfinder not found. Please ensure it is installed and in your PATH.", "red"))
        return False
    
    return True
