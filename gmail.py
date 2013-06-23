
import poplib
import datetime

mailServer = 'pop.gmail.com'
emailID = 'redcrossincident@gmail.com'
emailPass = 'redcross123'

def correctTime(email_time):
	first_semicolon = email_time.find(":")-2
	hour_time = int(email_time[first_semicolon:first_semicolon+2])
	correct_time = str((hour_time + 2)%24)
	return email_time[:first_semicolon]+correct_time+email_time[first_semicolon+2:-12]


## open connection to mail server (Secured using SSL)
myEmailConnection = poplib.POP3_SSL(mailServer)
## print the response message from server
#print myEmailConnection.getwelcome()
## set email address
myEmailConnection.user(emailID)
## set password 
myEmailConnection.pass_(emailPass)
## get information about the email address
EmailInformation = myEmailConnection.stat()
 
## Read all emails
numberOfMails = EmailInformation[0]
for i in range(numberOfMails):
	email = myEmailConnection.retr(i+1)[1]
	email_body = email[-4]
	email_body = email_body[8:].strip()
	email_time = email[4].strip()
	email_time = correctTime(email_time)
	file_output = email_body + " | " + email_time 
	print file_output