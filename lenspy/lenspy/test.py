from GraphQLClient import client
from queries import *
from gql import gql
from web3.auto import w3
from eth_account.messages import encode_defunct
import logging
logging.basicConfig(level=logging.DEBUG)

unauthorised_client = client()
# print(client.client.schema)
wallet_private_address = '1f523c0452136325ecd2d6897d7742189203aad003e4a68c328b02c11d4e963b'

wallet_public_address = '0x7CFFc134A864bc05A1Dcf73966E5bF6a20E8F6A3'

chAllenge = gql(Challenge("address:"+'"'+wallet_public_address+'"'))
print(chAllenge)
# print("mutation:"+"'"+chAllenge+"'")
# x = client.execute_query("query:"+"'"+chAllenge+"'")
challengeres = unauthorised_client.execute_query(chAllenge)
txt = challengeres['challenge']['text']

message = encode_defunct(text = txt)
signed_message = w3.eth.account.sign_message(message,private_key = wallet_private_address)
# print(signed_message.signature.hex())
# passphrase = 'hurry fiction expect volume begin juice known sister athlete seat lizard miss'




# result = web3.eth.sign(
#     wallet_public_address,
#     text = txt
# )
# print(result)


# query = gql(
#     """
#     query ping {
#     ping
#     }
#     """
# )

aUthenticate = gql(authenticate("address:"+'"'+wallet_public_address+'",'+'signature:'+'"'+signed_message.signature.hex()+'"'))
print(aUthenticate)
x = unauthorised_client.execute_query(aUthenticate)
access_token = x['authenticate']['accessToken']

authorised_client = client(token = access_token)



cREatepRofILe = gql(createProfile('handle:"tobysarcasm",profilePictureUri: null,followNFTURI: null,followModule: null'))

x = authorised_client.execute_query(query = cREatepRofILe)
print(x)


# x = client.execute_query(create_profile)
# print(x)