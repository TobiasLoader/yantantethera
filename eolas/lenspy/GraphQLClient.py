from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from graphql.type import GraphQLSchema
import json

class client:
    def __init__(self,url="https://api-mumbai.lens.dev", token = None):
        if token != None:
            transport = AIOHTTPTransport(url = url, headers = {"Authorization":f"Bearer {token}"})
        else:
            transport = AIOHTTPTransport(url = url)

        with open('schema.graphql','r', encoding = 'utf-16') as f:
            schema_str = f.read()
            print(schema_str[0:10])
            
        self.client = Client(transport = transport, schema = schema_str)
        
    def execute_query(self,query):
        print(query)
        return self.client.execute(query)
