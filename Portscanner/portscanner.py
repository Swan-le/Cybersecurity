import socket
from datetime import datetime

def scan_port(target_host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1.0)
        
        result = sock.connect_ex((target_host, port))

        sock.close()
        
        return result == 0 
    except Exception:
        return False

def main():
    target = input("Enter Target IP or hostname. Example: 192.168.1.1: ").strip()
    common_ports = [21, 22, 23, 25, 53, 67, 68,  80, 110, 123, 135, 139, 143, 161, 162, 389, 443, 445, 514, 636, 993, 995, 1433, 1521, 1723, 2049, 3306, 3389, 5432, 5900, 6379, 8000, 8080, 8888, 8443, 9000, 1883, 8883, 873, 1750]

    print(f"\nScanning {target}, common ports: {common_ports} only")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    open_ports = []
    
    for port in common_ports:
        if scan_port(target, port):
            print(f"Port {port:>5} is OPEN")
            open_ports.append(port)
        else:
            print(f"Port {port:>5} is CLOSED")
            pass
    print(f"\nScan finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if open_ports:
        print(f"Open ports found: {open_ports}")
    else:
        print("No open ports found on target")
if __name__ == "__main__":
    main()
