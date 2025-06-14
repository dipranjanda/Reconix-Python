import subprocess
import shutil

def run_subfinder(domain):
    print("[*] Running Subfinder...")
    
    if not shutil.which("subfinder"):
        print("[!] Subfinder not found on this system.")
        print("    Please install it or skip this module.")
        return
    
    try:
        result = subprocess.run(
            ["subfinder", "-d", domain, "-silent"],
            capture_output=True, text=True, timeout=20
        )
        with open(f"output/{domain}_subdomains.txt", "w") as f:
            f.write(result.stdout)
        print("[+] Subfinder results saved.")
    except Exception as e:
        print(f"[!] Subfinder failed: {e}")
