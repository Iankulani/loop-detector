# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:39:25 2024

@author: IAN CARTER KULANI

"""

import re

def detect_loops_and_control_structures(assembly_code):
    # Define regular expressions for various control structures and loops
    loop_patterns = [
        r'\bfor\b',       # Detects 'for'
        r'\bwhile\b',     # Detects 'while'
        r'\bswitch\b',    # Detects 'switch'
        r'\bcase\b',      # Detects 'case'
        r'\bbreak\b',     # Detects 'break'
        r'\bdefault\b',   # Detects 'default'
        r'\bgoto\b'       # Detects 'goto' (optional, often used in loops/branches)
    ]
    
    # Combine the patterns into one regex
    combined_pattern = '|'.join(loop_patterns)
    
    # Use re.findall to search for the patterns in the assembly code
    matches = re.findall(combined_pattern, assembly_code, flags=re.IGNORECASE)
    
    return matches

def read_assembly_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None

def main():
    print("============================LOOP DETECTOR============================\n")
    # Prompt user for the assembly file path
    file_path = input("Enter the path of the assembly file to analyze:")

    # Read the content of the assembly file
    assembly_code = read_assembly_file(file_path)
    
    if assembly_code:
        # Detect loops and control structures in the assembly code
        detected_structures = detect_loops_and_control_structures(assembly_code)

        if detected_structures:
            print("\nDetected loops and control structures:")
            for structure in set(detected_structures):  # Using set to remove duplicates
                print(f"- {structure}")
        else:
            print("No loops or control structures detected in the assembly code.")
    
if __name__ == "__main__":
    main()
