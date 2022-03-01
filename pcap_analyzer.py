from scapy.all import rdpcap, IP
import numpy as np
import sys


packet = rdpcap(sys.argv[1])

ips = []
ttls = []
filtered_1 = []
for i in range(len(packet)):
    if packet[i].haslayer(IP):
        filtered_1.append(packet[i])
for i in range (len(filtered_1)):
    ips.append(filtered_1[i][IP].src)

unique_ips, index = np.unique(ips, return_index=True)

for i in index:
    ttls.append(filtered_1[i][IP].ttl)
    
OS = []
for i in range(len(ttls)):
    if ttls[i] == 64 or ttls[i] == 63:
        OS.append("Linux")
    elif ttls[i] == 128 or ttls[i] == 127:
        OS.append("Windows")
    elif ttls[i] == 255 or ttls[i] == 254:
        OS.append("IOS 12.4")

print('\nList of all the hosts and possible OS')
print('-------------------------------------')
for i in range(len(unique_ips)):
    print('{:15}  -  {}'.format(unique_ips[i], OS[i]))
    
print('\n')