from scapy.all import rdpcap, DNSQR, UDP

pcap_extract = rdpcap('Boston2016.pcap')

packets = pcap_extract[DNSQR]

packet_chksum = []

for i in packets:
    if i[UDP].an is None:
        packet_chksum.append(format(i[UDP].chksum, '04x'))

exfiltrated_hex = ''.join(packet_chksum)

exfiltrated_bytes = bytes.fromhex(exfiltrated_hex)

exfiltrated_ascii = exfiltrated_bytes.decode("ASCII")

print('\n')
print(exfiltrated_ascii)
print('\n')