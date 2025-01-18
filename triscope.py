import os
import sys
import subprocess

# Function to print the banner
def print_banner():
    print("""
         
            

  _______ _____  _____  _____  _____ ____  _____  ______ 
 |__   __|  __ \|_   _|/ ____|/ ____/ __ \|  __ \|  ____|
    | |  | |__) | | | | (___ | |   | |  | | |__) | |__   
    | |  |  _  /  | |  \___ \| |   | |  | |  ___/|  __|  
    | |  | | \ \ _| |_ ____) | |___| |__| | |    | |____ 
    |_|  |_|  \_\_____|_____/ \_____\____/|_|    |______|
                                                         
                                                         


    """)

# Function to run Nmap scan
def nmap_scan(target, scan_type):
    print("Starting Nmap scan...")
    if scan_type == "quick":
        cmd = f"nmap -T4 --top-ports 100 {target}"
    elif scan_type == "basic":
        cmd = f"nmap -sC -sV {target}"
    elif scan_type == "full":
        cmd = f"nmap -p- -sC -sV {target}"
    print(f"Executing: {cmd}")
    os.system(cmd)

# Function to run Gobuster scan
def gobuster_scan(target, directory_wordlist):
    print("Running Gobuster scan...")
    cmd = f"gobuster dir -u {target} -w {directory_wordlist} -b 302 -o gobuster_results.txt"
    print(f"Executing: {cmd}")
    os.system(cmd)

# Function to run Nikto scan
def nikto_scan(target):
    print("Running Nikto scan...")
    cmd = f"nikto -h {target} -output nikto_results.txt"
    print(f"Executing: {cmd}")
    os.system(cmd)

# Main function to run the full scan
def run_scan(target, scan_type, wordlist):
    print_banner()

    print(f"\nStarting {scan_type} scan on {target}")

    # Run Nmap scan
    nmap_scan(target, scan_type)

    # Run Gobuster scan
    gobuster_scan(target, wordlist)

    # Run Nikto scan
    nikto_scan(target)

    print("\n--- Scan Completed ---")
    print("Results saved in:")
    print("- Nmap results: nmap_results.txt")
    print("- Gobuster results: gobuster_results.txt")
    print("- Nikto results: nikto_results.txt")

# Entry point of the script
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 triscope.py <target> <scan_type> <wordlist>")
        sys.exit(1)

    target = sys.argv[1]
    scan_type = sys.argv[2]
    wordlist = sys.argv[3]

    if scan_type not in ['quick', 'basic', 'full']:
        print("Invalid scan type. Please choose from: quick, basic, full.")
        sys.exit(1)

    run_scan(target, scan_type, wordlist)
