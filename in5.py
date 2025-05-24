from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def process_packet(packet):
    print("="*60)
    print(f"Time: {datetime.now()}")

    if IP in packet:
        ip_layer = packet[IP]
        print(f"From: {ip_layer.src} --> To: {ip_layer.dst}")

        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print(f"Protocol: TCP")
            print(f"Ports: {tcp_layer.sport} --> {tcp_layer.dport}")
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print(f"Protocol: UDP")
            print(f"Ports: {udp_layer.sport} --> {udp_layer.dport}")
        else:
            print(f"Protocol: Other (not TCP/UDP)")

        if packet.haslayer(Raw):
            try:
                payload = packet[Raw].load
                print(f"Payload: {payload.decode('utf-8', errors='replace')}")
            except Exception as e:
                print(f"Could not decode payload: {e}")

def main():
    print("📡 Starting Packet Sniffer... Press Ctrl+C to stop.\n")
    try:
        sniff(filter="ip", prn=process_packet, store=False)
    except PermissionError:
        print("❌ Permission Denied! Try running as admin/root.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
