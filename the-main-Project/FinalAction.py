#!/usr/bin/env python

import csv
import gi
import os

import notify
from email.message import EmailMessage
import ssl
import smtplib
from app_password import password




if os.path.isfile("/home/samael/EDI Project/MY HOST intru-detec/PID.txt"):
    os.remove("/home/samael/EDI Project/MY HOST intru-detec/PID.txt")
if os.path.isfile("/home/samael/EDI Project/MY HOST intru-detec/P-NAME.txt"):
    os.remove("/home/samael/EDI Project/MY HOST intru-detec/P-NAME.txt")
if os.path.isfile("/home/samael/EDI Project/MY HOST intru-detec/LOCAL-IP.txt"):
    os.remove("/home/samael/EDI Project/MY HOST intru-detec/LOCAL-IP.txt")
if os.path.isfile("/home/samael/EDI Project/MY HOST intru-detec/NET-STATUS.txt"):
    os.remove("/home/samael/EDI Project/MY HOST intru-detec/NET-STATUS.txt")



def searchbyPROCESSID():
	csv_file1=csv.reader(open('NETINFO-2022-11-13-samael-feather-b-127.0.0.1-55476.csv','r'))
	csv_file2=csv.reader(open('PROINFO-2022-11-13-samael-feather-b-127.0.0.1-55460.csv','r'))
	PROCESSID=input('Enter PID name: ')

	
	for row in csv_file2:
		if PROCESSID==row[0]:
			v=open("PID.txt",'a')
			print(row,file=v)
			v.close()
			
	for row in csv_file1:
		if PROCESSID==row[0]:
			x=open("PID.txt",'a')
			print(row,file=x)
			x.close()		
	
	notify.notify("The "+ PROCESSID + " P-ID is stored in PID.txt")	
	email_sender = 'raystrahl30032003@gmail.com'
	email_password = password
	email_reciever = 'narutouzumaki30032003@gmail.com'
	subject = '* Security Mail:'
	body = '''The Query "''' +PROCESSID+ '''" as the "PROCESS-ID" been asked has been processed. The detailed information is available at the following address : "/home/samael/EDI Project/MY HOST intru-detec/PID.txt". 

	['45729', 'qemu-system-x86_64']
	
Please visit the ".txt" file for more information. 

Thank You and have a Good Day.

''' 
	
	e_m=EmailMessage()
	e_m['From'] = email_sender
	e_m['To'] = email_reciever
	e_m['subject'] = subject
	e_m.set_content(body)


	context = ssl.create_default_context()
	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(email_sender, password)
		smtp.sendmail(email_sender, email_reciever, e_m.as_string())
	print('\n\n\t\tMail Sent...')
	notify.notify("The mail has been SENT...")
				

def searchbyLOCALIP():
	csv_file=csv.reader(open('NETINFO-2022-11-13-samael-feather-b-127.0.0.1-55476.csv','r'))
	LOCALIP=str(input('Enter IP to show data: '))

	for row in csv_file:
		if LOCALIP in row[2]:
			y=open("LIP.txt",'a')
			print(row,file=y)
			y.close()
	notify.notify("The "+ LOCALIP + " L.IP is stored in LIP.txt")		

	email_sender = 'raystrahl30032003@gmail.com'
	email_password = password
	email_reciever = 'narutouzumaki30032003@gmail.com'
	subject = '* Security Mail:'
	body = '''The Query "''' +LOCALIP+ '''" as the "Local IP-address" been asked has been processed. The detailed information is available at the following address : "/home/samael/EDI Project/MY HOST intru-detec/LIP.txt". 
	
Please visit the ".txt" file for more information. 

Thank You and have a Good Day.'''

	e_m=EmailMessage()
	e_m['From'] = email_sender
	e_m['To'] = email_reciever
	e_m['subject'] = subject
	e_m.set_content(body)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(email_sender, password)
		smtp.sendmail(email_sender, email_reciever, e_m.as_string())
	print('\n\n\t\tMail Sent...')
	notify.notify("The mail has been SENT...")
			
			
