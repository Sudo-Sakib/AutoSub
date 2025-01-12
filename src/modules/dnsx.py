import subprocess
import os
from termcolor import colored

def run_dnsx(input_file, output_file):
    try:
        print(colored(f"Running dnsx on {input_file} to retrieve A records...", "yellow"))
        subprocess.run(
            ["dnsx", "-l", input_file, "-a", "-resp-only", "-o", output_file],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(colored(f"A records saved to {output_file}", "green"))
        return True
    except subprocess.CalledProcessError as e:
        print(colored(f"Error running dnsx: {e}", "red"))
        return False
