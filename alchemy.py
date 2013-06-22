import urllib, urllib2
import json
import os

#Wrapper class for AlchemyAPI
class Alchemy(object):

	#Initializes the Alchemy object with AlchemyAPI key
	def __init__(self,apikey):
		self.apikey = apikey
		self.params = {'apikey':apikey,'outputMode':'json'}

	#Set the text input for the Alchemy object
	def setText(self, tweet):
		if isinstance(tweet,str):
			self.params['text'] = tweet
		elif isinstance(tweet,list):
			self.params['text'] = "\n ".join(tweet)

	#Retrieves entity relations in stored text - WORKS
	def getRelations(self):
		baseURL = "http://access.alchemyapi.com/calls/text/TextGetRelations?"
		response = urllib.urlopen(baseURL+urllib.urlencode(self.params))
		results = json.loads(response.read())
		relations = results['relations']
		return relations

	#Retrieves entities in stored text - WORKS
	def getEntities(self):
		baseURL = "http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities?"
		response = urllib.urlopen(baseURL+urllib.urlencode(self.params))
		results = json.loads(response.read())
		entities = results['entities']
		return entities

	#Retrieve keywords in text - WORKS
	def getKeywords(self):
		baseURL = "http://access.alchemyapi.com/calls/text/TextGetRankedKeywords?"
		response = urllib.urlopen(baseURL+urllib.urlencode(self.params))
		results = json.loads(response.read())
		keywords = results['keywords']
		return keywords

	def getConcepts(self):
		baseURL = "http://access.alchemyapi.com/calls/text/TextGetRankedConcepts?"
		response = urllib.urlopen(baseURL+urllib.urlencode(self.params))
		results = json.loads(response.read())
		concepts = results['concepts']
		return concepts
