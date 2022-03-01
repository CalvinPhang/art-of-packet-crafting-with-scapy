from scapy.all import IP, TCP, sr1, sr 
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def help_text():
    print("\nUsage:\n python tcp_syn_scan.py target_ip_address\n")
    sys.exit()

def scan_port(ip):
    closed_port_counter = 0
    open_ports = []
    print("Please wait ....", end = "\r")
    for port in range(1,1025):
        tcp_connect_scan_resp = sr1( IP(dst=ip)/TCP(sport=1500,dport=port,flags="S"),verbose=0,timeout=10 )
        if tcp_connect_scan_resp is None:
            closed_port_counter += 1
        elif tcp_connect_scan_resp.haslayer(TCP):
            if tcp_connect_scan_resp.getlayer(TCP).flags == 0x12 :
                send_rst = sr( IP(dst=ip)/TCP(sport=1500,dport=port,flags="AR"),verbose=0,timeout=10 )
                open_ports.append(port)
            elif tcp_connect_scan_resp.getlayer(TCP).flags == 0x14 :
                closed_port_counter += 1
    print('Scan results :                   \n')
    for port in open_ports:
        print(f'Port {port} is open')
    print(f"\n{closed_port_counter} ports are closed\n")     
      
if __name__ == '__main__':
    if len(sys.argv) < 2:
        help_text()
    ip = sys.argv[1]
    scan_port(ip)