def searchbyPROCESSNAME():
	csv_file=csv.reader(open('PROINFO-2022-11-13-samael-feather-b-127.0.0.1-55460.csv','r'))
	PROCESSNAME=input('Enter P-NAME name: ')

	for row in csv_file:
		if PROCESSNAME==row[1]:
			z=open("P-NAME.txt",'a')
			print(row,file=z)
			z.close()
	notify.notify("The "+ PROCESSNAME + " Process is stored in P-NAME.txt")			

	file = open("P-NAME.txt", "r")
	email_sender = 'raystrahl30032003@gmail.com'
	email_password = password
	email_reciever = 'narutouzumaki30032003@gmail.com'
	subject = '* Security Mail:'
	body = '''The Query "''' +PROCESSNAME+ ''' " as the "PROCESS-NAME" been asked has been processed. The detailed information is available at the following address : "/home/samael/EDI Project/MY HOST intru-detec/P-NAME.txt". 
	Please visit the ".txt" file for more information.\n\n\n[ProcessID,\tProc-Name,\tProc-Status,\tStartTime]'''+file.read()+'''\n\n\n\tThank You and have a Good Day.'''
	
	e_m=EmailMessage()
	e_m['From'] = email_sender
	e_m['To'] = email_reciever
	e_m['subject'] = subject
	e_m.set_content(body)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(email_sender, password)
		smtp.sendmail(email_sender, email_reciever, e_m.as_string())
	print('\n\n\t\tMail Sent...')
	notify.notify("The mail has been SENT...")



def searchbyNETSTATUS():
	csv_file=csv.reader(open('NETINFO-2022-11-13-samael-feather-b-127.0.0.1-55476.csv','r'))
	STATUS=str(input('Enter STATUS to show data: '))

	for row in csv_file:
		if STATUS in row[1]:
			u=open("NET-STATUS.txt",'a')
			print(row,file=u)
			u.close()			
	notify.notify("The "+ STATUS + " Status is stored in NET-STATUS.txt")			

	email_sender = 'raystrahl30032003@gmail.com'
	email_password = password
	email_reciever = 'narutouzumaki30032003@gmail.com'
	subject = '* Security Mail:'
	body = '''The Query "''' +STATUS+ '''" as the "Network Status" been asked has been processed. The detailed information is available at the following address : "/home/samael/EDI Project/MY HOST intru-detec/NET-STATUS.txt". 
	
Please visit the ".txt" file for more information. 

Thank You and have a Good Day.'''

	e_m=EmailMessage()
	e_m['From'] = email_sender
	e_m['To'] = email_reciever
	e_m['subject'] = subject
	e_m.set_content(body)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(email_sender, password)
		smtp.sendmail(email_sender, email_reciever, e_m.as_string())
	print('\n\n\t\tMail Sent...')
	notify.notify("The mail has been SENT...")


print ('''.
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝     
                                                                                        
███╗   ██╗███████╗████████╗   ███╗   ██╗      ██████╗ ██████╗  ██████╗  ██████╗         
████╗  ██║██╔════╝╚══██╔══╝   ████╗  ██║      ██╔══██╗██╔══██╗██╔═══██╗██╔════╝         
██╔██╗ ██║█████╗     ██║█████╗██╔██╗ ██║█████╗██████╔╝██████╔╝██║   ██║██║              
██║╚██╗██║██╔══╝     ██║╚════╝██║╚██╗██║╚════╝██╔═══╝ ██╔══██╗██║   ██║██║              
██║ ╚████║███████╗   ██║      ██║ ╚████║      ██║     ██║  ██║╚██████╔╝╚██████╗         
╚═╝  ╚═══╝╚══════╝   ╚═╝      ╚═╝  ╚═══╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝         
                                                                                        
 █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗                         
██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗                        
███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗█████╗  ██████╔╝                        
██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██╔══╝  ██╔══██╗                        
██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║███████╗██║  ██║                        
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝                        
                                                                                        ''')

print('\n\tEnter "1" to search by PID')
print('\n\tEnter "2" to search by Local-IP')
print('\n\tEnter "3" to search by P-NAME')
print('\n\tEnter "4" to search by NET-STATUS')

src=int(input('\n\n\t\tEnter here:.  '))

if src==1:
	searchbyPROCESSID()
elif src==2:
	searchbyLOCALIP()
elif src==3:
	searchbyPROCESSNAME()	
elif src==4:
	searchbyNETSTATUS()		
else:
	print('SorryInvalid input')
	print('Exiting...')
	
	
	
