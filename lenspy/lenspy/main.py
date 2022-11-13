from GraphQLClient import client
from queries import *

def listtostr(l):
	s = '['
	for el in l:
		s += el + ','
	s = s[:-1] + ']'
	return s

client = client()

# sortcriteria = ['TOP_COMMENTED','TOP_COLLECTED','TOP_MIRRORED','LATEST','CURATED_PROFILES']
# publicationtypes = ['POST', 'COMMENT', 'MIRROR']
def explorepublications(sortCriteria,publicationTypes,limit):
	return ExplorePublications("sortCriteria:"+sortCriteria+",publicationTypes: "+listtostr(publicationTypes)+",limit: "+str(limit))

def searchprofiles(query,limit):
	return SearchProfiles("query:"+query+",limit: "+str(limit))

def searchpublications(query,limit):
	return SearchPublications("query:"+query+",limit: "+str(limit))

def allpublications(profileId,publicationTypes,limit):
	return publications("profileId:"+profileId+",publicationTypes: "+listtostr(publicationTypes)+",limit: "+str(limit))

def specificpublication(publicationId):
	return publication("publicationId:"+publicationId)

def executequery(func,args):
	x = client.execute_query(func(**args))
	print(x)