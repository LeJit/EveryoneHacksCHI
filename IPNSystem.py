from imapclient import IMAPClient
import datetime
import MySQLdb as MySQLdb

con = mdb.connect("hostname","username","password","database")

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

def enterIntoDatabase(database_info,data_dict):
	with con:
		cur = con.cursor()
		cur.execute("SET NAMES utf-8")
		cur.execute("SET CHARACTER SET utf-8")
		cur.execute("SET character_set_connection=utf-8")
		state = data_dict["State"]
		county = data_dict["City/County"]
		disaster = data_dict["Disaster"]
		location = data_dict["Location"]
		description = data_dict["Description"]
		time = data_dict["Time"]

		query = "INSERT INTO %s(STATE,COUNTY,DISASTER,LOCATION,DESCRIPTION,TIME) VALUES(%s,%s,%s,%s,%s,%s)" %(database_info,state,county,disaster,location,description,time)
		try:
			cur.execute(query)
		except mdb.IntegrityError:
			pass
		cur.close()
	con.commit()


def retrieveDatabaseValue(database_info,field, condition_field, condition):
	with con:
		cur = con.cursor()
		cur.execute("SET NAMES utf-8")
		cur.execute("SET CHARACTER SET utf-8")
		cur.execute("SET character_set_connection=utf-8")

		query = "SELECT %s from %s WHERE %s=%s" % (field,database_info,condition_field,condition)
 
def updateDatabaseValue(database_info,field, new_Value, condition_field, condition):
	with con:
		cur = con.cursor()
		cur.execute("SET NAMES utf-8")
		cur.execute("SET CHARACTER SET utf-8")
		cur.execute("SET character_set_connection=utf-8")


def findUpdates(data_dict):
	description = data_dict['Description']
	if description.startswith("U/D: Corr")
		if description.__contains__("address"):
			updateDatabase(db_info,"Location",data_dict["Location"])
		else:
			updateDatabase(db_info,"Disaster",data_dict["Disaster"])


