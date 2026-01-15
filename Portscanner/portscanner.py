import socket 
from datetime import datetime

def scan_port(target_host, port):
    """
    Attempt to connect to a single port.
    Returns True if port is open (Connection Successful).
    """
    try:
        #Create a TCP/IP Socket (AF_INET = IPv4, SOCK_STREAM = TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Set a short timeout so we don't hang on a closed port
        sock.settimeout(1.0) #1 Second

        #Try to connect > Returns 0 on sucess, error code if failed
        result = sock.connect_ex((target_host, port))

        sock.close () # Makes sure the sock is closed

        return result == 0 #0 means port was sucessful
    except Exception:
        return False

    def main ():
        # ***CONFIG***
        target = input ("Enter Taret (IP or hostname, Example: 192.168.1.1 or scanme.nmap.org): ").strip()
        start_port = int(input("start port (Example: 1): "))
        end_port = int(input("End port (Example: 1024): " ))

        print(f"\nScanning {target} from port {start_port} through {end_port}...")
        print(f"\nStarted at: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

        open_ports = []
        
        for port in range (start_port, end_port + 1):
            if scan_port(target, port):
                print(f"port {Port:>5} > OPEN")
                open_ports.append(port)
            else:
                # print(f"Port {Port:>5} > CLOSED")
                pass

        print(f"\nScan finished at: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
         if open_ports:
          print(f"Open Ports Found {open_ports}")
         else:
        print(f"No Open ports found in the scan range.")
         if __name__ == "__main__":
main()


