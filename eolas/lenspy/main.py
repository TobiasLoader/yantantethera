from lenspy.GraphQLClient import client
from queries import *
from gql import gql
from web3.auto import w3
from eth_account.messages import encode_defunct
import names
import random

def listtostr(l):
	s = '['
	for el in l:
		s += el + ','
	s = s[:-1] + ']'
	return s

def lOgin(handle_name,wallet_private_address):

	unauthorised_client = client()

	wallet_public_address = '0x7CFFc134A864bc05A1Dcf73966E5bF6a20E8F6A3'
	chAllenge = gql(Challenge("address:"+'"'+wallet_public_address+'"'))

	challengeres = unauthorised_client.execute_query(chAllenge)
	txt = challengeres['challenge']['text']

	message = encode_defunct(text = txt)
	signed_message = w3.eth.account.sign_message(message,private_key = wallet_private_address)
	aUthenticate = gql(authenticate("address:"+'"'+wallet_public_address+'",'+'signature:'+'"'+signed_message.signature.hex()+'"'))
	
	x = unauthorised_client.execute_query(aUthenticate)
	access_token = x['authenticate']['accessToken']

	authorised_client = client(token = access_token)

	handles = [handle_name]
	cREatepRofILe = gql(createProfile('handle:"{name}",profilePictureUri: null,followNFTURI: null,followModule: null'.format(handle_name)))
	x = authorised_client.execute_query(query = cREatepRofILe)
	profile_ids = [get_profileIds(authorised_client,handle_name)]

	cREatepRofILe = gql(createProfile('handle:"{name}",profilePictureUri: null,followNFTURI: null,followModule: null'.format('James')))
	x = authorised_client.execute_query(query = cREatepRofILe)
	profile_ids.append(get_profileIds(authorised_client,'James'))
	handles.append('James')

	for i in range(8):
		random_name = names.get_first_name()
		cREatepRofILe = gql(createProfile('handle:"{name}",profilePictureUri: null,followNFTURI: null,followModule: null'.format(random_name+str(random.randint(1,9000)))))
		x = authorised_client.execute_query(query = cREatepRofILe)

		handles.append(random_name)
		profile_ids.append(get_profileIds(authorised_client,random_name))


	return authorised_client, handles, profile_ids

def get_profileIds(authorised_client,handle):
	profile_query ="""
		query SearchProfiles {
	search(request: {
		query: "<here>",
		type: PROFILE,
		limit: 5
	}) {
		... on ProfileSearchResult {
		__typename
		items {
			... on Profile {
			handle
			id
			}
		}
		
		}
	}
	}
	"""	
	# profile_query = profile_query.replace('{','{{').replace('}','}}')
	profile_query = profile_query.replace('<here>',handle)

	pRofile = gql(profile_query)

	y = authorised_client(pRofile)

	return y['search']['items'][0]['id']

def follow():

	follow_query = """
	mutation createFollowTypedData {
	createFollowTypedData({
		
	}) {
		id
		expiresAt
		typedData {
		domain {
			name
			chainId
			version
			verifyingContract
		}
		types {
			FollowWithSig {
			name
			type
			}
		}
		value {
			nonce
			deadline
			profileIds
			datas
		}
		}
	}
	}
	"""


# sortcriteria = ['TOP_COMMENTED','TOP_COLLECTED','TOP_MIRRORED','LATEST','CURATED_PROFILES']
# publicationtypes = ['POST', 'COMMENT', 'MIRROR']
# def explorepublications(sortCriteria,publicationTypes,limit):
# 	return ExplorePublications("sortCriteria:"+sortCriteria+",publicationTypes: "+listtostr(publicationTypes)+",limit: "+str(limit))

# def search(query, authorised_client):
# 	profile_query ="""
# 		query SearchProfiles {
# 	search(request: {
# 		query: "<here>",
# 		type: PROFILE,
# 		limit: 5
# 	}) {
# 		... on ProfileSearchResult {
# 		__typename
# 		items {
# 			... on Profile {
# 			handle
# 			id
# 			}
# 		}
		
# 		}
# 	}
# 	}
# 	"""	

	# return SearchProfiles("query:"+query+",limit: "+str(limit))

# def searchpublications(query,limit):
# 	return SearchPublications("query:"+query+",limit: "+str(limit))

# def allpublications(profileId,publicationTypes,limit):
# 	return publications("profileId:"+profileId+",publicationTypes: "+listtostr(publicationTypes)+",limit: "+str(limit))

# def specificpublication(publicationId):
# 	return publication("publicationId:"+publicationId)

# def executequery(func,args):
# 	x = client.execute_query(func(**args))
# 	print(x)


class PubClass:
	def __init__(self,title, description, contributors, content):
		self.title = title
		self.desc = description
		self.contributors = contributors
		self.content = content