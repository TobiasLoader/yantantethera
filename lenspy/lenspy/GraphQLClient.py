from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


class Client:
    def __init__(self,url="https://api-mumbai.lens.dev"):
        transport = AIOHTTPTransport(url = url)
        self.client = Client(transport = transport, fetch_schema_from_transport = True)
    
    def execute_query(self,query):
        return self.client.execute(query)
