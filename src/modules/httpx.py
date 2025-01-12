# httpx.py
from subprocess import run, CalledProcessError
from termcolor import colored

def run_httpx(input_file, output_file):
    command = ["httpx", "-silent", "-l", input_file, "-o", output_file]
    print(colored(f"Executing Httpx to validate subdomains from {input_file}", "yellow"))
    try:
        run(command, check=True, text=True)
    except CalledProcessError as e:
        print(colored(f"Error: Httpx failed with return code {e.returncode}.", "red"))
        return False
    except FileNotFoundError:
        print(colored("Error: Httpx not found. Please ensure it is installed and in your PATH.", "red"))
        return False

    print(colored(f"Httpx completed successfully. Results saved to {output_file}.", "green"))
    return True
