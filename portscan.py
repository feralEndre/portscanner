# 
# Simple port open check and scan 
#

import socket
import sys

def port_scanner(ip, port):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout for the connection
            s.settimeout(1)
            # Try to connect to the specified IP and port
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} on {ip} is OPEN")
            else:
                print(f"Port {port} on {ip} is CLOSED")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        # Ensure correct number of arguments
        if len(sys.argv) != 3:
            raise ValueError("Usage: python port_scanner.py <IP_ADDRESS> <PORT>")
        
        # Parse command-line arguments
        ip_address = sys.argv[1]
        port = int(sys.argv[2])
        
        # Call the port scanner function
        port_scanner(ip_address, port)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")