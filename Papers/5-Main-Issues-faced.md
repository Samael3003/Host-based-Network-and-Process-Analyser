# MAIN ISSUES FACED :

**1.	SMTP and G Mail connection.**

So, due to few changes in Google’s Security Systems in recent Years, Google Introduced New Security Policies in May 2022. This led to clashes between mail transfer by using only our G-Mail and Google Password.
To overcome this issue, we created a Dummy Gmail Account, and created an Application Password inside it’s Google Security. We, then copied the same Password to the Python file: “App_password.py” and then fetched the password to it’s orignal phase. The new Python file was formed, solely for the Security purposes.

**2. Notifier.**

There were many options to choose the notifier option from the Python Libraries. But, we choose to go with the inbuilt Notifier.
For Simplicity of Notifications, we created the Notify.py file, and  added the Syntax for the Same.

**3. SMTP , EmailMessage , SSL libraries**
`
We select the Sender and the Reciever of the Mail in advance. We also add the ssl_default_context,  so that the mail passes securely throughout Internet. We also select that the message to be travelled through “smtp.gmail.com”  present at port no. (465).
 After this, we Notify th User about the Success of the Mail Transfer
