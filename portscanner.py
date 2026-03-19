import  socket

def scan(target, ports):
	for port in range(1,ports):
		scan_port(target, port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		socket.connect((ipaddress, port))
		print("[+] Port Opende" + str(port))
	except:
		print("[-] Port Closed" + str(port))


targets = input("[*] Enter targets to scan (split them by ,) : ")
ports = input("[*] How many ports do you want to scan?: ")
if "," in targets:
	print("[*] scanning multiple targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.split(' '),ports)
else:
	can(targets, port);
scan(targets,ports)

