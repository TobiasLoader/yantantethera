from GraphQLClient import client
from queries import *

client = client()

create_profile = createProfile("handle:'Tobias Sarcasm',profilePictureUri: null,followNFTURI: null,followModule: null")

x = client.execute_query("query{{ping}}")
print(x)