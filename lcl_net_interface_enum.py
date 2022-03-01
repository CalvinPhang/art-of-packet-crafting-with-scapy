import netifaces as ni
import winreg as wr
from pprint import pprint

def get_connection_name_from_guid(iface_guids):
    iface_names = ['(unknown)' for i in range(len(iface_guids))]
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in range(len(iface_guids)):
        try:
            reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
            iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
        except FileNotFoundError:
            pass
    return iface_names



ifaces = ni.interfaces()
ifaces_guid = get_connection_name_from_guid(ifaces)

for i in range(len(ifaces)):
    if 2 in ni.ifaddresses(ifaces[i]):
        ifaces_details = ni.ifaddresses(ifaces[i])[2][0]
        if ifaces_details['addr'] == '127.0.0.1':
            print('Localhost Network')
        else:    
            print(ifaces_guid[i])
        print(f"IP Address: {ifaces_details['addr']}")
        print(f"Netmask   : {ifaces_details['netmask']}")
        if i != 'lo':
            print(f"Broadcast : {ifaces_details['broadcast']}")
        for j in ni.gateways()[2]:
            if j[1] == i:
                print(f"Gateway   : {j[0]}")
        print('\n')





