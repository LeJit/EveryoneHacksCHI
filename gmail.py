
import poplib
import datetime

## print the response message from server
#print myEmailConnection.getwelcome()

def correctTime(email_time):
	first_semicolon = email_time.find(":")-2
	hour_time = int(email_time[first_semicolon:first_semicolon+2])
	correct_time = str((hour_time + 2)%24)
	return email_time[:first_semicolon]+correct_time+email_time[first_semicolon+2:-12]

class Gmail():

	def __init__(self,mailServer = 'pop.gmail.com' ,emailID = 'redcrossincident@gmail.com',emailPass = 'redcross123'):
		self.mailServer = mailServer
		self.emailID = emailID
		self.emailPass = emailPass
		## open connection to mail server (Secured using SSL)
		self.myEmailConnection = poplib.POP3_SSL(self.mailServer)
		## set email address
		self.myEmailConnection.user(self.emailID)
		## set password 
		self.myEmailConnection.pass_(self.emailPass)
		## get information about the email address
		self.EmailInformation = self.myEmailConnection.stat()

	def correctTime(self,email_time):
		first_semicolon = email_time.find(":")-2
		hour_time = int(email_time[first_semicolon:first_semicolon+2])
		correct_time = str((hour_time + 2)%24)
		return email_time[:first_semicolon]+correct_time+email_time[first_semicolon+2:-12]

	## Read all emails
	def readEmails(self, includeTime):
		numberOfMails = self.EmailInformation[0]
		messageHolders = []
		for i in range(numberOfMails):
			email = self.myEmailConnection.retr(i+1)[1]
			email_body = email[-4]
			email_body = email_body[8:].strip()
			email_time = email[4].strip()
			email_time = correctTime(email_time)
			file_output = email_body
			if includeTime:
			 	file_output = file_output+ " | " + email_time 
			messageHolders.append(file_output)
		return messageHolders