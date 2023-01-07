#!/usr/bin/env python3

import os
import platform
import sys
import socket
import selectors
import types
import psutil
import re
import uuid

print ("Usrnam:")
username = input()
if username == "123":
	print ('Hello'+username+'entr passwrd')
	password= input()
	if username == '123' and password == '123':
		print ('ACCESS GRANTED')

sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message2 from client.", b"message3."]
mySysOS = "NIL"
# globalmyMessages
# myMessages = [b".", b".", b"."]

def getProcess():
	output = "PROCESSID,PROCESSNAME,STATUS,STARTTIME\n"
	for proc in psutil.process_iter():
		try:
		#Get process Name & PID from process object.
			#print(proc)
			#print(str(proc.pid), ",", str(proc.name()), .....
			#output += str(proc.pid) + "," + str(proc.name()) + .....
			output += str(proc.pid) + "," + str(proc.name()) + "," + str(proc.status()) + "," + str(proc.create_time()) + "\n"
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return output

def getConnection():
	output = "PROCESSID,STATUS,LOCALIP,LOCALPORT,REMOTEIP,REMOTEPORT\n"
	for cons in psutil.net_connections(kind='inet'):
		try:
		#Get process name & pid from process Object.
			#print ()proc
			#print(str(cons.pid)), ",", str(cons.laddr.in), ",", str(cons.laddr.port), str(cons.raddr).replace("()",",,")
			#output += str(proc.pid), proc.name(), ....
			output += str(cons.pid) + "," +str(cons.status) + "," + str(cons.laddr.ip) + "," + str(cons.laddr.port) + "," +  ( (str(cons.raddr).replace("()",",,")).replace("()",",,")) + "\n"
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return output

def getSystem():
	output = "NAME,DETAILS\n"
	output += "platform," + str(platform.system()) + "\n"
	output += "platform-release," + platform.release() + "\n"
	output += "platform-version," + platform.version() + "\n"
	output += "architecture," + platform.machine() + "\n"
	output += "hostname," + socket.gethostname() + "\n"
	output += "ip-address," + socket.gethostbyname(socket.gethostname()) + "\n"
	output += "mac-address," + ':'.join(re.findall('..', '%012x' % uuid.getnode())) + "\n"
			
	output += "processor," + (platform.processor()).replace(","," ") + "\n"		
	output += "ram,"+ str(round(psutil.virtual_memory().total / (1024.0 **3))) + "\n"		
	return output
	
def getWinSystem():
	#output = os.popen('wmic computersystem list Name, UserName ... ')	
	output = os.popen('wmic computersystem list full /format:Textvaluelist').read()
	# print(output)
	return output		
	
def getWinProcess():
	output = os.popen('wmic process get description, processid /format:csv').read()
	# print(output)
	return output			
			
def getWinConnection():
	output = os.popen('netstat -an').read()
	# print(output)
	return output				
			
def os_info():
	return platform.system()			
			
def cpu_info():
	if platform.system() == 'Windows':
		return platform.processor()
	elif platform.system() == 'Darwin':
		command = '/usr/sbin/sysctl -n machdep.cpu.brand_string'			
		return os.popen(command).read().strip()
	elif platform.system() == 'Linux':
		command = 'cat /proc/cpuinfo'			
		return os.popen(command).read().strip() 	
	return 'platform not identified'		
			
			
def start_connections(host, port, num_conns, sysData):
	server_addr = (host, port)
	for i in range (0, num_conns):
		connid = i + 1 			
		print ("starting Connection", connid, "to", server_addr)	
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setblocking(False)
		sock.connect_ex(server_addr)
		events = selectors.EVENT_READ | selectors.EVENT_WRITE
		data = types.SimpleNamespace(
			connid=connid,
			msg_total=sum(len(m) for m in sysData),
			recv_total=0,
			messages=list(sysData),
			outb=b"",
		)
		sel.register(sock, events, data=data)


def service_connection(key, mask):
	sock = key.fileobj
	data = key.data
	if mask & selectors.EVENT_READ:
		recv_data = sock.recv(10240)    # Should be ready to read
		if recv_data:
			print("SERVER Recieved [", sys.getsizeof(repr(recv_data)), "] Bytes For Connection ", data.connid)
			data.recv_total += len(recv_data)
		if not recv_data or data.recv_total == data.msg_total:
			print("closing Connection", data.connid)
			sel.unregister(sock)
			sock.close()
	if mask & selectors.EVENT_WRITE:
		if not data.outb and data.messages:
			data.outb = data.messages.pop(0)
		if data.outb:
			print ("sending", sys.getsizeof(repr(data.outb)), " bytes to connection", data.connid)
			sent = sock.send(data.outb) # Should be ready to write
			data.outb = data.outb[sent:]


if len(sys.argv) !=3:
	print("usage:", sys.argv[0], "<host> <port> ")
	sys.exit(1)

host, port = sys.argv[1:3]
host = socket.gethostbyname(host)
hostname = socket.gethostname()
myMessages=[ ("SYSINFO,"+hostname+","+str(host)+","+str(port)+"~`~`~`~`~`\n").encode(), (getSystem()).encode()]
start_connections(host, int(port), 1, myMessages)
myMessages=[ ("PROINFO,"+hostname+","+str(host)+","+str(port)+"~`~`~`~`~`\n").encode(), (getProcess()).encode()]
start_connections(host, int(port), 1, myMessages)
myMessages=[ ("NETINFO,"+hostname+","+str(host)+","+str(port)+"~`~`~`~`~`\n").encode(), (getConnection()).encode()]
start_connections(host, int(port), 1, myMessages)


print(cpu_info())

try:
	while True:
		events = sel.select(timeout=1)
		if events:
			for key, mask in events:
				service_connection(key, mask)
		# Check for a socket being monitored to Continue
		if not sel.get_map():
			break
except KeyboardInterrupt:
	print("caught keyboard interrupt, exiting")
finally:
	sel.close()















































			
