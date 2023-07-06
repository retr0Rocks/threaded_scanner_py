from socket import *
from concurrent.futures import ThreadPoolExecutor
import argparse

def test_port_number(host, port):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(3)
        try:
            sock.connect((host, port))
            return True
        except:
            return False

def port_scan(host, ports):
    with ThreadPoolExecutor(len(ports)) as executor:
        results = executor.map(test_port_number, [host]*len(ports), ports)
        for port,is_open in zip(ports,results):
            if is_open:
                print(f'> {host}:{port} open')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "port scanner")
    parser.add_argument("ip", help = "ip to scan")
    parser.add_argument("range", help = "range to scan from")
    args = parser.parse_args()
    ports = range(int(args.range))
    port_scan(args.ip, ports)
