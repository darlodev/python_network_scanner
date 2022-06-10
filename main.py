from scapy.all import ARP, Ether, srp

print("Welcome to PNS (Python Network Scanner).\n")

print("Please input an IP Address and Range:\n")
target_ip = input()
#TODO create conditional logic.

arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:\n")
print("IP" + " " * 18 + "MAC")

for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))