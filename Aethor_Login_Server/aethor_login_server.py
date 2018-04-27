from jae_server.jae_server import JaeServer
from sql_connector.jae_connector import aedb_connector
import argparse
import json


class AethorLoginServer(JaeServer):
    def __init__(self):
        JaeServer.__init__(self, '', 52796)
        self.set_function_thread(self.message_receive)
        self.run()

    def message_receive(self, client, address):
        adbc = aedb_connector()
        adbc.connect()
        while True:
            try:
                data = client.recv(1024)
                # Need to decode to be able to access stuff
                message = data.decode('utf-8')
                print(message)
                message = json.loads(message)
                message["aethor_login_result"] = adbc.user_login(message["aethor_username"], message["aethor_password"])
                message = json.dumps(message)
                #Need to re-encode the string/dictionary before we send back to the client
                message = message.encode('utf-8')
                client.sendall(message)
            except:
                client.close()
                adbc.close()


ACS = AethorLoginServer()