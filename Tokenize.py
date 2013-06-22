from pattern.en import *
#from sklearn.feature_extraction.text import TfidfVectorizer
from alchemy import Alchemy 

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

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

def writeOutput(filename, nouns, entities):
	f = open(filename,"w+")
	for noun in nouns:
		if entities.has_key(noun):
			f.write(noun+", "+entities[noun]+"\n")
		else:
			f.write(noun+", Unknown\n")
	f.close()

def main():
	text = "There is a fire on 1444 N Bosworth Avenue. I can hear a crying baby inside. His name is Deckard Cain"
	nouns = []
	s = parsetree(text)
	for sentence in s:
		chunks = sentence.chunks
		for chunk in chunks:
			tag, string = chunk.tag, chunk.string
			if tag == "NP":
				no_adjective_string = removeAdjective(chunk)
				nouns.append(no_adjective_string) 
	nouns = [formatString(string) for string in nouns]
	nouns = [string for string in nouns if len(string) > 0]
	entities = findEntities(text)
	writeOutput("firstTest.txt",nouns, entities)
	

if __name__ == '__main__':
	main()


