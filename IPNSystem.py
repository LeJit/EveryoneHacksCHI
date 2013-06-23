from gmail import Gmail
import datetime

def getEmails(username,password):
	HOST = "pod51009.outlook.com"
	email = Gmail(HOST,username,password)
	messages = email.readEmails(False)
	return messages

def extractInformation(ipn_input):
    labels = ["State","City/County","Disaster","Location","Description","Time"]
    entries = ipn_input.split("|")
    data_dict = {}
    for i,entry in enumerate(entries):
        data_dict[labels[i]] = entry.strip()
    data_dict["Date"] = datetime.datetime.now().strftime("%m-%d-%Y")
    return data_dict


def findUpdates(data_dict):
	description = data_dict['Description']
	if description.startswith("U/D: Corr")
		if description.__contains__("address"):
			updateDatabase(db_info,"Location",data_dict["Location"])
		else:
			updateDatabase(db_info,"Disaster",data_dict["Disaster"])

def main():
	allEmails = getEmails('username','password')
	for message in allEmails:
		information = extractInformation(message)
		print information
	

