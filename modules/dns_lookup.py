import subprocess

def run_dns_lookup(domain):
    print("[*] Running DNS Lookup (nslookup)...")
    try:
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True, timeout=10)
        with open(f"output/{domain}_dns.txt", "w") as f:
            f.write(result.stdout)
        print("[+] DNS lookup results saved.")
    except Exception as e:
        print(f"[!] DNS Lookup failed: {e}")
