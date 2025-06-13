import subprocess

def run_whois(domain):
    print("[*] Running WHOIS...")
    try:
        result = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=10)
        with open(f"output/{domain}_whois.txt", "w") as f:
            f.write(result.stdout)
        print("[+] WHOIS results saved.")
    except Exception as e:
        print(f"[!] WHOIS failed: {e}")
