import socket, sys
from struct import *
def eth_addr (a) :
	b = ("%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5])))
	return b
#Comparing the src and destination with the default port for each application layer protocol
def isSrcDes(src, des, arg):
	if(arg == "http"):
		if(src == "80" or des == "80"):
			return True
	elif(arg == "telnet"):
		if(src == "23" or des == "23"):
			return True
	elif(arg == "ftp"):
		if(src == "21" or des == "21" or src == "20" or des == "20"):
			return True
	return False
	
#Checking whether Ip is valid or not
def isIp(addr):
	try:
		n = addr.split(".")
		if(len(n) == 4):
			for i in n:
				if(int(i) <=0 and int(i) >= 255):
					return False
			return True
		return False
	except:
		return False

#Checking whether port is integer or not
def isPort(port):
	try:	
		if(type(int(port)) == type(10)):
			return True
	except:
		return False

#Checking whether name is from given application layer protocol name
def isName(name):
	l = ["http", "tcp", "udp", "telnet", "ftp"]
	for i in l:
		if(i == name):
			return True
	return False

#Returns the src and des port resp for TCP packet. 
def portTcp(iph_length, eth_length, packet):	
	t = iph_length + eth_length
	tcp_header = packet[t:t+20]
	tcph = unpack('!HHLLBBHHH' , tcp_header)			
	return tcph[0], tcph[1]

#Returns the src and des port resp for UDP packet.
def portUdp(iph_length, eth_length, packet):
	u = iph_length + eth_length
	udph_length = 8
	udp_header = packet[u:u+8]
	udph = unpack('!HHHH' , udp_header)			
	return udph[0], udph[1]
	
#Printing TCP packet data
def printTcp(iph_length, eth_length, packet):
	t = iph_length + eth_length
	tcp_header = packet[t:t+20]

	tcph = unpack('!HHLLBBHHH' , tcp_header)
			
	source_port = tcph[0]
	dest_port = tcph[1]
	sequence = tcph[2]
	acknowledgement = tcph[3]
	doff_reserved = tcph[4]
	tcph_length = doff_reserved >> 4
			
	print ('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))
			
	h_size = eth_length + iph_length + tcph_length * 4
	data_size = len(packet) - h_size
			
	data = packet[h_size:]
	count = 0
	print("Data:")
	print("------------------------------------------------------------------------------------------------------")
	t = 0
	for i in data:
		if(chr(i).isprintable()):
			print(chr(i), end="")
		else:
			print(".", end="")
		if(count == 35):
			print("                                     ", end=" ")
			for j in range(count):
				print(hex(data[t]).rstrip("L").lstrip("0x"), end=" ")
				t+=1		 
			count = 0
			print()
		else:
			count+=1
	print("                                     ", end=" ")
	for k in range(36-count):
		print("", end=" ")
	for j in range(count):
		print(hex(data[t]).rstrip("L").lstrip("0x"), end=" ")
		t+=1
	print("\n------------------------------------------------------------------------------------------------------")
	#for i in data:
	#	print(hex(i).rstrip("L").lstrip("0x"), end=" ")

#Printing UDP packet data
def printUdp(iph_length, eth_length, packet):
	u = iph_length + eth_length
	udph_length = 8
	udp_header = packet[u:u+8]

	udph = unpack('!HHHH' , udp_header)
			
	source_port = udph[0]
	dest_port = udph[1]
	length = udph[2]
	checksum = udph[3]
			
	print ('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + 
				' Length : ' + str(length) + ' Checksum : ' + str(checksum))
			
	h_size = eth_length + iph_length + udph_length
	data_size = len(packet) - h_size
			
	data = packet[h_size:]
	count = 0
	print("Data:")
	print("------------------------------------------------------------------------------------------------------")
	t = 0
	for i in data:
		if(chr(i).isprintable()):
			print(chr(i), end="")
		else:
			print(".", end="")
		if(count == 35):
			print("                                     ", end=" ")
			for j in range(count):
				print(hex(data[t]).rstrip("L").lstrip("0x"), end=" ")
				t+=1		 
			count = 0
			print()
		else:
			count+=1
	print("                                     ", end=" ")
	for k in range(36-count):
		print("", end=" ")
	for j in range(count):
		print(hex(data[t]).rstrip("L").lstrip("0x"), end=" ")
		t+=1
	print("\n------------------------------------------------------------------------------------------------------")
	#for i in data:
	#	print(hex(i).rstrip("L").lstrip("0x"), end=" ")
	#print ('Data : ' + str(data))

try:
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except(socket.error, msg):
	print ('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()

while True:
	packet = s.recvfrom(65565)
	
	packet = packet[0]
	
	eth_length = 14
	
	eth_header = packet[:eth_length]
	eth = unpack('!6s6sH' , eth_header)
	eth_protocol = socket.ntohs(eth[2])

	if eth_protocol == 8 :
		ip_header = packet[eth_length:20+eth_length]
		iph = unpack('!BBHHHBBH4s4s' , ip_header)

		version_ihl = iph[0]
		version = version_ihl >> 4
		ihl = version_ihl & 0xF

		iph_length = ihl * 4

		ttl = iph[5]
		protocol = iph[6]
		s_addr = socket.inet_ntoa(iph[8])
		d_addr = socket.inet_ntoa(iph[9])
		#print_flag = 1-> TCP packet, print_flag = 2-> UDP packet  
		print_flag = 0


		#TCP protocol
		if(protocol == 6):
			src_port, des_port = portTcp(iph_length, eth_length, packet)
			src_port, des_port = str(src_port), str(des_port)
			try:
				if(len(sys.argv) == 1):
					print_flag = 1
				elif(len(sys.argv) == 2 and isIp(sys.argv[1]) and sys.argv[1] == str(d_addr)):
					print_flag = 1
				elif(len(sys.argv) == 2 and isPort(sys.argv[1]) and sys.argv[1] == str(des_port)):
					print_flag = 1
				elif(len(sys.argv) == 2 and sys.argv[1] == "tcp"):
					print_flag = 1
				elif(len(sys.argv) == 2 and isName(sys.argv[1]) and isSrcDes(src_port, des_port, sys.argv[1])):
					print_flag = 1
				elif(len(sys.argv) == 2 and not isIp(sys.argv[1]) and not isPort(sys.argv[1]) and not isName(sys.argv[1])):
					print("Invalid Input!!!")
					print("Enter valid Ip, port or protocol name")
					break
				elif(len(sys.argv) == 3 and isIp(sys.argv[1]) and isPort(sys.argv[2]) and sys.argv[2] == str(des_port) and sys.argv[1] == str(d_addr)):
					print_flag = 1
				elif(len(sys.argv) == 3 and isIp(sys.argv[1]) and isName(sys.argv[2]) and sys.argv[2] == "tcp" and sys.argv[1] == str(d_addr)):
					print_flag = 1
				elif(len(sys.argv) == 3 and isPort(sys.argv[1]) and isName(sys.argv[2]) and sys.argv[2] == "tcp" and sys.argv[1] == str(des_port)):
					print_flag = 1	
				elif(len(sys.argv) == 3 and isIp(sys.argv[1]) and isName(sys.argv[2]) and isSrcDes(src_port, des_port, sys.argv[2]) and sys.argv[1] == str(d_addr)):
					print_flag = 1	
				elif(len(sys.argv) == 3 and isPort(sys.argv[1]) and isName(sys.argv[2]) and isSrcDes(src_port, des_port, sys.argv[2]) and sys.argv[1] == str(des_port)):
					print_flag = 1
				elif(len(sys.argv) == 3 and  ((not isPort(sys.argv[1]) and not isIp(sys.argv[1])) or (not isPort(sys.argv[2]) and not isName(sys.argv[2])))):
					print("Invalid Input!!!")
					print("First argument: valid Ip or Port\nSecond argument: valid Port or protocol Name")
					break	
				elif(len(sys.argv) == 4 and isIp(sys.argv[1]) and isPort(sys.argv[2]) and isName(sys.argv[3]) and sys.argv[3] == "tcp" and sys.argv[1] == str(d_addr) and sys.argv[2] == str(des_port)):
					print_flag = 1
				elif(len(sys.argv) == 4 and isIp(sys.argv[1]) and isPort(sys.argv[2]) and isName(sys.argv[3]) and sys.argv[1] == str(d_addr) and sys.argv[2] == str(des_port) and isSrcDes(src_port, des_port, sys.argv[3])):
					print_flag = 1
				elif(len(sys.argv) == 4 and (not isIp(sys.argv[1]) or not isPort(sys.argv[2]) or not isName(sys.argv[3]))):
					print("Invalid Input!!!")
					print("First argument: valid Ip\nSecond argument: valid Port\nThird argument: valid protocol Name")
					break
			except:
				print_flag = 0
		#UDP packets
		elif protocol == 17:
			src_port, des_port = portUdp(iph_length, eth_length, packet)
			src_port, des_port = str(src_port), str(des_port)
			try:
				if(len(sys.argv) == 1):
					print_flag = 1
				elif(len(sys.argv) == 2 and isIp(sys.argv[1]) and sys.argv[1] == str(d_addr)):
					print_flag = 2
				elif(len(sys.argv) == 2 and isPort(sys.argv[1]) and sys.argv[1] == str(des_port)):
					print_flag = 2
				elif(len(sys.argv) == 2 and sys.argv[1] == "udp"):
					print_flag = 2
				elif(len(sys.argv) == 2 and not isIp(sys.argv[1]) and not isPort(sys.argv[1]) and not isName(sys.argv[1])):
					print("Invalid Input!!!")
					print("Enter valid Ip, port or protocol name")
					break
				elif(len(sys.argv) == 3 and isIp(sys.argv[1]) and isPort(sys.argv[2]) and sys.argv[2] == str(des_port) and sys.argv[1] == str(d_addr)):
					print_flag = 1
				elif(len(sys.argv) == 3 and isIp(sys.argv[1]) and isName(sys.argv[2]) and sys.argv[2] == "udp" and sys.argv[1] == str(d_addr)):
					print_flag = 2
				elif(len(sys.argv) == 3 and isPort(sys.argv[1]) and isName(sys.argv[2]) and sys.argv[2] == "udp" and sys.argv[1] == str(des_port)):
					print_flag = 2
				elif(len(sys.argv) == 3 and  ((not isPort(sys.argv[1]) and not isIp(sys.argv[1])) or (not isPort(sys.argv[2]) and not isName(sys.argv[2])))):
					print("Invalid Input!!!")
					print("First argument: valid Ip or Port\nSecond argument: valid Port or protocol Name")
					break
				elif(len(sys.argv) == 4 and isIp(sys.argv[1]) and isPort(sys.argv[2]) and isName(sys.argv[3]) and sys.argv[3] == "udp" and sys.argv[1] == str(d_addr) and sys.argv[2] == str(des_port)):
					print_flag = 2
				elif(len(sys.argv) == 4 and (not isIp(sys.argv[1]) or not isPort(sys.argv[2]) or not isName(sys.argv[3]))):
					print("Invalid Input!!!")
					print("First argument: valid Ip\nSecond argument: valid Port\nThird argument: valid protocol Name")
					break
			except:
				print_flag = 0
		
		if(print_flag == 1):
			print ('Destination MAC : ' + str(eth_addr(str(packet[0:6]))) + ' Source MAC : ' + 
						str(eth_addr(str(packet[6:12]))) + ' Protocol : ' + str(eth_protocol))
			print ('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + 
						' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
			printTcp(iph_length, eth_length, packet)
		elif(print_flag == 2):
			print ('Destination MAC : ' + str(eth_addr(str(packet[0:6]))) + ' Source MAC : ' + 
						str(eth_addr(str(packet[6:12]))) + ' Protocol : ' + str(eth_protocol))
			print ('Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + 
						' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
			printUdp(iph_length, eth_length, packet)
