from imapclient import IMAPClient
import datetime


def accessEmail(username,password):
	HOST = "pod51009.outlook.com"
	ssl = False
	server = IMAPClient(HOST, use_uid = True, ssl = False)
	server.login(username,password)

	select_info = server.select_folder("INBOX")



def extractInformation(ipn_input):
    labels = ["State","City/County","Disaster","Location","Description","Time"]
    entries = ipn_input.split("|")
    data_dict = {}
    for i,entry in enumerate(entries):
        data_dict[labels[i]] = entry.strip()
    data_dict["Date"] = datetime.datetime.now().strftime("%m-%d-%Y")
    return data_dict


def retrieveDatabaseValue(database_info,field):
	# get 

def updateDatabase(database_info,field, new_Value):



def findUpdates(data_dict):
	description = data_dict['Description']
	if description.startswith("U/D: Corr")
		if description.__contains__("address"):
			updateDatabase(db_info,"Location",data_dict["Location"])
		else:
			updateDatabase(db_info,"Disaster",data_dict["Disaster"])


