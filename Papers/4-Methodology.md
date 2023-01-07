# METHODOLOGY :

**This Project is successfully accompalished in Two different Stages :.** 

A. Communication of Client and Server over the same Network.

B.  Analyse the Outputs created by the First Stage, to provide the Analysis of the Query, and send Email to the User’s Address, besides notifying the System, using System Notifier.

## 1.	Creation of the Virtual Machines :
We created Two Virtual Machines. For the Creation of the Virtual Machines, we used QEMU VirtManager App inside our Linux WorkStation.
v	Server 1(Test-Parrot-1) :   Parrot OS , XFCE DesktopEnvironment  ,  25GB .qcow2 Storage  ,  2GB RAM ,  2 core CPU ,  192.168.122.222
v	Client 1(Test-Parrot) :   Parrot OS , MATE DesktopEnvironment  ,  25GB .qcow2 Storage  ,  2GB RAM ,  2 core CPU ,  192.168.122.21
v	Client 2(Samael-elementary) :  Elementary OS , Pantheon DesktopEnvironment  ,  25GB .qcow2 Storage  ,  2GB RAM ,  2 core CPU ,  192.168.122.250
Reason for creation of Virtual Machines : 
 * The Virtual Machines are typically a set of Softwares running to provide an User Experience of Running an Virtual Environment of a workstation inside owr own Work Station. We can run multiple Virtual Machines in the same Work Station. Each Virtual Machine will have it’s dedicated Storage, RAM, CPU and NIC (herein, GraphicsCard is not mandatory, but can be included). It can also have it’s own Network Settings, like the Virtual NAT(Network Address Translation), or Bridged Network Adaper. For our Project’s purpose, It also has the pre-identified IP (Internet Protocols) configured .It is due to all these reasons, that the Virtual Machines are treated as a Computational System inside another System. 
* Here, we have used Parrot OS and Elementary OS, for their minimal nature of Operating Systems, and higher Efficiency of the Battery Life, compared to the other Flavours of Linux Distributions, and the simplicity of use.
* We have recommended using Ubuntu based Distributions, for their simplicity in work environment. Moreover, Ubuntu based Distros provide Stability, compared to the Rolling Arch Linux based Distros, or More Secured Red Hat Enterprise Linux based Distros, or Higher Level Linux distros like Gentoo Linux or Void Linux.


## 2. Prerequisites of all Virtual Machines :
 * Install the required Linux Distribution over the Virtual Machine, using the (.iso) image file through SATA port ,ove the system having pre-defined RAM, CPU, Storage. The Calamares Installer will take the User through the process. The User, in theis case, simply has to follow the Instructions offered by the Installer.
 * After Installing the Operating System over the Virtual Machine Interface, remove the SATA Drive, or the (.iso) file from the System, and reboot the Virtual System. 
 * On rebooting, 
the user is required to update the Operating System. This can be done by :  
#sudo apt update && sudo apt upgrade
To check the Network configuration, install the package: “net-tools” and running the command “ifconfig” :  
 $ apt install net-tools
 # ifconfig
the user is required install “python3” to run the following Project in his/her machine and “pip” to install required Python files:
 $ apt install python3
  $ apt install pip 
the user is required to update the Operating System. This can be done by :  
 sudo apt update && sudo apt upgrade
## 3.  Running the Python Files to Establish the Connection.
 * For SERVER file, just run the following command :
  # python3 server.py <ip.addrs.SERVER> <port number>
  # python3  server.py  192.168.122.222  5421
  * For CLIENT file, just run the following command :
  # python3 client.py <ip.addrs.SERVER> <port number>
  # python3  client.py  192.168.122.222  5421
 Running these will establish the connection between the SERVER and the CLIENT.  The Server, here, is in the listening mode; so, it will accept all the data being sent from the Client. The Client, on the other Hand, will transfer all the System Information, Process Information, Network Information.
 When observed at the SERVER’s console, the Data Transferred will have the IP Address and the Port from which the Client had transferred the Data. The console will also show the bytes of Data transferred during the Communication Sequence. 
The  0th line specifies the normal amount of Data transferred during the Communication. 
The 1st line shows the Data transferred about the System’s Information. It has the Least Data Transfer.
The 2nd line represents the Data transferred about the Process’s Information. This has the maximum Data Transfer among all three, Since it consists of Processes running about inside the System.
The 3rd line represents the Data transferred about the Network Information. This has Data transfer less than Process Info, since all Networks are the part of Processes, eg Firefox, Youtube, Outlook, Emby Server; but, not all Processes might be Networks, like the Terminal, Gallery, VLC Player. 
All this information is stored in (.xyz) format, inside the File Syatem, further to be Analysed.

## 4. Analysing the Recieved Data :
 
 Just run the command : 
  #  python3  analyser.py

 This command will convert the created (.xyz) file into the (.csv ) file. The  (.csv) file is specially easy to read for the user, and comes handy in the Further Analysis. The (.csv) file will open  with Excel format, each element seperated with the ‘comma’ (‘,’).
The Sysinfo.csv provides the infoormation about the Computational System. It includes System’s Architecture, Kernel Module, Operating System, RAM and Storage.
The Procinfo.csv consists of the Process ID, it’s relative Process Name, the Process’s Status on the System (Sleep, Idle, Running) and the Start time of the System.
The Netinfo.csv consists of the Process ID, its Network Status (Sleep, Established, Closed), it’s Local IP and Port, and Remote IP and Port. This also shows the Connection ports of the CLIENT we had deployed.

##5. The Final Analysis :
To start the final Analysis, a Python Script has been Created :
 # python3  FinalAction.py
 #  ./FinalAction.py
Here, the User will be asked to choose one out of the Four Options :
a.	To search the Query by Process ID
b.	To search the Query by Local IP
c.	To search the Query by Process Name
d.	To search the Query by Network Status
For The First Option : PROCESS ID
We have seen, the Elements of Process ID is presemt in both the (.csv) files. — Procinfo and Netinfo.  So, it catches the Query in the 0th column in both the files, and Prints the entire Row. The appending occours in the “P.ID.txt” inside the File System. After completion of this process, the User recives Notification on the Work Station. The mail is Sent to the Host’s  E-mail address. The Host, later recieves the Notification regarding Sending of the Email on the Work Station.
For The Other Options : LOCAL IP, PROCESS NAME, NETWORK STATUS
We have seen, the Elements of LOCAL-IP and NET-STATUS is presemt in “Netinfo.csv”. Also, the PROCESS-NAME is present in “Procinfo.csv”.  So, it catches the Query in  the files, and Prints the entire Row. The appending occours in the “LIP.txt”, “P-Name.txt”, “Net-Status.txt”  inside the File System. 

After completion of this process, the User recives Notification on the Work Station. The mail is Sent to the Host’s  E-mail address, confirming the Querry and the Location of the Appended file in the File System. The Host, later recieves the Notification regarding Sending of the Email on the Work Station.

