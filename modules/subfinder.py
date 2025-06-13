import subprocess

def run_subfinder(domain):
    print("[*] Running Subfinder...")
    try:
        result = subprocess.run(["subfinder", "-d", domain, "-silent"], capture_output=True, text=True, timeout=15)
        with open(f"output/{domain}_subdomains.txt", "w") as f:
            f.write(result.stdout)
        print("[+] Subfinder results saved.")
    except Exception as e:
        print(f"[!] Subfinder failed: {e}")
