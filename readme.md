# Hello Friend. 🤓

Today what happened with me was truly unbelieveable. I was programming my **EDI Project**. 
The thing is, I have never been able to sit and program for more than 15-20 minuits.
But, today was different. I have surpassed all my previous limits and continuously programmed for a total of 5:43 hrs.
Well, it was not all programming, obviously. I had to refer various sources on Internet to read the Documentationa and stuff.

I had one eye on the Python Documentation and other articles. My browser tab was completely filled with multiple tabs I had opened. Moreover, I even had multiple videos playing at the same time. Usually, I hate multi-tasking, but Today, it seems, I had forgot my idealism. The other side of my Desktop was pinned to my Text-Editor. I prefer "GNU-NANO" over any other code-editors. 

Overall, the Project was a SUCCESS. PLease visit my Project.

## > My EDI Project. : )   ___ _Phase-I_ 💻

So, my friend, let me explain my Project and steps I took to accompalish it until its' completion.

First-of-all, I have prepared a Server-Client Interface in my "FEATHERS", that is my Laptop. The "Server" here, is an ideal server in listening mode.
The Client, on other hand is in Active mode. The Client is made to throw three files to the Server. To note here, is that both CLIENT and the SERVER are supposed to be on same IP-address and Port (here,- localhost 4444)

Run the Following commands:
    
        python3 SERVER.PY localhost 4444
        or
        ./SERVER.PY 127.0.0.1 1221
        
        python3 CLIENT.PY localhost 4444
        or
        ./CLIENT.PY 127.0.0.1 1221

Now, the client throws the Information of three different sources. - 

  1.) System Information.
  2.) Process Information.
  3.) Network Information.
    
Now, the Server accepts the request and packs up the information in three files, named upon the port numbers.
The difference between the byte-transfer can tell us the information passed from certain port.
The server then names the packed information with the lable of ***.xyz***. The thing to note here is that the file is not in readable format.
So, we use the program **ANALYSER.PY** to convert it into some readable format and with ***.csv*** extension, so we get the Tabular form.

Run the command: 
        
        python3 ANALYSER.PY
        or
        ./ANALYSER.PY

SO, we now we get 3 files namely- **Sysinfo.csv, Procinfo.csv, Netinfo.csv**. Out of these,:
    
> The **Sysinfo.csv** provides the information about all the System Configuration, like the _cpu architecture_, _ram present_, _Operationg System_, _Kernel Information_, etc.

.

> The **Procinfo.csv** provides the information about the _ProcessID_, _Process-Name_, _Process Status_. 

.

> The **Netinfo.csv** provides the information about the _ProcessID_, _Local IP & Port_, _Remote IP & Port_.


## Revison (Phase-1) 🔖

So, recap: 

Firstly, we started a connection between Client and Server. From this connection, we produced three files, regarding System Information, Process Information, Network Information. After this process, we used my Python Script-- ANALYSER.py to convert all these random files to a readable format --(.csv). Now, we could distinguish between the parameters present in all these files. The Syatem info. file provides the information regarding the System Configuration. The Process Info. provides the information regarding the Processes happening within the system, it gives us the Process IDs, with respective Process Names and Process Status. Atlast, The Network Info. gives us the info abou the Processes, requireing Network connectivity. It shows the ProcessIDs along with their Network Status, Local IP&Ports and Remote IP&Ports.


## > My EDI Project. : )   ___ _Phase-II_ 💻

Now, for Phase II, we have three outputs. First, we have to creatte a text file out of the querry, having all the parameters from .csv file, combined over to single file. Second, we have to notify about the creation of the file with the **NOTIFICATION** over the Desktop. Third, we have to **E-MAIL** the completion of the progress to the User's account along with the location of the file and the Query address.

For the provided outcomes, we have prepared to categorise into 4 processes:

1.) searchbyPROCESSID:
        
> Since the Tab of Process IP is present in Netinfo.csv and Procinfo.csv, we take both files as the input, and find the required ProcessId asked by the User. If present, we append the complete row about the UserQuery into the PID.txt. On completion of this task, we send the Notification on the Desktop and Email to the User account.

2.) searchbyLOCALIP:
        
> Now, the Tab of Local IP tab is only available in the Netinfo.csv. So, we consider only this file as the Input. We then proceed to find the UserQuerry in the LocalIP tab. If Present, (say 0.0.0.0), we append the complete row about the Query into the LIP.txt file inside the same Directory.

3.) searchbyPROCESSNAME:
        
> Now, the Tab of ProcessName tab is only available in the Procinfo.csv. So, we consider only this file as the Input. We then proceed to find the UserQuerry in the PROCESSNAME tab. If Present, (say python3, or zsh), we append the complete row about the Query into the P-Name.txt file inside the same Directory.

4.) searchbyNETWORKSTATUS:
    
> Now, the Tab of NetworkSTATUS tab is only available in the Netinfo.csv. So, we consider only this file as the Input. We then proceed to find the UserQuerry in the NETSTAUS tab. If Present, (say ESTABLISHED or IDLE or CLOSED), we append the complete row about the Query into the NET-STATUS.txt file inside the same Directory.
        
The user is notifies about the Progress as:

1.) Through Notification:

            The (User Query)(User Choice) is stored in (UserChoice).txt")  >

2.) Through E-mail:

   > Sender: raystrahl30032003@gmail.com
   > Reciever: (TheUser@example.xyz)

Subject:

        * Security Mail:
body:

        The Query " (User Query) " as the "(User Choice)" been asked has been processed. The detailed information is available at the following address : "(Directory-to-be-stored-in)/(UserChoice).txt". 

        Please visit the ".txt" file for more information. 

        Thank You and have a Good Day.'''

## Backend of my _PHASE-II_ 🎱

For Notify:

- I had created new **python library "Notify.py"** so as to simplify the matters regarding Notifications. Then I impored it as a library, and sent notification.
    
For Email:

- FOr Email, I had to do a lot of research, since Google had banned the **Less Secure App Permissions** during MAY'2022. So, I created **App-Password** from Security Tab. I, then saved the password in another **python library: "password.py"** and then imported it as the email password. 
- Moreover, I also imported modules: **ssl** and **smtplib**. The **ssl** module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption and peer authentication facilities for network sockets. The **smtplib** module  was used, as it defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP listener daemon. In this session, the reciever was "smtp.gmail.com" with port "465" (the default port "587" was not working.)
