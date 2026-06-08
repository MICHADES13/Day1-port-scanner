import socket
from concurrent.futures import ThreadPoolExecutor

target = "scanme.nmap.org"
start_port = 1
end_port = 1024

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()


print(f"\nScanning Target: {target}")
print("-" * 40)

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port))

print("\nScan Completed.")
