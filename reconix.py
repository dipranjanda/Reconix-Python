import os
from modules.whois_lookup import run_whois
from modules.dns_lookup import run_dns_lookup
from modules.ping_test import run_ping
from modules.subfinder import run_subfinder

def print_banner():
    print("="*40)
    print("         Reconix v1.0 (Python)        ")
    print("   Lightweight CLI Recon Tool in Python")
    print("="*40)

def main():
    print_banner()
    domain = input("Enter target domain (e.g. example.com): ").strip()

    print("\nSelect recon modules to run:")
    print("1. WHOIS Lookup")
    print("2. DNS Lookup")
    print("3. Ping Test")
    print("4. Subdomain Enumeration (Subfinder)")
    print("Enter choices separated by commas (e.g. 1,3,4): ", end="")
    choices = input().split(",")

    os.makedirs("output", exist_ok=True)

    for choice in choices:
        choice = choice.strip()
        if choice == '1':
            run_whois(domain)
        elif choice == '2':
            run_dns_lookup(domain)
        elif choice == '3':
            run_ping(domain)
        elif choice == '4':
            run_subfinder(domain)
        else:
            print(f"[!] Invalid option: {choice}")

    print("\n[+] Recon complete. Results saved in the 'output/' directory.")

if __name__ == "__main__":
    main()
