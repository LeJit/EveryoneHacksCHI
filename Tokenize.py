from pattern.en import *
#from sklearn.feature_extraction.text import TfidfVectorizer
from alchemy import Alchemy 

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

common_disasters = ["Fire","Flood","Microburst","Tornado","Home Damage","Carbon Monoxide","Gas Leak","Car crash","Building collapse","Roof collapse","Brushfire","Hazmat","Plane Crash","Weather","Mass Care","Canteen"]
disaster_lexnames = ["noun.event","noun.act","noun.phenomenon"]
textfile_names = ["Disaster.txt","IncidentAddress.txt","ClientName.txt"]
textfile_names = ["/bootstrap/callData/"+filename for filename in textfile_names]
textfile_mappings = ["Disaster","Location","Person"]

def formatString(input):
	formatted = [w for w in input.split() if not w.lower() in stopwords]
	formatted = " ".join(formatted).upper()
	return formatted

def removeAdjective(chunk):
	output = ""
	words = chunk.words
	for word in words:
		if not word.tag == "JJ":
			output= output+word.string+" "
	return output

def findEntities(text):
	api_key = "7674818bdcdcb1249b599e2bf3699001ee957dbf"
	alchemist = Alchemy(api_key)

	alchemist.setText(text)
	entities = alchemist.getEntities()
	name_entities = {}
	for entity in entities:
		name, type_ent, relevance = entity['text'], entity['type'], entity['relevance']
		name_entities[name.upper()] = type_ent
	return name_entities

def isPerson(word):
	synset = wordnet.synsets(word)
	if len(synset) > 0:
		synset = synset[0]
		return synset.lexname == "noun.person"
	else:
		return False

def isDisaster(word):
	synset = wordnet.synsets(word)
	if len(synset) > 0:
		synset = synset[0]
		return disaster_lexnames.__contains__(synset.lexname)
	else:
		return False

def determineType(noun,sentence):
	if isDisaster(noun):
		return "Disaster"
	elif isPerson(noun):
		return "Person"
	elif findLocations(noun,sentence):
		return "Location"
	else:
		return "Unknown"

def writeOutput(filename, entities, value):
	f = open(filename,"w+")
	for noun,typing in entities.iteritems():
		if typing == value:
			f.write(noun)
	f.close()

def findLocations(noun,sentence):
	pnps = sentence.pnp
	for chunk in pnps:
		string = chunk.string.lower() 
		if string.__contains__(noun.lower()):
			return True
	return False 


def main():
	text = "There is a flood on 1444 N Bosworth Avenue. I can hear a crying baby inside. His name is Deckard Cain"
	entities = findEntities(text)
	s = parsetree(text)
	for sentence in s:
		chunks = sentence.chunks
		for chunk in chunks:
			tag, string = chunk.tag, chunk.string
			if tag == "NP":
				no_adjective_string = removeAdjective(chunk)
				no_adjective_string = formatString(no_adjective_string)
				if len(no_adjective_string) > 0:
					if not entities.has_key(no_adjective_string):
						entities[no_adjective_string] = determineType(no_adjective_string,sentence)
	for i,textfile in enumerate(textfile_names):
		value = textfile_mappings[i]
		writeOutput(textfile,entities,value)

if __name__ == '__main__':
	main()


