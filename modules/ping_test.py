import subprocess

def run_ping(domain):
    print("[*] Running Ping Test...")
    try:
        result = subprocess.run(["ping", "-c", "4", domain], capture_output=True, text=True, timeout=10)
        with open(f"output/{domain}_ping.txt", "w") as f:
            f.write(result.stdout)
        print("[+] Ping results saved.")
    except Exception as e:
        print(f"[!] Ping test failed: {e}")
