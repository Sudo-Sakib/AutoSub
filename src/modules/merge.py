from termcolor import colored
import os

def merge_and_remove_duplicates(file1, file2, file3, output_file):
    """
    Merges and removes duplicates from three input files.
    :param file1: First input file
    :param file2: Second input file
    :param file3: Third input file
    :param output_file: The output file to save merged results
    :return: True if successful, False otherwise
    """
    try:
        files = [file1, file2, file3]
        unique_subdomains = set()

        for file in files:
            if os.path.exists(file):
                with open(file, 'r') as f:
                    unique_subdomains.update(f.readlines())
            else:
                print(colored(f"Warning: {file} not found, skipping.", "yellow"))

        with open(output_file, 'w') as out:
            out.writelines(sorted(unique_subdomains))

        print(colored(f"Merged and deduplicated subdomains saved to {output_file}", "green"))
        return True
    except Exception as e:
        print(colored(f"Error during merging: {e}", "red"))
        return False
